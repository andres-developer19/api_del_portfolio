from django.http import JsonResponse
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from projects.models import Project
from projects.serializer import ProjectSerializer
from experience.models import Experience
from experience.serializers import ExperienceSerializer


# --- 🧱 Clase base con soporte CORS, autenticación y serialización DRY ---
class BaseProxyView(View):
    authentication_classes = [JWTAuthentication]

    # --- 🧩 Configuración de CORS ---
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

    # --- 🔐 Autenticación JWT ---
    def authenticate(self):
        """Valida el token JWT enviado en el header Authorization."""
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

    # --- ⚙️ Helper para serializar con contexto ---
    def serialize_with_context(self, queryset, serializer_class, many=True):
        """Serializa datos incluyendo el contexto del request automáticamente."""
        return serializer_class(queryset, many=many, context={"request": self.request}).data

    # --- ⚡ Método helper para manejar respuestas seguras ---
    def safe_response(self, data=None, error=None, status=200):
        if error:
            response = JsonResponse({"error": str(error)}, status=status)
        else:
            response = JsonResponse(data, safe=False, status=status)
        return self.add_cors_headers(response)


# --- 📦 Proxy para Projects ---
class ProjectsProxyView(BaseProxyView):
    def get(self, request):
        try:
            self.authenticate()  # valida JWT
            projects = Project.objects.all()
            data = self.serialize_with_context(projects, ProjectSerializer)
            return self.safe_response(data)
        except PermissionError as e:
            return self.safe_response(error=e, status=401)
        except Exception as e:
            print("❌ Error en proxy Projects:", e)
            return self.safe_response(error=e, status=500)


# --- 💼 Proxy para Experiences ---
class ExperiencesProxyView(BaseProxyView):
    def get(self, request):
        try:
            self.authenticate()  # valida JWT
            experiences = Experience.objects.all()
            data = self.serialize_with_context(experiences, ExperienceSerializer)
            return self.safe_response(data)
        except PermissionError as e:
            return self.safe_response(error=e, status=401)
        except Exception as e:
            print("❌ Error en proxy Experiences:", e)
            return self.safe_response(error=e, status=500)
