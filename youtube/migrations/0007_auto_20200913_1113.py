# Generated by Django 3.1 on 2020-09-13 05:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0006_ytlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='video',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
