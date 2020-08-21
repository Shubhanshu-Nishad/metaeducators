# Generated by Django 3.1 on 2020-08-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donar',
            fields=[
                ('donar_id', models.AutoField(primary_key=True, serialize=False)),
                ('donar_name', models.CharField(max_length=100)),
                ('donar_amount', models.CharField(max_length=25)),
                ('donar_professional', models.CharField(max_length=13)),
                ('donar_desc', models.TextField()),
            ],
        ),
    ]