# Generated by Django 5.0.7 on 2024-12-22 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_room_science'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='room',
        ),
    ]
