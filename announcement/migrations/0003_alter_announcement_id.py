# Generated by Django 4.0.5 on 2023-09-09 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_alter_announcement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]