# Generated by Django 2.0.6 on 2018-08-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydatabase', '0004_emailobject_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailobject',
            name='change',
            field=models.BooleanField(default=False),
        ),
    ]
