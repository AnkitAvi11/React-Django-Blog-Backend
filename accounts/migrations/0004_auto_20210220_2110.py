# Generated by Django 3.1.6 on 2021-02-20 15:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210220_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='joined_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 20, 21, 10, 51, 139888)),
        ),
    ]
