import boto3
# NOTE: We can specify proxy configuration in code or in ~/.aws/config file
# from botocore.config import Config


s3 = boto3.resource('s3')   # ,config=Config(proxies={'http': '<user>:<password>@<proxy_host>:<port_port>'}))
for bucket in s3.buckets.all():
    print(bucket.name)
