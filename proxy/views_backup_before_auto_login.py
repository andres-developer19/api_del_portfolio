from django.http import JsonResponse
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from projects.models import Project
from projects.serializer import ProjectSerializer
from experience.models import Experience
from experience.serializers import ExperienceSerializer

# --- 🧱 Clase base con soporte CORS y JWT ---
class BaseProxyView(View):
    authentication_classes = [JWTAuthentication]

    def add_cors_headers(self, response):
        allowed_origins = [
            "https://andres-gutierrez.vercel.app",
            "https://andres-developer-s3mh.vercel.app",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
        origin = self.request.headers.get("Origin")
        if origin in allowed_origins:
            response["Access-Control-Allow-Origin"] = origin
            response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
            response["Access-Control-Allow-Credentials"] = "true"
        return response

    def options(self, request, *args, **kwargs):
        """Responde a las peticiones OPTIONS (preflight de CORS)."""
        response = JsonResponse({"detail": "OK"})
        return self.add_cors_headers(response)

    def authenticate(self):
        """Valida JWT enviado en Authorization header."""
        auth_header = self.request.headers.get("Authorization")
        if not auth_header:
            raise PermissionError("Falta el token de autorización")

        try:
            auth = JWTAuthentication()
            validated_token = auth.get_validated_token(auth_header.split()[1])
            user = auth.get_user(validated_token)
            return user
        except (InvalidToken, TokenError, IndexError) as e:
            raise PermissionError(f"Token inválido: {str(e)}")


# --- 📦 Proxy para Projects ---
class ProjectsProxyView(BaseProxyView):
    def get(self, request):
        try:
            user = self.authenticate()  # valida JWT
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True, context={'request': request})
            response = JsonResponse(serializer.data, safe=False)
            return self.add_cors_headers(response)
        except PermissionError as e:
            response = JsonResponse({"error": str(e)}, status=401)
            return self.add_cors_headers(response)
        except Exception as e:
            print("❌ Error en proxy Projects:", e)
            response = JsonResponse({"error": str(e)}, status=500)
            return self.add_cors_headers(response)


# --- 💼 Proxy para Experiences ---
class ExperiencesProxyView(BaseProxyView):
    def get(self, request):
        try:
            user = self.authenticate()  # valida JWT
            experiences = Experience.objects.all()
            serializer = ExperienceSerializer(experiences, many=True, context={'request': request})
            response = JsonResponse(serializer.data, safe=False)
            return self.add_cors_headers(response)
        except PermissionError as e:
            response = JsonResponse({"error": str(e)}, status=401)
            return self.add_cors_headers(response)
        except Exception as e:
            print("❌ Error en proxy Experiences:", e)
            response = JsonResponse({"error": str(e)}, status=500)
            return self.add_cors_headers(response)
