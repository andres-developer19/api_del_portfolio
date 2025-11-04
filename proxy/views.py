import os
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views import View

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
            # si tu JWT dura 5 minutos, puedes ajustar aquí
            self.token_expiration = datetime.now() + timedelta(minutes=4)
            return self.token
        else:
            raise Exception("Error al obtener token JWT")

    def proxy_request(self, endpoint):
        """Hace la petición a la API original con autenticación automática."""
        token = self.get_token()
        headers = {"Authorization": f"Bearer {token}"}
        api_url = f"https://portfolio-api-x6xk.onrender.com/{endpoint}/"  # tu API real
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            return JsonResponse(response.json(), safe=False)
        else:
            return JsonResponse({"error": "Error al obtener datos del backend"}, status=response.status_code)


class ProjectsProxyView(BaseProxyView):
    def get(self, request):
        return self.proxy_request("projects")


class ExperiencesProxyView(BaseProxyView):
    def get(self, request):
        return self.proxy_request("experiences")
