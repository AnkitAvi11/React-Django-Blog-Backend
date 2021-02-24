# Generated by Django 3.1.6 on 2021-02-24 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210221_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 11, 42, 0, 492523)),
        ),
    ]