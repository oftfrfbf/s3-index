import json
import os
from hashlib import sha256

import networkx as nx
from networkx.readwrite import json_graph
import numpy as np

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


