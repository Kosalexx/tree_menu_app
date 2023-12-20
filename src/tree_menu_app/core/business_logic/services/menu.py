from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Menu, MenuItem

if TYPE_CHECKING:
    from django.db.models import QuerySet


def get_main_menu() -> QuerySet:
    """Gets menu info from DB."""

    menu = Menu.objects.all()
    return menu


def get_submenu(menu_name: str) -> QuerySet:
    """Gets menu items from DB."""

    menu_items: QuerySet = MenuItem.objects.select_related("menu", "parent", "parent__parent").filter(
        menu__name=menu_name
    )
    return menu_items


def get_menu_items(menu_name: str) -> dict[str, None | MenuItem | list]:
    """Gets submenu info from DB."""

    menu_items = get_submenu(menu_name=menu_name)
    trees: dict[str, dict] = {"root": {"parent": None, "item": None, "sub": []}}

    for item in menu_items:
        parent_item = item.parent if item.parent is not None else "root"
        trees.setdefault(parent_item, {"sub": []})
        trees.setdefault(item, {"sub": []})
        trees[item]["parent"] = item.parent
        trees[item]["item"] = item
        trees[parent_item]["sub"].append(trees[item])

    result: dict[str, None | MenuItem | list] = trees["root"]
    return result


def get_item_info(menu_name: str | None = None, menu_item: str | None = None) -> QuerySet:
    """Gets info about Menu object or MenuItem object for page body."""

    result = {"menu": None, "submenu": None}
    if menu_name:
        result["menu"] = Menu.objects.get(name=menu_name)

    else:
        result["submenu"] = MenuItem.objects.select_related("menu", "parent", "parent__parent").get(name=menu_item)
    return result
