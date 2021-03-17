import os
import sys
from typing import List, Tuple

from django.conf import settings
from django.conf.urls import url
from django.core.handlers.wsgi import WSGIHandler, WSGIRequest
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse

DEBUG: bool = os.environ.get("DEBUG", "on") == "on"

SECRET_KEY: str = os.environ.get("SECRET_KEY", os.urandom(32))

ALLOWED_HOSTS: List[str] = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ),
)


def index(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("Hello World")


urlpatterns: Tuple = (url(r"^$", index),)


application: WSGIHandler = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
