import os
import requests
from django.http import JsonResponse
from django.views import View


# --- 🔑 Función para obtener un nuevo access token automáticamente ---
def get_access_token():
    refresh_token = "eyJhbGciOiJIUzeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2MjcwMzk5NSwiaWF0IjoxNzYyMDk5MTk1LCJqdGkiOiIyOWFkNGRiYTRmZDk0NThkYmMyYmYzMzAyMGFkMDY2YSIsInVzZXJfaWQiOiIxIn0.ngBKRMXYTEv6kiEph1vm7zK5JCEzv2E93hMb4XT_1yU"#os.environ.get("API_REFRESH_TOKEN")

    if not refresh_token:
        raise ValueError("Falta la variable de entorno API_REFRESH_TOKEN")

    resp = requests.post("https://portfolio-api-x6xk.onrender.com/api/token/refresh/",json={"refresh": refresh_token},    )

    if resp.status_code != 200:
        raise ValueError(f"Error al refrescar token: {resp.text}")

    return resp.json()["access"]


# --- 🧱 Clase base con soporte CORS ---
class BaseProxyView(View):
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


# --- 📦 Proxy para Projects ---
class ProjectsProxyView(BaseProxyView):
    def get(self, request):
        try:
            access = get_access_token()
            headers = {"Authorization": f"Bearer {access}"}

            r = requests.get(
                "https://portfolio-api-x6xk.onrender.com/api/projects/",
                headers=headers,
                timeout=10,
            )
            r.raise_for_status()

            response = JsonResponse(r.json(), safe=False)
            return self.add_cors_headers(response)

        except Exception as e:
            response = JsonResponse({"error": str(e)}, status=500)
            return self.add_cors_headers(response)


# --- 💼 Proxy para Experiences ---
class ExperiencesProxyView(BaseProxyView):
    def get(self, request):
        try:
            access = get_access_token()
            headers = {"Authorization": f"Bearer {access}"}

            r = requests.get(
                "https://portfolio-api-x6xk.onrender.com/api/experiences/",
                headers=headers,
                timeout=10,
            )
            r.raise_for_status()

            response = JsonResponse(r.json(), safe=False)
            return self.add_cors_headers(response)

        except Exception as e:
            response = JsonResponse({"error": str(e)}, status=500)
            return self.add_cors_headers(response)
