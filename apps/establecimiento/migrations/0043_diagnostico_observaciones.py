# Generated by Django 5.1.2 on 2024-12-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0042_tituloitemdiagnostico_orden'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='observaciones',
            field=models.TextField(blank=True, null=True),
        ),
    ]