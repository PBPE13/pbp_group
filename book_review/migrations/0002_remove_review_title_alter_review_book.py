# Generated by Django 4.2.8 on 2023-12-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_review", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="review", name="title",),
        migrations.AlterField(
            model_name="review", name="book", field=models.CharField(max_length=255),
        ),
    ]
