from rest_framework import viewsets, permissions
from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

def get_permissions(self):
    if self.action in ['list', 'retrieve']:
        permission_classes = [permissions.IsAuthenticated]  # lectura con token
    else:
        permission_classes = [permissions.IsAdminUser]  # escritura solo admins
    return [permission() for permission in permission_classes]