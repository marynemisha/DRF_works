from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ExamApp.models import *
from ExamApp.serializers import *
# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionsDb.objects.all()
        serializers_instance=QuestionSerializer(qs,many=True)
        return Response(data=serializers_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionsDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class QuestionsRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=QuestionsDb.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            original_data=serializer_instance.validated_data
            QuestionsDb.objects.filter(id=pk).update(**original_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        QuestionsDb.objects.filter(id=pk).delete()
        return Response(
            {"message":"Questions deleted successfully...!"}
        )



class SubmissionListCreateView(APIView):
    def get(self, request):
        qs = SubmissionsDb.objects.all()
        serializer_instance = SubmissionSerializer(qs, many=True)
        return Response(data=serializer_instance.data)
    def post(self, request):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            original = serializer_instance.validated_data
            SubmissionsDb.objects.create(**original)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class SubmissionRetrieveUpdateDelete(APIView):
    def get(self, request, pk):
        qs = get_object_or_404(SubmissionsDb, id=pk)
        serializer_instance = SubmissionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self, request, pk):
        form_data = request.data
        serializer_instance = SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual = serializer_instance.validated_data
            SubmissionsDb.objects.filter(id=pk).update(**actual)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self, request, pk):
        SubmissionsDb.objects.filter(id=pk).delete()
        return Response({
            "message": "Submission deleted successfully!"
        })

class EvaluateSubmissionView(APIView):
    def put(self, request, pk):
        form_data = request.data
        SubmissionsDb.objects.filter(id=pk).update(**form_data)
        return Response(data={
            "Message": "Submission evaluated successfully!"
        })
