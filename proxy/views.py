from django.http import JsonResponse
from django.views import View
from projects.models import Project
from experience.models import Experience
from projects.serializer import ProjectSerializer
from experience.serializers import ExperienceSerializer


class BasePublicView(View):
    def add_cors_headers(self, response):
        allowed_origins = [
            "https://andres-gutierrez.vercel.app",
            "https://andres-developer-s3mh.vercel.app",
        ]
        origin = self.request.headers.get("Origin")
        if origin in allowed_origins:
            response["Access-Control-Allow-Origin"] = origin
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response


class PublicProjectsView(BasePublicView):
    def get(self, request):
        projects = Project.objects.all().order_by("-id")
        serializer = ProjectSerializer(projects, many=True)
        response = JsonResponse(serializer.data, safe=False)
        return self.add_cors_headers(response)


class PublicExperiencesView(BasePublicView):
    def get(self, request):
        experiences = Experience.objects.all().order_by("-id")
        serializer = ExperienceSerializer(experiences, many=True)
        response = JsonResponse(serializer.data, safe=False)
        return self.add_cors_headers(response)
