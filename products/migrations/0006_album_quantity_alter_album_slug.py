# Generated by Django 4.0.4 on 2022-06-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_album_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(),
        ),
    ]
