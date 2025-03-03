# Generated by Django 5.1.2 on 2024-11-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0030_alter_partida_categoria_partida_alter_partida_codigo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUnidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Tipo Unidad',
                'verbose_name_plural': 'Tipos de unidad',
            },
        ),
        migrations.RemoveField(
            model_name='partida',
            name='unidad',
        ),
    ]
