# Generated by Django 5.1.2 on 2024-12-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdp', '0003_alter_cdp_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='CdpCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='cdp',
            name='cuenta_contable',
        ),
        migrations.AlterField(
            model_name='cdp',
            name='cdp',
            field=models.CharField(blank=True, editable=False, max_length=4),
        ),
    ]