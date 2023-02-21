import boto3
import csv
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket_name)
    print(key)
    res = s3.get_object(Bucket=bucket_name,Key=key)
    print(res)
    data = res['Body'].read().decode('utf-8')
    reader = csv.reader(io.StringIO(data))
    next(reader)
    for row in reader:
        print(row[0],row[1],row[2])