# Generated by Django 2.0.6 on 2018-08-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ava',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/'),
        ),
    ]