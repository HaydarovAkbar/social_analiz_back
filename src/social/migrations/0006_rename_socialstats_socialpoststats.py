# Generated by Django 4.2.7 on 2023-12-05 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_socialpost_state_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialStats',
            new_name='SocialPostStats',
        ),
    ]
