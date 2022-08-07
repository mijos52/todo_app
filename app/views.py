from urllib import response
from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_todo(request):
    todo_data = Todo.objects.all()
    serializer = TodoSerializer(todo_data,many=True)
    return Response(serializer.data)



@api_view(["POST"])
def create_todo(request):
    serializer = TodoSerializer(request.data)
    return Response(serializer.data)






