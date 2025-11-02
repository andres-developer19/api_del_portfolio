from rest_framework import viewsets, permissions
from .models import Project
from .serializer import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

    def get_permissions(self):
        # Lectura pública
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        # Modificaciones solo para administradores
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
