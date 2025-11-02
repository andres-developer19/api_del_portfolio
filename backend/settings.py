import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# ARCHIVOS MEDIA (imagenes)
# -----------------------------
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# -----------------------------
# CONFIGURACIÓN GENERAL
# ----------------------------- 
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key') # 🔒 Ocúltala en Render como variable de entorno
DEBUG = False

ALLOWED_HOSTS = [
    'portfolio-api-x6xk.onrender.com',
    'https://andres-developer-s3mh.vercel.app', 
    'localhost',
    '127.0.0.1'
]

# -----------------------------
# APLICACIONES INSTALADAS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',

    # Tus apps
    'projects',
    'experience',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# CORS (solo permite tu sitio)
# -----------------------------
CORS_ALLOWED_ORIGINS = [
    "https://andres-gutierrez.vercel.app",
    "https://andres-developer-s3mh.vercel.app"
]

# Si quieres aceptar peticiones desde el admin de Django en desarrollo:
# CORS_ALLOW_ALL_ORIGINS = DEBUG

# -----------------------------
# CONFIGURACIÓN REST FRAMEWORK
# -----------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# -----------------------------
# BASE DE DATOS
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # ⚙️ Si usas MySQL cámbialo aquí
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# VALIDACIÓN DE CONTRASEÑAS
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# INTERNACIONALIZACIÓN
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# ARCHIVOS ESTÁTICOS
# -----------------------------
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#SECRET_KEY = 'django-insecure-6f@r1du-shmdd2adltr1-3-9g^u@q+o_6lo$1-08(l(aqq$9#j'