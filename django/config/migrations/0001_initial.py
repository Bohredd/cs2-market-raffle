# Generated by Django 5.0.7 on 2024-07-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chave', models.CharField(max_length=255)),
            ],
        ),
    ]