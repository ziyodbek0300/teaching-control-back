# Generated by Django 4.0.3 on 2022-03-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_section_job_theme_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='lesson_status',
            field=models.BooleanField(default=True),
        ),
    ]