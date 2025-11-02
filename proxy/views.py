import os
import requests
from django.http import JsonResponse
from django.views import View

# Función para obtener un access token desde el refresh token
def get_access_token():
    refresh_token = os.environ.get("API_REFRESH_TOKEN")
    if not refresh_token:
        raise ValueError("No se encontró la variable de entorno API_REFRESH_TOKEN")

    resp = requests.post(
        "https://portfolio-api-x6xk.onrender.com/api/token/refresh/",
        json={"refresh": refresh_token}
    )
    if resp.status_code != 200:
        raise ValueError("No se pudo obtener token de acceso")

    return resp.json().get("access")


class ProjectsProxyView(View):
    def get(self, request):
        try:
            access = get_access_token()
            headers = {"Authorization": f"Bearer {access}"}
            r = requests.get(
                "https://portfolio-api-x6xk.onrender.com/api/projects/",
                headers=headers
            )
            r.raise_for_status()
            return JsonResponse(r.json(), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class ExperiencesProxyView(View):
    def get(self, request):
        try:
            access = get_access_token()
            headers = {"Authorization": f"Bearer {access}"}
            r = requests.get(
                "https://portfolio-api-x6xk.onrender.com/api/experiences/",
                headers=headers
            )
            r.raise_for_status()
            return JsonResponse(r.json(), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
