from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class Classroom(models.Model):
    class_id = models.CharField(max_length=10, primary_key=True)
    teachers = models.ManyToManyField(User, related_name='classrooms_as_teacher', blank=True)
    students = models.ManyToManyField(User, related_name='classrooms_as_student', blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    info = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.class_id


class Post(models.Model):
    post_id = models.CharField(max_length=20, primary_key=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='posts')
    is_edited = models.BooleanField(default=False)  # Thêm trường is_edited

    def __str__(self):
        return self.post_id


class Comment(models.Model):
    comment_id = models.CharField(max_length=10, primary_key=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

