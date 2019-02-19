import boto3
from botocore.client import Config


s3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='NRY1PGXB4K5N8UK9XORC',
    aws_secret_access_key='uUQtcMEoX7phtXEkmvSX+C2wH7kHNaZHm600cUKh',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

for bucket in s3.buckets.all():
    print(bucket.name)

FILE_LOCATION = r'C:\Users\jsalisbury\Downloads\Glitch7NA.mp3'
DOWNLOAD_LOCATION = r'C:\Users\jsalisbury\Downloads\TestLocation'

# uploadfile from local file system to bucket 'songs'.
s3.Bucket('local-test-media').upload_file(
    FILE_LOCATION,
    'Glitch7NA.mp3'
)

# download the object from the bucket 'songs' and save it to local
s3.Bucket('local-test-media').download_file(
    'Glitch7NA.mp3', DOWNLOAD_LOCATION)

print(
    "Downloaded '[HQ] The Glitch Mob - Seven Nation Army Remi.mp3' as  'classical.mp3'. "
)
