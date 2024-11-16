from django.db import models

# Create your models here.

class Timetable(models.Model):
    teacher_name = models.CharField(max_length=30)
    dept_name = models.CharField(max_length=5,blank=False)
    day = models.CharField(max_length=8,blank=False,default="")
    slot1 = models.IntegerField()
    slot2 = models.IntegerField()
    slot3 = models.IntegerField()
    slot4 = models.IntegerField()
    slot5 = models.IntegerField()
    slot6 = models.IntegerField()
    slot7 = models.IntegerField()
    teacher_mail = models.CharField(max_length=55)

    def __str__(self):
        return self.teacher_name    

class Student(models.Model):
    student_name=models.CharField(max_length=30)
    dept_name = models.CharField(max_length=5,blank=False)
    student_id=models.CharField(max_length=30,blank=False)

    def __str__(self):
         return self.student_id
