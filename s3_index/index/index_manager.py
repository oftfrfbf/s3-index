import glob
import json
import os
import tarfile
from hashlib import sha256
import hashlib
import networkx as nx
import pandas as pd
import numpy as np
from awscrt import checksums
import base64

from s3_index.aws import S3Manager

MAX_POOL_CONNECTIONS = 64
MAX_CONCURRENCY = 64
MAX_WORKERS = 64
GB = 1024**3

import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0 B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


class IndexManager:

    def __init__(
            self,
            input_bucket_name,
    ):
        self.input_bucket_name = input_bucket_name
        self.s3_manager = S3Manager()

    #################################################################
    def get_bucket_name(self):
        return self.input_bucket_name

    def build_merkle_tree(self):
        G = nx.DiGraph()
        # https://noaa-wcsd-pds.s3.amazonaws.com/index.html#data/raw/Henry_B._Bigelow/HB0707/
        ship_name = "Henry_B._Bigelow"
        cruise_name = "HB0707"
        # cruise_name = "HB0805"
        prefix = f"data/raw/{ship_name}/{cruise_name}/"
        # prefix = f"data/raw/{ship_name}/"
        page_iterator = self.s3_manager.paginator.paginate(
            Bucket=self.input_bucket_name,
            Prefix=prefix,
        )
        for page in page_iterator:
            for contents in page["Contents"]:
                obj_key = contents["Key"]
                # https://datatracker.ietf.org/doc/html/rfc7232#section-2.3
                obj_etag = contents["ETag"].split('"')[1]  # strip away weakness param
                obj_size = contents["Size"]
                basename = os.path.basename(obj_key)
                G.add_node(
                    node_for_adding=basename,
                    ETag=obj_etag,
                    Size=obj_size,
                    Key=obj_key
                )  # TODO: add parent hash
                split_path = os.path.normpath(obj_key).split(os.path.sep)
                # split_path: ['data', 'raw', 'Henry_B._Bigelow', 'HB0707', 'EK60', 'D20070712-T004447.raw']
                for previous, current in zip(split_path, split_path[1:]):
                    if not G.has_edge(previous, current):
                        G.add_edge(previous, current)

        etag_set = frozenset(
            [k for j, k in list(G.nodes.data("ETag")) if k is not None]
        )
        new_hash = sha256(str(etag_set.__hash__()).encode("utf-8")).hexdigest()
        total_sizes = [k for j, k in list(G.nodes.data("Size")) if k is not None]
        total_size = np.sum(total_sizes)
        print()  # 22.24 Terabytes in Henry_B._Bigelow cruises
        print(f"Total: {convert_size(total_size)}")
        print(new_hash)
        print('bfs') # list(nx.bfs_predecessors(G, 'data'))[::-1]
        # print(nx.bfs_predecessors(G, 0))

        # write to json
        # data = json_graph.tree_data(G, root='data')
        # data = json_graph.tree_graph(G)
        # with open('data.json', 'w') as f:
        #     json.dump(data, f)
        # https://github.com/vasturiano/react-force-graph/blob/master/example/datasets/forcegraph-dependencies.json
        # {
        #     "nodes": [
        #         {"id": "Myriel", "group": 1},
        #         {"id": "Napoleon", "group": 1},
        #     ],
        #     "links": [
        #         {"source": "Napoleon", "target": "Myriel", "value": 1},
        #         {"source": "Mlle.Baptistine", "target": "Myriel", "value": 8},
        #     ]
        # }
        # nodes = [{'id': i[0], 'data': i[1]} for i in G.nodes(data=True)]
        # nodes = [i[1] for i in G.nodes(data=True)]
        nodes = [{'id': i[0]} for i in G.nodes(data=True)]
        links = [{"source": i[0], "target": i[1]} for i in list(G.edges)]
        output_data = {"nodes": nodes, "links": links}
        with open('data.json', 'w') as f:
            json.dump(output_data, f)

        return new_hash

    def get_total_size(self, prefixes):
        all_objects = []
        for prefix in prefixes:
            all_objects_subset = []
            print(prefix)
            page_iterator = self.s3_manager.paginator.paginate(Bucket=self.input_bucket_name, Prefix=prefix)
            for page in page_iterator:
                for contents in page["Contents"]:
                    all_objects_subset.append({'Key': contents["Key"], 'Size': contents['Size']})
                    all_objects.append({'Key': contents["Key"], 'Size': contents['Size']})
            total_sizes = [j['Size'] for j in all_objects_subset]
            print(f"Total objects: {len(total_sizes)}")
            total_size = np.sum(total_sizes)
            print(f"Total size: {convert_size(total_size)}")

        total_sizes = [j['Size'] for j in all_objects]
        print(f"Total objects: {len(total_sizes)}")
        total_size = np.sum(total_sizes) # Total size: 12.9 TB for all the data
        print(f"Total size: {convert_size(total_size)}")

    def compress_to_tar_gz(
            self,
            source_dir,
            archive_name,
    ):
        tar = tarfile.open(archive_name, "w:gz")
        for file_name in glob.glob(os.path.join(source_dir, "*")):
            print("  Adding %s..." % file_name)
            tar.add(file_name, os.path.basename(file_name))
        tar.close()

    def file_sha256_sum(self, file_name, crc64nvme=False):
        if crc64nvme:
            with open(file_name, 'rb', buffering=0) as f:
                checksum = checksums.crc64nvme(f)
                checksum_bytes = checksum.to_bytes(8, byteorder='big')  # CRC64 is 8 bytes
                checksum_base64 = base64.b64encode(checksum_bytes)
                return checksum_base64
        else:
            with open(file_name, 'rb', buffering=0) as f:
                return hashlib.file_digest(f, 'sha256').hexdigest()

    def index_s3_bucket(
            self,
            prefix,
            file_name,
    ):
        all_objects = []
        page_iterator = self.s3_manager.paginator.paginate(Bucket=self.input_bucket_name, Prefix=prefix)
        for page in page_iterator:
            for contents in page["Contents"]:
                # obj_etag = contents["ETag"].split('"')[1]  # strip away weakness param
                all_objects.append({'Key': contents["Key"], 'Size': contents['Size'], "ETag": contents["ETag"].split('"')[1]})
            #break

        total_sizes = [j['Size'] for j in all_objects]
        print(f"Total objects: {len(total_sizes)}")
        total_size = np.sum(total_sizes) # Total size: 12.9 TB for all the data
        print(f"Total size: {convert_size(total_size)}")

        data = pd.DataFrame.from_dict(all_objects)
        data.to_csv(file_name, index=False)
        # TODO: convert csv into tar.gz
        # tar c noaa-dcdb-bathymetry-pds-index.csv | gzip --best > noaa-dcdb-bathymetry-pds-index2.tar.gz
        # self.compress_to_tar_gz(source_dir=, archive_name=)
        archive_name = "noaa-wcsd-pds-index-test.tar.gz"
        tar = tarfile.open(archive_name, "w:gz")
        tar.add(file_name, os.path.basename(file_name))
        tar.close()
        # TODO: get sha sum of tar.gz
        archive_hash = self.file_sha256_sum(file_name=os.path.basename(archive_name), crc64nvme=False)
        print(archive_hash)
        # TODO: write has to file
        text_file = open(f"{archive_name}_sha256sum", "w")
        text_file.write(f"sha256:{archive_hash} {file_name}")
        text_file.close()


