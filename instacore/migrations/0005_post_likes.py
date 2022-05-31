# Generated by Django 4.0.4 on 2022-05-05 07:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instacore', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post', to=settings.AUTH_USER_MODEL),
        ),
    ]
