# Generated by Django 5.0.7 on 2024-12-22 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_science_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='science',
            name='teacher',
        ),
    ]