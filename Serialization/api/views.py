import django
from django.shortcuts import render
import rest_framework
from rest_framework import serializers
from .models import student
from .serializers import studentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student_detail(request, pk):
    stud = student.objects.get(id = pk)
    serializer = studentSerializer(stud)
    return JsonResponse(serializer.data)

def student_all(request):
    stud = student.objects.all()
    serializer = studentSerializer(stud, many=True)
    return JsonResponse(serializer.data, safe=False)
    