from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .serializer import DocumentSerializer
from .models import Document
import boto3
from rest_framework import permissions, viewsets
from botocore.client import Config
import logging

s3 = boto3.resource(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='NRY1PGXB4K5N8UK9XORC',
    aws_secret_access_key='uUQtcMEoX7phtXEkmvSX+C2wH7kHNaZHm600cUKh',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

logger = logging.getLogger(__name__)


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print("-------------Print")
        print(*args)
        print(**kwargs)
        logging.warning('Test')
        return self.create(request, *args, **kwargs)


class DocumentCreateView(CreateView):
    model = Document
    fields = ['file', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        context['documents'] = documents
        return context

    def post(self, request, *args, **kwargs):
        print("==========THIS=========")
        print(request)
        print("asdfasd")
        s3.Bucket('local-test-media').upload_file(
            Filename=f'{self}', Key=self)
