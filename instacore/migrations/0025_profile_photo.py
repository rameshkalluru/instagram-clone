# Generated by Django 4.0.4 on 2022-05-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instacore', '0024_profile_bio_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='profile pics'),
        ),
    ]