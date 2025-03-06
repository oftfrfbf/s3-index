import os
from collections.abc import Generator
from typing import Optional

import boto3
from botocore import UNSIGNED
from boto3.s3.transfer import TransferConfig
from botocore.config import Config

MAX_POOL_CONNECTIONS = 64
MAX_CONCURRENCY = 64
MAX_WORKERS = 64
GB = 1024**3


#########################################################################
def chunked(ll: list, n: int) -> Generator:
    # Yields successively n-sized chunks from ll.
    for i in range(0, len(ll), n):
        yield ll[i : i + n]


class S3Manager:
    #####################################################################
    def __init__(
        self,
        # endpoint_url: Optional[str] = None,
    ):
        self.s3_region = os.environ.get("AWS_REGION", default="us-east-1")

        self.s3_client_config = Config(
            signature_version=UNSIGNED,
            max_pool_connections=MAX_POOL_CONNECTIONS,
        )

        self.s3_transfer_config = TransferConfig(
            max_concurrency=MAX_CONCURRENCY,
            use_threads=True,
            max_bandwidth=None,
            multipart_threshold=10 * GB,
        )

        self.s3_session = boto3.Session(
            region_name=self.s3_region,
        )

        self.s3_client = self.s3_session.client(
            service_name="s3",
            config=self.s3_client_config,
        )
        self.s3_resource = self.s3_session.resource(
            service_name="s3",
            config=self.s3_client_config,
        )
        self.paginator = self.s3_client.get_paginator("list_objects_v2")

    #####################################################################
    #####################################################################
    #####################################################################


#########################################################################
