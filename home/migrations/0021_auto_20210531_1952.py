# Generated by Django 3.1 on 2021-05-31 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_news_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_profile',
            name='are_of_working_in_metaeducator',
            field=models.CharField(default='NULL', max_length=3),
        ),
        migrations.AddField(
            model_name='update_profile',
            name='are_we_helping_in_project',
            field=models.CharField(default='NULL', max_length=3),
        ),
        migrations.AddField(
            model_name='update_profile',
            name='are_you_doing_intrenship_through_metaeducator',
            field=models.CharField(default='NULL', max_length=3),
        ),
        migrations.AddField(
            model_name='update_profile',
            name='company_name',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='update_profile',
            name='position',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AddField(
            model_name='update_profile',
            name='project_name',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='update_profile',
            name='teacher',
            field=models.CharField(default='', max_length=3),
        ),
    ]