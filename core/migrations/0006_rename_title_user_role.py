# Generated by Django 5.2 on 2025-05-05 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_user_gallery_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='title',
            new_name='role',
        ),
    ]
