# Generated by Django 4.2.7 on 2023-12-06 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_socialpoststats_social_stat_post_id_052e2b_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='socialpost',
            name='social_post_social__ab1d72_idx',
        ),
        migrations.RemoveField(
            model_name='socialpost',
            name='social',
        ),
        migrations.AddField(
            model_name='socialpost',
            name='social_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='social.socialtypes'),
        ),
        migrations.AddIndex(
            model_name='socialpost',
            index=models.Index(fields=['social_type'], name='social_post_social__8be0b5_idx'),
        ),
    ]
