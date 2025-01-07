# Generated by Django 5.1.2 on 2024-12-30 12:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('establecimiento', '0044_remove_tituloitemdiagnostico_orden_and_more'),
        ('usuario', '0005_alter_unidad_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitulo',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('n_subtitulo', models.CharField(default='', max_length=2)),
                ('denominacion', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cdp',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('numero_requerimiento', models.IntegerField()),
                ('programa', models.CharField(choices=[('01', 'Programa 01'), ('02', 'Programa 02')], max_length=2)),
                ('fondo', models.CharField(choices=[('SEP', 'SEP'), ('NORMAL/REGULAR', 'NORMAL/REGULAR'), ('PIE', 'PIE'), ('JUNJI', 'JUNJI'), ('PRO-RETENCION', 'PRO-RETENCION'), ('MANTENIMIENTO', 'MANTENIMIENTO')], max_length=20)),
                ('cuenta_contable', models.CharField(max_length=50)),
                ('cdp', models.CharField(max_length=50)),
                ('folio_sigfe', models.CharField(max_length=5)),
                ('documento', models.CharField(max_length=50)),
                ('monto', models.IntegerField()),
                ('detalle', models.CharField(max_length=500)),
                ('otros', models.CharField(max_length=100)),
                ('fecha_cdp', models.DateField()),
                ('fecha_guia_requerimiento', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('establecimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='establecimiento.establecimiento')),
                ('unidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.unidad')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('n_item', models.CharField(default='', max_length=2)),
                ('denominacion', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subtitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdp.subtitulo')),
            ],
        ),
        migrations.CreateModel(
            name='SubtituloPresupuestario',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('programa_presupuestario', models.CharField(choices=[('P01 GASTOS ADMINISTRATIVOS', 'GASTOS ADMINISTRATIVOS P01'), ('P02 SERVICIOS EDUCATIVOS', 'SERVICIOS EDUCATIVOS P02')], max_length=50)),
                ('ley_presupuestaria_subtitulo', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subtitulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdp.subtitulo')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPresupuestario',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('ley_presupuestaria_item', models.IntegerField(default=0)),
                ('monto_comprometido', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdp.item')),
                ('subtitulo_presupuestario', models.ForeignKey(default=99, on_delete=django.db.models.deletion.CASCADE, related_name='items_presupuestarios', to='cdp.subtitulopresupuestario')),
            ],
        ),
        migrations.CreateModel(
            name='EjecucionPresupuestaria',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('nivel', models.CharField(choices=[('1', 'Nivel 1'), ('2', 'Nivel 2'), ('3', 'Nivel 3')], max_length=1)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('item_presupuestario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cdp.itempresupuestario')),
                ('subtitulo_presupuestario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cdp.subtitulopresupuestario')),
            ],
        ),
    ]