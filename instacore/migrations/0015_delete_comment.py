# Generated by Django 4.0.4 on 2022-05-10 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instacore', '0014_remove_comment_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]