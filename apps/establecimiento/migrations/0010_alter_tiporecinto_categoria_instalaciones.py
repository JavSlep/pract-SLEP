# Generated by Django 5.1.2 on 2024-11-10 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0009_categoriainstalaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiporecinto',
            name='categoria_instalaciones',
            field=models.ManyToManyField(blank=True, to='establecimiento.categoriainstalaciones'),
        ),
    ]
