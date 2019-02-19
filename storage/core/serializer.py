from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = (
            'id',
            'uploaded_at',
            'file',
        )
        read_only_fields = ['id', 'uploaded_at', ]
