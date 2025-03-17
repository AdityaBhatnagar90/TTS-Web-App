import os
import django
from fastapi.middleware.wsgi import WSGIMiddleware
from django.core.asgi import get_asgi_application
from fastapi_app import fastapi_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tts_project.settings')
django.setup()

django_asgi_app = get_asgi_application()

# Mount FastAPI inside Django’s ASGI
from starlette.middleware.wsgi import WSGIMiddleware
fastapi_app.mount("/api", WSGIMiddleware(django_asgi_app))

application = fastapi_app
