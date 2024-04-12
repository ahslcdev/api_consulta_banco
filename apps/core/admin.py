from pprint import pprint
from django.contrib import admin

from import_export import resources
from import_export.fields import Field
from import_export.widgets import IntegerWidget
from import_export.admin import ImportExportModelAdmin

from apps.core.models import Bank

class BookResource(resources.ModelResource):
    code = Field(attribute='code', column_name='Código de compensação', widget=IntegerWidget())
    name = Field(attribute='name', column_name='Nome Instituição')

    class Meta:
        model = Bank
        import_id_fields = ['code']
        

@admin.register(Bank)
class BankAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]
    list_display = ('code', 'name', )

   