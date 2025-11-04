from django.urls import path
from .views import ProjectsProxyView, ExperiencesProxyView

urlpatterns = [
    path('projects/', ProjectsProxyView.as_view(), name='projects_proxy'),
    path('experiences/', ExperiencesProxyView.as_view(), name='experiences_proxy'),
]