"""
TODO:
    noaa-wcsd-pds index is:
        sha256sum noaa-wcsd-pds-index.csv 
        315dd51ad25f552b9c30f3ce0cc0e012bb224ebbbb19c8f8d54791fbfd743ff2  noaa-wcsd-pds-index.csv
    index google 
    gsutil ls -l gs://noaa-passive-bioacoustic/


Testing started at 10:35 AM ...
Launching pytest with arguments test_index_manager.py::test_index_s3_bucket --no-header --no-summary -q in /Users/rudy/Documents/github/s3-index/tests/index
============================= test session starts ==============================
collecting ... collected 1 item
test_index_manager.py::test_index_s3_bucket setup
PASSED                       [100%]Total objects: 4292490
Total size: 293.46 TB
teardown
======================== 1 passed in 810.39s (0:13:30) =========================
Process finished with exit code 0
"""

"""
setup
PASSED                        [100%]
data/raw/Henry_B._Bigelow/HB2405/EK80/
Total objects: 176
Total size: 32.99 GB
data/raw/Henry_B._Bigelow/HB2404/EK80/
Total objects: 246
Total size: 48.02 GB
data/raw/Henry_B._Bigelow/HB2403/EK80/
Total objects: 372
Total size: 69.69 GB
data/raw/Henry_B._Bigelow/HB2402/EK80/
Total objects: 1648
Total size: 302.28 GB
data/raw/Henry_B._Bigelow/HB2401/EK80/
Total objects: 212
Total size: 41.23 GB
data/raw/Henry_B._Bigelow/HB2305/EK80/
Total objects: 11733
Total size: 1.35 TB
data/raw/Henry_B._Bigelow/HB2304/EK80/
Total objects: 1178
Total size: 224.26 GB
data/raw/Henry_B._Bigelow/HB2303/EK80/
Total objects: 11710
Total size: 2.25 TB
data/raw/Henry_B._Bigelow/HB2302/EK80/
Total objects: 1574
Total size: 153.74 GB
data/raw/Henry_B._Bigelow/HB2301/EK80/
Total objects: 835
Total size: 81.42 GB
data/raw/Henry_B._Bigelow/HB2206/EK60/
Total objects: 4044
Total size: 196.89 GB
data/raw/Pisces/PC2205/EK80/
Total objects: 1556
Total size: 564.09 GB
data/raw/Henry_B._Bigelow/HB2205/EK60/
Total objects: 1044
Total size: 48.73 GB
data/raw/Henry_B._Bigelow/HB2204/EK60/
Total objects: 1342
Total size: 65.11 GB
data/raw/Henry_B._Bigelow/HB2203/EK60/
Total objects: 282
Total size: 13.76 GB
data/raw/Henry_B._Bigelow/HB2202/EK60/
Total objects: 4596
Total size: 222.6 GB
data/raw/Henry_B._Bigelow/HB2103/EK60/
Total objects: 5428
Total size: 253.82 GB
data/raw/Henry_B._Bigelow/HB2102/EK60/
Total objects: 3484
Total size: 168.73 GB
data/raw/Pisces/PC2104/EK60/
Total objects: 1171
Total size: 55.07 GB
data/raw/Henry_B._Bigelow/HB2101/EK60/
Total objects: 14250
Total size: 695.33 GB
data/raw/Henry_B._Bigelow/HB2001/EK60/
Total objects: 1623
Total size: 52.01 GB
data/raw/Henry_B._Bigelow/HB1906/EK60/
Total objects: 5130
Total size: 167.16 GB
data/raw/Gordon_Gunter/GU1905/EK60/
Total objects: 1208
Total size: 118.0 GB
data/raw/Henry_B._Bigelow/HB1904/EK60/
Total objects: 672
Total size: 21.87 GB
data/raw/Henry_B._Bigelow/HB1907/EK60/
Total objects: 1755
Total size: 58.85 GB
data/raw/Henry_B._Bigelow/HB1903/EK60/
Total objects: 1095
Total size: 17.41 GB
data/raw/Henry_B._Bigelow/HB1902/EK60/
Total objects: 1656
Total size: 43.69 GB
data/raw/Henry_B._Bigelow/HB1901/EK60/
Total objects: 4497
Total size: 170.9 GB
data/raw/Henry_B._Bigelow/HB1806/EK60/
Total objects: 9561
Total size: 152.28 GB
data/raw/Henry_B._Bigelow/HB1805/EK60/
Total objects: 2028
Total size: 32.72 GB
data/raw/Henry_B._Bigelow/HB1803/EK60/
Total objects: 3957
Total size: 64.51 GB
data/raw/Henry_B._Bigelow/HB1802/EK60/
Total objects: 14571
Total size: 237.33 GB
data/raw/Henry_B._Bigelow/HB1801/EK60/
Total objects: 894
Total size: 14.55 GB
data/raw/Pisces/PC1706/EK60/
Total objects: 3111
Total size: 180.43 GB
data/raw/Henry_B._Bigelow/HB1702/EK60/
Total objects: 16032
Total size: 260.82 GB
data/raw/Henry_B._Bigelow/HB1701/EK60/
Total objects: 3927
Total size: 63.8 GB
data/raw/Henry_B._Bigelow/HB1604/EK60/
Total objects: 15957
Total size: 259.71 GB
data/raw/Pisces/PC1609/EK60/
Total objects: 486
Total size: 7.95 GB
data/raw/Henry_B._Bigelow/HB1603/EK60/
Total objects: 9966
Total size: 155.59 GB
data/raw/Henry_B._Bigelow/HB1601/EK60/
Total objects: 6871
Total size: 112.21 GB
data/raw/Henry_B._Bigelow/HB1507/EK60/
Total objects: 1203
Total size: 19.59 GB
data/raw/Henry_B._Bigelow/HB1506/EK60/
Total objects: 12258
Total size: 199.93 GB
data/raw/Henry_B._Bigelow/HB1503/EK60/
Total objects: 2175
Total size: 35.06 GB
data/raw/Henry_B._Bigelow/HB1502/EK60/
Total objects: 2370
Total size: 33.25 GB
data/raw/Henry_B._Bigelow/HB1501/EK60/
Total objects: 11355
Total size: 185.02 GB
data/raw/Pisces/PC1405/EK60/
Total objects: 3207
Total size: 52.31 GB
data/raw/Henry_B._Bigelow/HB1405/EK60/
Total objects: 5631
Total size: 76.75 GB
data/raw/Pisces/PC1404/EK60/
Total objects: 2265
Total size: 37.0 GB
data/raw/Henry_B._Bigelow/HB1403/EK60/
Total objects: 699
Total size: 22.39 GB
data/raw/Henry_B._Bigelow/HB1402/EK60/
Total objects: 528
Total size: 16.48 GB
data/raw/Henry_B._Bigelow/HB1401/EK60/
Total objects: 9123
Total size: 148.61 GB
data/raw/Gordon_Gunter/GU1402L1/EK60/
Total objects: 1821
Total size: 58.43 GB
data/raw/Gordon_Gunter/GU1402L2/EK60/
Total objects: 2943
Total size: 95.82 GB
data/raw/Gordon_Gunter/GU1305/EK60/
Total objects: 2076
Total size: 33.69 GB
data/raw/Henry_B._Bigelow/HB1304/EK60/
Total objects: 15232
Total size: 175.33 GB
data/raw/Okeanos_Explorer/EX1305/EK60/
Total objects: 810
Total size: 12.79 GB
data/raw/Henry_B._Bigelow/HB1303/EK60/
Total objects: 10314
Total size: 167.98 GB
data/raw/Henry_B._Bigelow/HB1301/EK60/
Total objects: 11145
Total size: 181.43 GB
data/raw/Pisces/PC1301/EK60/
Total objects: 3066
Total size: 49.63 GB
data/raw/Henry_B._Bigelow/HB1206/EK60/
Total objects: 12000
Total size: 195.35 GB
data/raw/Pisces/PC1206/EK60/
Total objects: 6264
Total size: 102.19 GB
data/raw/Henry_B._Bigelow/HB1201/EK60/
Total objects: 12570
Total size: 204.86 GB
data/raw/Henry_B._Bigelow/HB1105/EK60/
Total objects: 10431
Total size: 169.84 GB
data/raw/Delaware_Ii/DE1108/EK60/
Total objects: 4281
Total size: 69.45 GB
data/raw/Henry_B._Bigelow/HB1103/EK60/
Total objects: 8325
Total size: 134.55 GB
data/raw/Henry_B._Bigelow/HB1102/EK60/
Total objects: 7103
Total size: 115.62 GB
data/raw/Delaware_Ii/DE1010/EK60/
Total objects: 3621
Total size: 58.43 GB
data/raw/Henry_B._Bigelow/HB1006/EK60/
Total objects: 5805
Total size: 93.65 GB
data/raw/Delaware_Ii/DE0107/EK500/
Total objects: 894
Total size: 1.67 GB
data/raw/Henry_B._Bigelow/HB1002/EK60/
Total objects: 11491
Total size: 187.09 GB
data/raw/Henry_B._Bigelow/HB0905/EK60/
Total objects: 5883
Total size: 95.58 GB
data/raw/Delaware_Ii/DE0910/EK60/
Total objects: 3597
Total size: 58.57 GB
data/raw/Henry_B._Bigelow/HB0904/EK60/
Total objects: 1851
Total size: 6.05 GB
data/raw/Henry_B._Bigelow/HB0903/EK60/
Total objects: 663
Total size: 7.47 GB
data/raw/Henry_B._Bigelow/HB0902/EK60/
Total objects: 3663
Total size: 54.36 GB
data/raw/Henry_B._Bigelow/HB0901/EK60/
Total objects: 10320
Total size: 167.97 GB
data/raw/Henry_B._Bigelow/HB0807/EK60/
Total objects: 10572
Total size: 171.95 GB
data/raw/Albatross_Iv/AL0803/EK60/
Total objects: 8389
Total size: 54.68 GB
data/raw/Delaware_Ii/DE0809/EK500/
Total objects: 2411
Total size: 4.6 GB
data/raw/Henry_B._Bigelow/HB0806/EK60/
Total objects: 369
Total size: 12.8 GB
data/raw/Henry_B._Bigelow/HB0805/EK60/
Total objects: 1731
Total size: 11.1 GB
data/raw/Henry_B._Bigelow/HB0803/EK60/
Total objects: 5466
Total size: 35.6 GB
data/raw/Albatross_Iv/AL0801/EK60/
Total objects: 2391
Total size: 70.39 GB
data/raw/Henry_B._Bigelow/HB0802/EK60/
Total objects: 17388
Total size: 113.32 GB
data/raw/Henry_B._Bigelow/HB0711/EK60/
Total objects: 648
Total size: 25.56 GB
data/raw/Delaware_Ii/DE0710/EK500/
Total objects: 1494
Total size: 3.03 GB
data/raw/Henry_B._Bigelow/HB0710/EK60/
Total objects: 129
Total size: 7.97 GB
data/raw/Henry_B._Bigelow/HB0706/EK60/
Total objects: 159
Total size: 9.6 GB
data/raw/Henry_B._Bigelow/HB0707/EK60/
Total objects: 36
Total size: 1.91 GB
data/raw/Delaware_Ii/DE0615/EK500/
Total objects: 2217
Total size: 4.22 GB
data/raw/Albatross_Iv/AL0509/EK60/
Total objects: 382
Total size: 3.68 GB
data/raw/Albatross_Iv/AL0508/EK60/
Total objects: 1493
Total size: 14.51 GB
data/raw/Delaware_Ii/DE0512/EK500/
Total objects: 2359
Total size: 4.52 GB
data/raw/Delaware_Ii/DE0505/EK500/
Total objects: 329
Total size: 6.36 GB
data/raw/Albatross_Iv/AL0504/EK60/
Total objects: 271
Total size: 2.64 GB
data/raw/Albatross_Iv/AL0502/EK60/
Total objects: 662
Total size: 6.46 GB
data/raw/Albatross_Iv/AL0409/EK60/
Total objects: 2198
Total size: 32.65 GB
data/raw/Delaware_Ii/DE0413/EK500/
Total objects: 2160
Total size: 21.17 GB
data/raw/Delaware_Ii/DE0410/EK500/
Total objects: 268
Total size: 1.05 GB
data/raw/Delaware_Ii/DE0408/EK500/
Total objects: 1837
Total size: 7.21 GB
data/raw/Albatross_Iv/AL0404/EK60/
Total objects: 50
Total size: 4.58 GB
data/raw/Albatross_Iv/AL0403/EK60/
Total objects: 145
Total size: 13.06 GB
data/raw/Albatross_Iv/AL0401/EK60/
Total objects: 1114
Total size: 4.37 GB
data/raw/Albatross_Iv/AL0305/EK60/
Total objects: 7010
Total size: 27.47 GB
data/raw/Albatross_Iv/AL0304/EK60/
Total objects: 620
Total size: 2.42 GB
data/raw/Delaware_Ii/DE0306/EK500/
Total objects: 182
Total size: 722.08 MB
data/raw/Delaware_Ii/DE0303/EK500/
Total objects: 1807
Total size: 7.05 GB
data/raw/Delaware_Ii/DE0302/EK500/
Total objects: 868
Total size: 3.38 GB
data/raw/Delaware_Ii/DE0301/EK500/
Total objects: 334
Total size: 1.3 GB
data/raw/Albatross_Iv/AL0210/EK500/
Total objects: 358
Total size: 1.32 GB
data/raw/Delaware_Ii/DE0208/EK500/
Total objects: 1128
Total size: 4.38 GB
data/raw/Delaware_Ii/DE0206/EK500/
Total objects: 112
Total size: 405.55 MB
data/raw/Albatross_Iv/AL0207/EK500/
Total objects: 210
Total size: 804.11 MB
data/raw/Albatross_Iv/AL0204/EK500/
Total objects: 706
Total size: 2.64 GB
data/raw/Delaware_Ii/DE0201/EK500/
Total objects: 509
Total size: 1.96 GB
data/raw/Albatross_Iv/AL0203/EK500/
Total objects: 409
Total size: 1.54 GB
data/raw/Albatross_Iv/AL0110/EK500/
Total objects: 881
Total size: 2.68 GB
data/raw/Delaware_Ii/DE0109/EK500/
Total objects: 1136
Total size: 4.22 GB
data/raw/Delaware_Ii/DE0108/EK500/
Total objects: 1481
Total size: 2.82 GB
data/raw/Albatross_Iv/AL0105/EK500/
Total objects: 4846
Total size: 1.51 GB
data/raw/Albatross_Iv/AL0104/EK500/
Total objects: 687
Total size: 339.61 MB
data/raw/Albatross_Iv/AL0103/EK500/
Total objects: 10664
Total size: 4.55 GB
data/raw/Albatross_Iv/AL0102/EK500/
Total objects: 4800
Total size: 2.26 GB
data/raw/Delaware_Ii/DE0101/EK500/
Total objects: 7594
Total size: 1.85 GB
data/raw/Albatross_Iv/AL0007/EK500/
Total objects: 4992
Total size: 1.64 GB
data/raw/Albatross_Iv/AL0006/EK500/
Total objects: 6494
Total size: 2.87 GB
data/raw/Delaware_Ii/DE0008/EK500/
Total objects: 17765
Total size: 4.43 GB
data/raw/Delaware_Ii/DE0007/EK500/
Total objects: 1885
Total size: 847.98 MB
data/raw/Delaware_Ii/DE0005/EK500/
Total objects: 15081
Total size: 5.64 GB
data/raw/Albatross_Iv/AL0002/EK500/
Total objects: 10038
Total size: 4.4 GB
data/raw/Albatross_Iv/AL0001/EK500/
Total objects: 4024
Total size: 1.81 GB
data/raw/Delaware_Ii/DE0002/EK500/
Total objects: 1226
Total size: 330.38 MB
data/raw/Albatross_Iv/AL9911/EK500/
Total objects: 9848
Total size: 4.51 GB
data/raw/Delaware_Ii/DE9909/EK500/
Total objects: 16192
Total size: 3.78 GB
data/raw/Delaware_Ii/DE9908/EK500/
Total objects: 6147
Total size: 2.34 GB
data/raw/Delaware_Ii/DE9906/EK500/
Total objects: 413
Total size: 114.05 MB
data/raw/Albatross_Iv/AL9903/EK500/
Total objects: 10297
Total size: 4.5 GB
data/raw/Delaware_Ii/DE9903/EK500/
Total objects: 1116
Total size: 327.36 MB
data/raw/Albatross_Iv/AL9902/EK500/
Total objects: 4359
Total size: 2.12 GB
data/raw/Albatross_Iv/AL9811/EK500/
Total objects: 81
Total size: 1.9 GB
data/raw/Delaware_Ii/DE9810/EK500/
Total objects: 12564
Total size: 2.61 GB
data/raw/Delaware_Ii/DE9809/EK500/
Total objects: 2097
Total size: 488.07 MB
data/raw/Albatross_Iv/AL9804/EK500/
Total objects: 37
Total size: 698.21 MB
Total objects: 616527
Total size: 12.9 TB
"""