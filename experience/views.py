from rest_framework import viewsets, permissions
from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]  # GET, HEAD, OPTIONS → público
        return [permissions.IsAuthenticated()]  # POST, PUT, DELETE → requiere token