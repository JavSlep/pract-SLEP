# Generated by Django 5.1.2 on 2025-01-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdp', '0008_rename_pdf_year_pdf_programa_presupuestario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cdp',
            old_name='ItemPresupuestario',
            new_name='item_presupuestario',
        ),
    ]