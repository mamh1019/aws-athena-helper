import sys; import os; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from aws_athena_helper import DataCenter
from aws_athena_helper.config import *

""" Athena Query Test """
if __name__ == "__main__":
    glue_config = GlueConfig(
        region = 'ap-northeast-1'
    )

    ## SDK
    dc = DataCenter(
        aws_profile_name='{AWS_PROFILE}',
        glue_config=glue_config
    )

    prefix = ','.join(['test_prefix'])
    log_date = ','.join(['20210301','20210304','20210307'])

    res = dc.glue.job_run(
        name='test_job',
        params={'prefix':prefix, 'log_date': log_date}
    )
    print(res)