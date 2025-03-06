import os
from hashlib import sha256

import networkx as nx
import numpy as np

from s3_index.aws import S3Manager

MAX_POOL_CONNECTIONS = 64
MAX_CONCURRENCY = 64
MAX_WORKERS = 64
GB = 1024**3


class IndexManager:
    # TODO: index into dynamodb instead of csv files

    def __init__(self, input_bucket_name, calibration_bucket, calibration_key):
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
                obj_etag = contents["ETag"].split('"')[1]  # properties
                obj_size = contents["Size"]
                basename = os.path.basename(obj_key)
                G.add_node(
                    node_for_adding=basename, ETag=obj_etag, Size=obj_size, Key=obj_key
                )  # TODO: add parent hash
                split_path = os.path.normpath(obj_key).split(os.path.sep)
                # split_path: ['data', 'raw', 'Henry_B._Bigelow', 'HB0707', 'EK60', 'D20070712-T004447.raw']
                for previous, current in zip(split_path, split_path[1:]):
                    if not G.has_edge(previous, current):
                        G.add_edge(previous, current)
        # print(G)
        etag_set = frozenset(
            [k for j, k in list(G.nodes.data("ETag")) if k is not None]
        )
        new_hash = sha256(str(etag_set.__hash__()).encode("utf-8")).hexdigest()
        total_size = [k for j, k in list(G.nodes.data("Size")) if k is not None]
        print(np.sum(total_size))  # 22.24 Terabytes in Henry_B._Bigelow cruises
        print(" ")
        print(new_hash)
        return new_hash
