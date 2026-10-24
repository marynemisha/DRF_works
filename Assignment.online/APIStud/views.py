from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from APIStud.models import *
from APIStud.serializers import *
# Create your views here.

#student details
class StudentListViewCreate(APIView):
    def get(self, request):
        qs = Student.objects.all()
        serializer_instance = StudentSerializer(qs, many=True)
        return Response(data=serializer_instance.data)
    def post(self, request):
        form_data = request.data
        serializer_instance = StudentSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            Student.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class StudentView(APIView):
    def get(self, request, pk):
        qs = Student.objects.get(id=pk)
        serializer_instance = StudentSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = StudentSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            Student.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self, request, pk):
        Student.objects.filter(id=pk).delete()

        return Response(
            {"message": "Student deleted successfully!"}
        )

#assignment details
class AssignmentListCreateView(APIView):
    def get(self,request):
        qs=AssignmentDb.objects.all()
        serializer_instance=AssignmentDbSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=AssignmentDbSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data
            AssignmentDb.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
class AssignmentView(APIView):
    def get(self,request,pk):
        qs=AssignmentDb.objects.get(id=pk)
        serializer_instance=AssignmentDbSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = AssignmentDbSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            AssignmentDb.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self, request, pk):
        AssignmentDb.objects.filter(id=pk).delete()
        return Response(
            {"message": "Assignment deleted successfully!"}
        )

#submission details
class SubmissionListCreateView(APIView):
    def get(self, request):
        qs = SubmissionDb.objects.all()
        serializer_instance = SubmissionDbSerializer(qs, many=True)
        return Response(data=serializer_instance.data)
    def post(self, request):
        form_data = request.data
        serializer_instance = SubmissionDbSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data = serializer_instance.validated_data
            SubmissionDb.objects.create(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
