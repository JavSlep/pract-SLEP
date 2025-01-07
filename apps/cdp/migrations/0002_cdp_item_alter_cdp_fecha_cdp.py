# Generated by Django 5.1.2 on 2024-12-30 14:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdp',
            name='Item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cdp.item'),
        ),
        migrations.AlterField(
            model_name='cdp',
            name='fecha_cdp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
