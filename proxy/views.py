import os
import requests
from django.http import JsonResponse
from django.views import View

# Función para obtener un access token válido usando el refresh token
def get_access_token():
    refresh_token = os.environ.get("API_REFRESH_TOKEN")
    if not refresh_token:
        raise Exception("No se encontró la variable de entorno API_REFRESH_TOKEN")

    resp = requests.post(
        "https://portfolio-api-x6xk.onrender.com/api/token/refresh/",
        json={"refresh": refresh_token}
    )

    if resp.status_code != 200:
        raise Exception("No se pudo refrescar el token: " + resp.text)

    return resp.json()["access"]


# Proxy para Projects
class ProjectsProxyView(View):
    def get(self, request):
        try:
            access = get_access_token()
            headers = {"Authorization": f"Bearer {access}"}
            r = requests.get(
                "https://portfolio-api-x6xk.onrender.com/api/projects/",
                headers=headers
            )
            r.raise_for_status()  # lanza error si el status no es 200
            return JsonResponse(r.json(), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


# Proxy para Experiences
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
