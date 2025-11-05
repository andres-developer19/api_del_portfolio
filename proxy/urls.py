from django.urls import path
from .views import PublicProjectsView, PublicExperiencesView

urlpatterns = [
    path("projects/", PublicProjectsView.as_view(), name="public-projects"),
    path("experiences/", PublicExperiencesView.as_view(), name="public-experiences"),
]
