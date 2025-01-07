# Generated by Django 5.1.2 on 2024-11-14 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0029_partida_categoria_partida'),
        ('mantenimiento', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='categoria_partida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='establecimiento.categoriapartida', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='partida_nomina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Partida_mantencion', to='mantenimiento.partidanomina', verbose_name='Partida Asociada (Nómina de Precios Mantención)'),
        ),
        migrations.AlterField(
            model_name='partida',
            name='unidad',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Unidad'),
        ),
    ]