from __future__ import annotations

from typing import TYPE_CHECKING

from core.business_logic.services import get_item_info, get_main_menu
from core.utils import query_debugger
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@query_debugger
@require_http_methods(request_method_list=["GET"])
def index_controller(request: HttpRequest) -> HttpResponse:
    """Index page controller"""

    if request.method == "GET":
        context = {"menus": get_main_menu()}
        return render(request, "menu_in_db.html", context)
    return HttpResponseBadRequest("Incorrect HTTP method.")


@query_debugger
@require_http_methods(request_method_list=["GET"])
def tree_menu(request: HttpRequest, url: str) -> HttpResponse:
    """Controller for drawing three menu."""

    if request.method == "GET":
        splitted_url = url.split("/")
        for _ in range(splitted_url.count("")):
            splitted_url.remove("")
        current_menu_name = splitted_url[0]
        current_item = splitted_url[-1]
        if current_menu_name == current_item:
            page_body_info = get_item_info(menu_name=current_item)
        else:
            page_body_info = get_item_info(menu_item=current_item)
        context = {"current_url": url, "current_menu_name": current_menu_name, "page_body_info": page_body_info}
        return render(request=request, template_name="menu_drawing.html", context=context)
    return HttpResponseBadRequest("Incorrect HTTP method.")
