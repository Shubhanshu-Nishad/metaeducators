# Generated by Django 3.1 on 2020-09-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0007_auto_20200913_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='number',
            field=models.IntegerField(default=''),
        ),
    ]
