# Generated by Django 3.1 on 2020-09-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0016_auto_20200913_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='number',
        ),
        migrations.AddField(
            model_name='video',
            name='numbe',
            field=models.IntegerField(default='0'),
        ),
    ]