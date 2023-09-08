# Generated by Django 4.0.5 on 2023-09-08 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_student_class_join_teacher_class_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('posted_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_feedbacks', to='users.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_feedbacks', to='users.teacher')),
            ],
        ),
    ]
