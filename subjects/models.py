from django.db import models


class Subject(models.Model):
    id_subject = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
