# Generated by Django 5.1.2 on 2024-11-08 15:55

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0003_partida_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanInfraestructura',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.IntegerField(choices=[(1, 'Borrador'), (2, 'Enviado'), (3, 'Observado'), (4, 'Aprobado'), (5, 'Eliminado')], default=1)),
                ('year', models.IntegerField(default=2024)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.establecimiento')),
            ],
            options={
                'verbose_name': 'Plan Infraestructura',
                'verbose_name_plural': 'Planes Infraestructura',
            },
        ),
    ]
