# Generated by Django 4.2.7 on 2023-12-20 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('television', '0003_remove_televisiontype_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='television.filestatus', verbose_name='File status'),
        ),
    ]
