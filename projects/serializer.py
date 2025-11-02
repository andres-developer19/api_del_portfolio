from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "image",
            "url",
            "technologies",
            "created_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
