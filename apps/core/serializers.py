from rest_framework.serializers import ModelSerializer, Serializer, FileField

from apps.core.models import Bank


class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'code',
            'name'
        ]


class FileImportSerializer(Serializer):
    file = FileField()