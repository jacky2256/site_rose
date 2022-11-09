# Generated by Django 4.0.2 on 2022-11-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_roses_color_roses_height_roses_number_of_flowers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='roses',
            name='author',
            field=models.CharField(default='Peter J. James', max_length=100),
        ),
        migrations.AddField(
            model_name='roses',
            name='city_made',
            field=models.CharField(default='Great Britain', max_length=100),
        ),
        migrations.AddField(
            model_name='roses',
            name='title_en',
            field=models.CharField(default='Eyes for You', max_length=100),
        ),
        migrations.AddField(
            model_name='roses',
            name='year_made',
            field=models.IntegerField(default=2008),
        ),
    ]
