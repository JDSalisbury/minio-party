from django.db import models
from storage import settings
import uuid


def file_path(instance, filename):
    name = filename.split('.')[0]
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4}--{name}.{ext}'
    return 'app/' + settings.MEDIA_URL + filename


def minioBucket(self):
    settings.S3_BUCKET.put_object(
        ACL='public-read-write',
        Key=self.file.name,
        Body=self.file
    )


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=file_path)

    def save(self, *args, **kwargs):
        super(Document, self).save(*args, **kwargs)
        minioBucket(self)
