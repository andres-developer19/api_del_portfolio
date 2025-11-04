from rest_framework import viewsets, permissions
from .models import Project
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer


    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]  # GET, HEAD, OPTIONS → público
        return [permissions.IsAuthenticated()]  # POST, PUT, DELETE → requiere token