# Generated by Django 3.1 on 2020-08-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='image',
            field=models.ImageField(default='', upload_to='static/winner'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='timeStamp',
            field=models.DateTimeField(blank=True),
        ),
    ]