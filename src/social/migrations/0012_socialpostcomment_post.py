# Generated by Django 4.2.7 on 2023-12-12 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_remove_socialpostcomment_reply_to_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpostcomment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='social.socialpost'),
        ),
    ]