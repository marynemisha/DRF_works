from rest_framework import serializers
from APIStud.models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    course = serializers.CharField(max_length=100)
    skills = serializers.ChoiceField(choices=Student.SKILLS_CHOICES)
    email = serializers.EmailField(max_length=100)
    mark = serializers.IntegerField()
class SubmissionSerializer(serializers.Serializer):
    name=models.CharField(max_length=100)
    description=models.TextField()
    points=models.PositiveIntegerField()
        