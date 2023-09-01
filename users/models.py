from djongo import models
from django.contrib.auth.models import User
from classes.models import Classroom


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    id_card = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.TextField()
    admission_year = models.PositiveIntegerField()
    isFirstLogin = models.BooleanField(default=True)
    class_join = models.ManyToManyField(Classroom, related_name='students_in_class', blank=True)




class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    id_card = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.TextField()
    hire_date = models.DateField()  # Ngày vào làm việc
    years_of_experience = models.PositiveIntegerField()  # Số năm kinh nghiệm
    graduation_school = models.CharField(max_length=255)  # Trường tốt nghiệp
    specialized_subject = models.CharField(max_length=255)  # Môn học chuyên ngành
    isFirstLogin = models.BooleanField(default=True)
    class_join = models.ManyToManyField(Classroom, related_name='teacher_in_class', blank=True)


