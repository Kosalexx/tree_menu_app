from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from core.business_logic.services import get_menu_items
from django import template

if TYPE_CHECKING:
    from django.http import HttpRequest
    from django.template import RequestContext


register = template.Library()

logger = logging.getLogger(__name__)


@register.inclusion_tag("tree_menu_tag_template.html", takes_context=True)
def draw_menu(context: RequestContext, menu_name: str) -> dict:
    """Responsible for displaying the nested menu."""

    menu_items = get_menu_items(menu_name=menu_name)
    request: HttpRequest = context["request"]
    menu_components = request.path.split("/")
    for _ in range(menu_components.count("")):
        menu_components.remove("")
    cont: dict = {"menu": menu_items, "menu_components": menu_components, "menu_name": menu_name, "request": request}
    return cont
