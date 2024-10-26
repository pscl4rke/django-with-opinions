

import logging
LOG = logging.getLogger(__name__)

from django.http import HttpRequest as Req
from django.http import HttpResponse as Rsp
from django.shortcuts import render


def error_404(req: Req, exception: Exception) -> Rsp:
    return render(req, "{{ project_name }}/error.html", {
        "status_code": "404",
        "status_message": "Not Found",
    }, status=404)


def error_500(req: Req) -> Rsp:
    return render(req, "{{ project_name }}/error.html", {
        "status_code": "500",
        "status_message": "Internal Server Error",
    }, status=500)


def home(req: Req) -> Rsp:
    LOG.info("Home page requested")
    return render(req, "{{ project_name }}/home.html", {})
