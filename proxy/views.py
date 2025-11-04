from django.http import JsonResponse
from django.views import View
import os, requests
from datetime import datetime, timedelta

class BaseProxyView(View):
    token = None
    token_expiration = None

    def get_token(self):
        """Obtiene o renueva el token JWT automáticamente desde variables de entorno."""
        if self.token and self.token_expiration and datetime.now() < self.token_expiration:
            return self.token

        login_url = os.getenv("API_LOGIN_URL")
        username = os.getenv("API_USERNAME")
        password = os.getenv("API_PASSWORD")

        response = requests.post(login_url, data={"username": username, "password": password})
        if response.status_code == 200:
            data = response.json()
            self.token = data.get("access")
            self.token_expiration = datetime.now() + timedelta(minutes=4)
            return self.token
        else:
            raise Exception("Error al obtener token JWT")

    def add_cors_headers(self, response):
        """Agrega los encabezados CORS necesarios."""
        response["Access-Control-Allow-Origin"] = "*"  # o tu dominio exacto
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

    def proxy_request(self, endpoint):
        """Hace la petición a la API original con autenticación automática."""
        try:
            token = self.get_token()
            headers = {"Authorization": f"Bearer {token}"}
            api_url = f"https://portfolio-api-x6xk.onrender.com/{endpoint}/"
            response = requests.get(api_url, headers=headers)

            json_response = JsonResponse(response.json(), safe=False, status=response.status_code)
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
