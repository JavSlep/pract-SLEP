# Generated by Django 5.1.2 on 2024-12-11 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0041_imagendiagnostico_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='tituloitemdiagnostico',
            name='orden',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
