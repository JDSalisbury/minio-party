from minio import Minio
from minio.error import ResponseError

minioClient = Minio('play.minio.io:9000',
                    access_key='NRY1PGXB4K5N8UK9XORC',
                    secret_key='uUQtcMEoX7phtXEkmvSX+C2wH7kHNaZHm600cUKh',
                    secure=False)


# Make a bucket with the make_bucket API call.
try:
    minioClient.make_bucket("maylogs", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise
else:
    # Put object 'pumaserver_debug.log' w/ content from 'pumaserver_debug.log'.
    try:
        minioClient.fput_object(
            'maylogs', 'pumaserver_debug.log', '/tmp/pumaserver_debug.log')
    except ResponseError as err:
        print(err)
