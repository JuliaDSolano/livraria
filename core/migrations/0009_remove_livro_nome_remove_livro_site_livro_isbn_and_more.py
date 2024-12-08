# Generated by Django 5.1.3 on 2024-12-02 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_livro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="livro",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="livro",
            name="site",
        ),
        migrations.AddField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="preco",
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="quantidade",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="titulo",
            field=models.CharField(default="livro", max_length=255),
            preserve_default=False,
        ),
    ]
