from django.db import models

class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
