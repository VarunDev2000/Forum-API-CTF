# Generated by Django 2.0 on 2019-10-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_posts_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='createdAt',
            field=models.DateTimeField(null=True),
        ),
    ]
