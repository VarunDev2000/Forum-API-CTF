# Generated by Django 2.0 on 2019-10-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20191003_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='createdAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='posts',
            name='modifiedAt',
            field=models.DateTimeField(null=True),
        ),
    ]