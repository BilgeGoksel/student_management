from django.db import models

# Create your models here.

class Student(models.Model):
    student_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    exam_score = models.IntegerField()

    def __str__(self):
        return f"{self.student_number} - {self.first_name} {self.last_name}"
