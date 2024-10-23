

from typing import Any

import logging
LOG = logging.getLogger(__name__)

from django.templatetags.static import static
from django.urls import reverse
from django.contrib.messages import get_messages

from jinja2 import Environment


def environment(**options: Any) -> Environment:
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
        'get_messages': get_messages,
    })
    return env
