# Generated by Django 5.1.2 on 2024-11-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0018_pabellon_categoriainstalaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadoinstalaciones',
            name='background_color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='estadoinstalaciones',
            name='text_color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]