from django.db import models

class Announcement(models.Model):
    announcement_id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_date = models.DateTimeField()

