import os
import boto3
import logging
from botocore.exceptions import ClientError
import os

session = boto3.Session(aws_access_key_id="AKIA3IW35XTIN24JY3UQ",
aws_secret_access_key="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"
)


s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

data=open('Screenshot from 2022-11-30 15-33-29.png','rb')
s3.Bucket(bucket.name).put_object(Key='Screenshot from 2022-11-30 15-33-29.png', Body=data)