# Generated by Django 5.0.7 on 2024-07-26 01:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NumeroVendido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_rifa', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade_numeros', models.IntegerField(blank=True, default=0, null=True)),
                ('quantidade_numeros_vendidos', models.IntegerField(blank=True, default=0, null=True)),
                ('valor_numero', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('items', models.ManyToManyField(related_name='rifas', to='item.item')),
                ('numeros_comprados', models.ManyToManyField(blank=True, null=True, related_name='numeros_comprados', to='rifa.numerovendido')),
            ],
        ),
    ]
