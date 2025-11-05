# proxy/views.py
from django.http import JsonResponse
from django.views import View
import requests
import os

class BaseProxyView(View):
    def add_cors_headers(self, response):
        response["Access-Control-Allow-Origin"] = "*"  # o tu dominio de Vercel
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

    def proxy_request(self, endpoint):
        """Hace la petición pública a la API real (sin token)."""
        try:
            PORT = os.getenv("PORT", "10000")  # Puerto interno de Render
            api_url = f"http://127.0.0.1:{PORT}/api/{endpoint}/"
            response = requests.get(api_url, timeout=20)

            if response.status_code == 200:
                json_response = JsonResponse(response.json(), safe=False)
            else:
                json_response = JsonResponse(
                    {"error": f"Error en la API: {response.status_code}"},
                    status=response.status_code
                )

            return self.add_cors_headers(json_response)

        except Exception as e:
            error_response = JsonResponse({"error": str(e)}, status=500)
            return self.add_cors_headers(error_response)


class ProjectsProxyView(BaseProxyView):
    def get(self, request):
        return self.proxy_request("projects")


class ExperiencesProxyView(BaseProxyView):
    def get(self, request):
        return self.proxy_request("experiences")
