from django.db import models
from storage import settings
import uuid


def file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4}.{ext}'
    return 'app/' + settings.MEDIA_URL + filename


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=file_path)
