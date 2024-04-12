# Generated by Django 4.2.11 on 2024-04-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Código de compensação')),
                ('name', models.CharField(max_length=255, verbose_name='Nome da instituição')),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
            },
        ),
    ]
