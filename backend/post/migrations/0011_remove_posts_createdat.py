# Generated by Django 2.0 on 2019-10-03 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20191003_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='createdAt',
        ),
    ]
