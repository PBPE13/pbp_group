# Generated by Django 4.2.7 on 2023-12-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('average_rating', models.FloatField(blank=True, null=True)),
                ('isbn', models.TextField(blank=True, null=True)),
                ('isbn13', models.IntegerField(blank=True, null=True)),
                ('language_code', models.TextField(blank=True, null=True)),
                ('num_pages', models.IntegerField(blank=True, null=True)),
                ('ratings_count', models.IntegerField(blank=True, null=True)),
                ('text_review_count', models.IntegerField(blank=True, null=True)),
                ('publication_date', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
