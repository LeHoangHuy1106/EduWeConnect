# Generated by Django 4.0.5 on 2023-08-30 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='is_active',
            new_name='active_status',
        ),
    ]
