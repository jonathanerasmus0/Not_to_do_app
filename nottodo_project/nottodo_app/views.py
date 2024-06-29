from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import NotTODO, Comment
from .serializers import NotTODOSerializer, CommentSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NotTODOViewSet(viewsets.ModelViewSet):
    queryset = NotTODO.objects.all()
    serializer_class = NotTODOSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def home(request):
    return HttpResponse("Welcome to the NotTODO App!")
