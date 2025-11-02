import os
from pathlib import Path
from datetime import timedelta

# -----------------------------
# BASE DIR
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECRET KEY
# -----------------------------
# 🔒 Nunca pongas la clave en el repo. Usa variables de entorno en Render:
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key')

# -----------------------------
# DEBUG
# -----------------------------
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# -----------------------------
# APPS
# -----------------------------
INSTALLED_APPS = [
    # Django
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

    # Apps propias
    'projects',
    'experience',
    'proxy',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Debe ir arriba
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# ALLOWED HOSTS
# -----------------------------
ALLOWED_HOSTS = [
    'portfolio-api-x6xk.onrender.com',
    'localhost',
    "https://andres-gutierrez.vercel.app",
    "https://andres-developer-s3mh.vercel.app",
    "https://portfolio-api-x6xk.onrender.com/proxy/projects/",
    "https://portfolio-api-x6xk.onrender.com/proxy/experiences/",
    '127.0.0.1',  # si haces peticiones desde tu front
    "http://localhost:3000",                      # si pruebas localmente con React o Next.js
    "http://127.0.0.1:3000",  
    'https://portfolio-api-x6xk.onrender.com/proxy/projects/',
    'https://portfolio-api-x6xk.onrender.com/proxy/experiences/',
]

# -----------------------------
# CORS
# -----------------------------
CORS_ALLOWED_ORIGINS = [
    "https://andres-gutierrez.vercel.app",
    "https://andres-developer-s3mh.vercel.app",
    "https://portfolio-api-x6xk.onrender.com/proxy/projects/",
    "https://portfolio-api-x6xk.onrender.com/proxy/experiences/",
]

# -----------------------------
# REST FRAMEWORK + JWT
# -----------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # JWT obligatorio en todas las rutas
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# -----------------------------
# DATABASE
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Cambiar a MySQL/PostgreSQL si quieres
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
# STATIC
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Carpeta donde collectstatic pone todos los static

# -----------------------------
# MEDIA
# -----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

# -----------------------------
# TEMPLATES (para admin)
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # opcional: rutas a tus carpetas de templates
        'APP_DIRS': True,  # muy importante para admin
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # obligatorio para admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# -----------------------------
# URLS y AUTO FIELD
# -----------------------------
ROOT_URLCONF = 'backend.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
