from django.db import models

class Feedback(models.Model):
    feedback_id = models.CharField(primary_key=True, max_length=10)
    teacher = models.ForeignKey('users.Teacher', on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
    content = models.TextField()
