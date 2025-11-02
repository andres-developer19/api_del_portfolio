from django.urls import path
from .views import ProjectsProxyView, ExperiencesProxyView

urlpatterns = [
    path('projects/', ProjectsProxyView.as_view(), name='projects-proxy'),
    path('experiences/', ExperiencesProxyView.as_view(), name='experiences-proxy'),
]
