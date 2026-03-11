import sys; import os; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from aws_athena_helper import DataCenter
from aws_athena_helper.config import *

""" S3 Test """
if __name__ == "__main__":
    print('S3 Test ====>>>>>>')

    ## SDK
    dc = DataCenter(
        aws_profile_name='{AWS_PROFILE}',
        s3_config = S3Config(
          bucket = '{S3_BUCKET}'
        )
    )

    # print(dc)
    response = dc.s3.upload('/path/to/dir', '{s3_object_name}')
    print(response)