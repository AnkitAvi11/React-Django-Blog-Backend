# Generated by Django 3.1.6 on 2021-02-20 15:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=300)),
                ('cover_image', models.ImageField(upload_to='blogs/%Y/%/m/')),
                ('body', models.TextField()),
                ('published_on', models.DateTimeField(default=datetime.datetime(2021, 2, 20, 20, 45, 21, 422890))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
