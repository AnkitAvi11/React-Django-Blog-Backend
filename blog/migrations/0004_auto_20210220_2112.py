# Generated by Django 3.1.6 on 2021-02-20 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210220_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 20, 21, 12, 59, 264928)),
        ),
    ]