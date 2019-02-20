from .serializer import DocumentSerializer
from .models import Document
from storage import settings
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = (permissions.AllowAny,)

    def minioBucket(self, request):
        file = request.FILES.get('file')
        settings.S3_BUCKET.put_object(
            ACL='public-read-write',
            Key=file.name,
            Body=file
        )

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        self.minioBucket(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
