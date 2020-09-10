from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from .serializer import PostSerializer
from .models import Blog



class PostList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer