# Generated by Django 5.0.7 on 2024-12-22 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_science_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='science',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers_science', to='main.teacher'),
        ),
    ]