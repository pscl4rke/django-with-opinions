

from django.http import HttpRequest as Req
from django.http import HttpResponse as Rsp
from django.shortcuts import render


def home(req: Req) -> Rsp:
    return render(req, "{{ project_name }}/home.html", {})
