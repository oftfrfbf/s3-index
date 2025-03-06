from moto import mock_aws

from s3_index.aws import S3Manager

input_bucket_name = "example_input_bucket"
output_bucket_name = "example_output_bucket"

#######################################################
def setup_module():
    print("setup")


def teardown_module():
    print("teardown")

# @pytest.fixture
# def s3_manager_test_path(test_path):
#     return test_path["S3_MANAGER_TEST_PATH"]


#######################################################
@mock_aws
def test_s3_manager(tmp_path):
    s3_manager = S3Manager()
    paginator = s3_manager.paginator

    assert paginator