from rest_framework import routers
from .views import ExperienceViewSet

router = routers.DefaultRouter()
router.register(r'experiences', ExperienceViewSet, basename='experience')

urlpatterns = router.urls
