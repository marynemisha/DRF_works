from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    question=serializers.CharField(max_length=100)
    option_a=serializers.CharField(max_length=100)
    option_b=serializers.CharField(max_length=100)
    option_c=serializers.CharField(max_length=100)
    option_d=serializers.CharField(max_length=100)
    correct_answer=serializers.CharField(max_length=100)


class SubmissionSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=100)
    question_id = serializers.IntegerField()
    answer = serializers.CharField(max_length=100)

