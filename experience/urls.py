from rest_framework import routers
from .views import ExperienceViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'experiences', ExperienceViewSet, basename='experience')


urlpatterns = [
    path('', include(router.urls)),
]
