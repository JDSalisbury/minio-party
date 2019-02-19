from django.db import models
from django_boto.s3.storage import S3Storage

s3 = S3Storage()


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
