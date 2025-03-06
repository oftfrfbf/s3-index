import time

import pandas as pd
import pytest
from moto import mock_aws

from s3_index.aws import S3Manager
from s3_index.index import IndexManager


#######################################################
def setup_module():
    print("setup")


#######################################################
def teardown_module():
    print("teardown")


#######################################################
#######################################################
# @pytest.mark.skip(reason="requires prod credentials")
def test_build_merkle_tree():
    """
    The goal of this test is to create a merkle tree of a s3 directory.
    It will iterate over each object, record the keys, the checksum, & the
    size and organize the information into a networkx graph
    """
    input_bucket_name = "noaa-wcsd-pds"

    index_manager = IndexManager(input_bucket_name)

    foo = index_manager.build_merkle_tree()

    assert len(foo) > 0


#######################################################
#######################################################
