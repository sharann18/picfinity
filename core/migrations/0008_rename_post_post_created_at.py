# Generated by Django 4.2.3 on 2023-07-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_post_created_at_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Post',
            new_name='created_at',
        ),
    ]
