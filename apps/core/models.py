from django.db import models

# Create your models here.

class Bank(models.Model):
    code = models.IntegerField(
        primary_key=True, 
        verbose_name='Código de compensação', 
        unique=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Nome da instituição'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
