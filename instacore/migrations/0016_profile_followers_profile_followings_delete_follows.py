# Generated by Django 4.0.4 on 2022-05-10 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instacore', '0015_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='followings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Follows',
        ),
    ]
