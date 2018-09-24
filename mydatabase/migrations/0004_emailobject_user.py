# Generated by Django 2.0.6 on 2018-08-25 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mydatabase', '0003_auto_20180825_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailobject',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]