# Generated by Django 3.2.18 on 2023-09-21 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20230921_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='movie/images/default.jpg', upload_to='movie/images/'),
        ),
    ]
