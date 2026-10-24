from rest_framework import serializers
from APIStud.models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    course = serializers.CharField(max_length=100)
    skills = serializers.ChoiceField(choices=Student.SKILLS_CHOICES)
    email = serializers.EmailField(max_length=100)
    mark = serializers.IntegerField()
class AssignmentDbSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=100)
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    marks = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)
class SubmissionDbSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    assignment_id = serializers.IntegerField()
    answer = serializers.CharField()
    submit_date = serializers.DateTimeField()
    score = serializers.IntegerField()