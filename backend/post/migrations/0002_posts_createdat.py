# Generated by Django 2.0 on 2019-10-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
