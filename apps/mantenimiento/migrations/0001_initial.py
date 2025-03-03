# Generated by Django 5.1.2 on 2024-11-07 21:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establecimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPartidas',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='NominaPrecios',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(default=2024)),
            ],
            options={
                'verbose_name': 'nomina precio',
                'verbose_name_plural': 'nominas de precios',
            },
        ),
        migrations.CreateModel(
            name='PartidaNomina',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('unidad', models.CharField(max_length=36)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'partida',
                'verbose_name_plural': 'partidas',
            },
        ),
        migrations.CreateModel(
            name='MontoMantenimiento',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('monto', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.establecimiento')),
            ],
            options={
                'verbose_name': 'monto mantenimiento',
                'verbose_name_plural': 'monto mantenimiento',
            },
        ),
    ]
