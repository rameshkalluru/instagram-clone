# Generated by Django 4.0.4 on 2022-05-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instacore', '0016_profile_followers_profile_followings_delete_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]