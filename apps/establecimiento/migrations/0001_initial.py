# Generated by Django 5.1.2 on 2024-11-07 21:19

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEstablecimiento',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'categoría establecimiento',
                'verbose_name_plural': 'categorías de establecimientos',
            },
        ),
        migrations.CreateModel(
            name='CategoriaRecinto',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Categoría Recintos',
                'verbose_name_plural': 'Categorías de Recintos',
            },
        ),
        migrations.CreateModel(
            name='EstadoRecinto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=36)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Estado Infraestructura',
                'verbose_name_plural': 'Estados Infraestructura',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Items',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='MaterialidadPabellon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'materialidad pabellon',
                'verbose_name_plural': 'materialidades pabellones',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=200)),
                ('unidad', models.CharField(max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Partida',
                'verbose_name_plural': 'Partidas',
            },
        ),
        migrations.CreateModel(
            name='Recinto',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=36)),
                ('piso', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Recinto pabellon',
                'verbose_name_plural': 'Recinto pabellones',
            },
        ),
        migrations.CreateModel(
            name='Recinto_Partida',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Partida Recinto Pabellon',
                'verbose_name_plural': 'Partidas Recinto Pabellones',
            },
        ),
        migrations.CreateModel(
            name='TipoRecinto',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Tipo Recinto',
                'verbose_name_plural': 'Tipos de Recinto',
            },
        ),
        migrations.CreateModel(
            name='TipoRecinto_Item',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Item Partida',
                'verbose_name_plural': 'Items Partidas',
            },
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('digito', models.CharField(blank=True, max_length=1, null=True)),
                ('letra_numero', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('direccion', models.CharField(max_length=100)),
                ('zona_geografica', models.IntegerField(choices=[(1, 'Urbano'), (2, 'Rural')], default=1)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono1', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=50, null=True)),
                ('email_establecimiento', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_director', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='establecimiento.categoriaestablecimiento')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='general.region')),
            ],
            options={
                'verbose_name': 'establecimiento',
                'verbose_name_plural': 'establecimientos',
            },
        ),
        migrations.CreateModel(
            name='Item_Partida',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.item')),
            ],
            options={
                'verbose_name': 'Item Partida',
                'verbose_name_plural': 'Items Partidas',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('matricula', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.establecimiento')),
            ],
            options={
                'verbose_name': 'matricula',
                'verbose_name_plural': 'matriculas',
            },
        ),
        migrations.CreateModel(
            name='Pabellon',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre', models.CharField(max_length=200)),
                ('numero_pisos', models.IntegerField(choices=[(1, '1 Piso'), (2, '2 Pisos'), (3, '3 Pisos'), (4, '4 Pisos'), (5, '5 Pisos')], default=1)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='establecimiento.establecimiento')),
            ],
            options={
                'verbose_name': 'pabellon',
                'verbose_name_plural': 'pabellones',
            },
        ),
    ]