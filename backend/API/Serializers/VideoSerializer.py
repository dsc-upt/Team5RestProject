from rest_framework import serializers

from backend.API.Models.ExampleModel import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['Title', 'Description', 'URL', 'Category']
