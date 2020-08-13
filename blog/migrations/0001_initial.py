# Generated by Django 3.1 on 2020-08-11 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=90)),
                ('author', models.CharField(max_length=13)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]