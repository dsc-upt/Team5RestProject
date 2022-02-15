from rest_framework import serializers

from API.Models.ExampleModel import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['Name']
