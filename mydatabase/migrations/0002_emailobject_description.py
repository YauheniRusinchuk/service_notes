# Generated by Django 2.0.6 on 2018-08-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydatabase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailobject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
