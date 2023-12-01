# Generated by Django 4.2.7 on 2023-12-01 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
                'db_table': 'level',
            },
        ),
        migrations.CreateModel(
            name='LevelCredantials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.PositiveIntegerField(default=1)),
                ('score2', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='level.level')),
            ],
            options={
                'verbose_name': 'Level Credantial',
                'verbose_name_plural': 'Level Credantials',
                'db_table': 'level_credantials',
            },
        ),
    ]