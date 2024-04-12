import pandas as pd
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.core.models import Bank
from apps.core.serializers import BankSerializer, FileImportSerializer

class BankConsultViewSet(ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    @extend_schema(request=FileImportSerializer)
    @action(methods=['POST'], url_path='import', detail=False, )
    def import_data(self, request, *args, **kwargs):
        """
        Endpoint que serve de alternativa ao import do ADMIN.
        Recebe um FILE no body da requisição
        """
        excel_file = request.FILES.get('file')
        imported_list = []
        df = pd.read_excel(excel_file)
        
        for index, row in df.iterrows():
            bank, created = Bank.objects.update_or_create(
                defaults={
                    "code":row['Código de compensação'],
                    "name":row['Nome Instituição']
                },
                code=row['Código de compensação'],
                name=row['Nome Instituição']
            )
            if created:
                imported_list.append(bank)
        
        serializer = self.get_serializer(imported_list, many=True).data
        return Response(serializer)