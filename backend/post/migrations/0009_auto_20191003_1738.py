# Generated by Django 2.0 on 2019-10-03 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20191003_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 3, 17, 38, 27, 430312), null=True),
        ),
    ]
