# Generated by Django 3.1 on 2021-06-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0004_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=150)),
                ('credential_id', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('issued_date', models.DateTimeField(blank=True)),
                ('certificate_link', models.CharField(max_length=1000)),
                ('instructor_name', models.CharField(max_length=150)),
            ],
        ),
    ]
