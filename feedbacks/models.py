from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=10)
    teacher = models.ForeignKey('users.Teacher', on_delete=models.CASCADE, related_name='teacher_feedbacks')
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, related_name='student_feedbacks')
    posted_date = models.DateTimeField()
    content = models.TextField()


