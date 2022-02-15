from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from backend.API.Models.ExampleModel import Video
from backend.API.Serializers.VideoSerializer import VideoSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
