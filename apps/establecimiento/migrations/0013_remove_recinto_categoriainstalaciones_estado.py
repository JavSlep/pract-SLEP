# Generated by Django 5.1.2 on 2024-11-10 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0012_estadoinstalaciones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recinto_categoriainstalaciones',
            name='estado',
        ),
    ]