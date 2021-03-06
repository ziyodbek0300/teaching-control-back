# Generated by Django 4.0.3 on 2022-03-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures/')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Section',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.TextField()),
                ('files', models.FileField(upload_to='uploads/')),
                ('yt_video', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Theme',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255, unique=True)),
                ('position', models.IntegerField(choices=[(1, 'Administrator'), (2, 'Teacher'), (3, 'Cleaner'), (4, 'Sales Asistant'), (5, 'SMM manager'), (6, 'Designer'), (7, 'Internship')], default=2)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
    ]
