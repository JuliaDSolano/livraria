# Generated by Django 5.1.4 on 2024-12-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_livro_capa"),
    ]

    operations = [
        migrations.AddField(
            model_name="autor",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="editora",
            name="cidade",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
