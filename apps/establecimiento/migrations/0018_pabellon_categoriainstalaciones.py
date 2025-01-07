# Generated by Django 5.1.2 on 2024-11-11 00:08

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0017_categoriainstalaciones_icono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pabellon_CategoriaInstalaciones',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('categoria_instalaciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.categoriainstalaciones')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.estadoinstalaciones')),
                ('pabellon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='establecimiento.pabellon')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='establecimiento.planinfraestructura')),
            ],
            options={
                'verbose_name': 'Instalación Pabellon',
                'verbose_name_plural': 'Instalaciones Pabellones',
            },
        ),
    ]
