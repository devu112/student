from django.db import models

# Create your models here.
class StudentTable(models.Model):
    student_name=models.CharField(max_length=255)
    address=models.TextField(max_length=255)
    age=models.CharField(max_length=255)
    email=models.EmailField()
    joiningdate=models.DateField()
    gender=models.CharField(max_length=255)
    qualifiation=models.CharField(max_length=255)
    mobileno=models.CharField(max_length=255)


