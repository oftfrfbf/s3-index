from moto import mock_aws

from s3_index.aws import S3Manager


#######################################################
def setup_module():
    print("setup")


def teardown_module():
    print("teardown")


#######################################################
@mock_aws
def test_s3_manager(tmp_path):
    s3_manager = S3Manager()
    page_iterator = s3_manager.paginator.paginate(
        Bucket="test_bucket",
        Prefix="/asdf",
    )

    assert page_iterator