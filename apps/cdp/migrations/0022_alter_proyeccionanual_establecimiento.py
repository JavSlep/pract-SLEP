# Generated by Django 5.1.2 on 2025-01-21 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdp', '0021_alter_proyeccionanual_year'),
        ('establecimiento', '0044_remove_tituloitemdiagnostico_orden_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyeccionanual',
            name='establecimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyeccion', to='establecimiento.establecimiento'),
        ),
    ]
