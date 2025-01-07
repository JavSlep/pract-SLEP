# Generated by Django 5.1.2 on 2024-11-10 00:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0008_rename_item_partida_recinto_partida_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaInstalaciones',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoría Instalaciones',
                'verbose_name_plural': 'Categorías Instalaciones',
            },
        ),
        migrations.AddField(
            model_name='tiporecinto',
            name='categoria_instalaciones',
            field=models.ManyToManyField(blank=True, null=True, to='establecimiento.categoriainstalaciones'),
        ),
    ]
