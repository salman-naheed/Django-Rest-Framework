from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream) #python data
        serializer = StudentSerializer(data = python_data) #complex data
        if serializer.is_valid():
            serializer.save() 
            msg = {'msg': 'Data inserted'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        json_data=  JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

