# Generated by Django 3.1 on 2020-08-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_donar'),
    ]

    operations = [
        migrations.AddField(
            model_name='donar',
            name='image',
            field=models.ImageField(default='', upload_to='static/image/donars'),
        ),
    ]