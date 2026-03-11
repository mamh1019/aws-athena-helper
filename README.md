# AWS Athena Helper SDK

A Python SDK for simplifying AWS Athena queries, Glue workflows, and S3 operations. This library provides an easy-to-use interface for running Athena queries, managing Glue jobs, and handling S3 file operations.

## Requirements

- Python 3.7+
- pandas
- boto3

## Installation
------------
```
$ pip3 install --upgrade aws-athena-helper
```

Examples
--------
```
from aws_athena_helper import DataCenter
from aws_athena_helper.config import *

""" Athena Query Test """
if __name__ == "__main__":
    ## Athena Config - aws_athena_helper.config.AthenaConfig
    athena_config = AthenaConfig(
        s3_bucket       = '{S3_BUCKET}',
        s3_output_uri   = '{ATHENA_RESULT_S3_URI}',
        region          = '{ATHENA_REGION}',
        tmp_local_path  = '/path/to/dir'
    )

    ## SDK
    dc = DataCenter(
        aws_profile_name='{AWS_CREDENTIAL_PROFILE}',
        athena_config=athena_config
    )
    df = dc.athena.run_query('SELECT * FROM "users"', 'test_db')
    print(df)
```
