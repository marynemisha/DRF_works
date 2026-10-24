from django.db import models

# Create your models here.
"""
Schema_name :QuestionsDb
Fields      :title,language,difficulty_level,score,topic,notes,
             published_date,sample_input,sample_output,is_active
"""

class QuestionsDb(models.Model):
    title=models.CharField(max_length=200)

    LANGUAGE_CHOICES=(
        ('python','Python'),
        ('java','Java'),
        ('cpp','C++'),
    )
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES)

    DIFFICULTY_CHOICES=(
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard'),
    )
    difficulty_level=models.CharField(max_length=100,choices=DIFFICULTY_CHOICES)

    score=models.IntegerField()

    topic=models.CharField(max_length=100)

    notes=models.TextField()

    published_date=models.DateTimeField(auto_now_add=True)

    sample_input=models.TextField()

    sample_output=models.TextField()

    is_active=models.BooleanField(default=True)



class SubmissionsDb(models.Model):
    answer=models.TextField()
    question_id=models.IntegerField()
    owner=models.CharField(max_length=200)
    points=models.PositiveIntegerField(null=True)
    submission_date=models.DateTimeField(auto_now_add=True)
    remarks=models.TextField(null=True)