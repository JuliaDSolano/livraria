# Generated by Django 5.1.4 on 2025-01-25 12:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_itenscompra_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
