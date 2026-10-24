from django.db import models

# Create your models here.
class Student(models.Model):
    #name,age,course,skills,email,mark
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    SKILLS_CHOICES=(
        ('python','Python'),
        ('django','Django'),
        ('html','HTML'),
        ('react','React')
    )
    skills=models.CharField(max_length=500,choices=SKILLS_CHOICES)
    email=models.EmailField(max_length=100)
    mark=models.IntegerField()
class SubmissionsDb(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    