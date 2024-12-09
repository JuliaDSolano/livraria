# Generated by Django 5.1.3 on 2024-12-08 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_livro_editora"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(blank=True, related_name="livros", to="core.autor"),
        ),
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.categoria",
            ),
        ),
    ]