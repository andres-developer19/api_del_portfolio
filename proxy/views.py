import os
import requests
from django.http import JsonResponse
from django.views import View

class ProjectsProxyView(View):
    def get(self, request):
        api_url = 'https://portfolio-api-x6xk.onrender.com/api/projects/'

        # Obtiene token de refresh automáticamente
        refresh_token = os.environ.get('API_REFRESH_TOKEN')
        token_resp = requests.post(
            f'https://portfolio-api-x6xk.onrender.com/api/token/refresh/',
            json={"refresh": refresh_token}
        )

        if token_resp.status_code != 200:
            return JsonResponse({"error": "No se pudo obtener token"}, status=500)

        access_token = token_resp.json().get("access")
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(api_url, headers=headers)

        if response.status_code != 200:
            return JsonResponse({"error": "Error al obtener data de la API"}, status=response.status_code)

        return JsonResponse(response.json(), safe=False)


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
