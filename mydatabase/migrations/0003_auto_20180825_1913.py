# Generated by Django 2.0.6 on 2018-08-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydatabase', '0002_emailobject_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailobject',
            options={'ordering': ['-create_data']},
        ),
        migrations.AddField(
            model_name='emailobject',
            name='create_data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]