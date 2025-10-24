from rest_framework import viewsets, permissions
from .models import Project
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

# Create your views here.
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else: 
            permission_classes = [permissions.IsAdminUser]
        return [permissions() for permissions in permission_classes]