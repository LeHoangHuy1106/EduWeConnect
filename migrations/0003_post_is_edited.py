# Generated by Django 4.0.5 on 2023-08-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_rename_is_active_classroom_active_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
    ]