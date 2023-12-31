# Generated by Django 4.2.7 on 2023-12-20 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0003_remove_organization_language'),
        ('utils', '0004_instruction'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelevisionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.state')),
            ],
            options={
                'verbose_name': 'Television type',
                'verbose_name_plural': 'Television types',
                'db_table': 'television_type',
            },
        ),
        migrations.CreateModel(
            name='FileStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.state')),
            ],
            options={
                'verbose_name': 'File status',
                'verbose_name_plural': 'File statuses',
                'db_table': 'file_status',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=250)),
                ('file_id', models.CharField(blank=True, max_length=250, null=True)),
                ('file_extension', models.CharField(blank=True, max_length=250, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('post_date', models.DateField(blank=True, null=True, verbose_name='Post date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='organization.organization', verbose_name='Organization')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.state')),
                ('television_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='files', to='television.televisiontype', verbose_name='Television type')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
                'db_table': 'files',
                'indexes': [models.Index(fields=['file_name'], name='files_file_na_85b89e_idx'), models.Index(fields=['post_date'], name='files_post_da_1a2067_idx')],
            },
        ),
    ]
