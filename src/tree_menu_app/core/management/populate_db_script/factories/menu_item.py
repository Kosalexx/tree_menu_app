from __future__ import annotations

from typing import TYPE_CHECKING

from core.management.populate_db_script.exceptions import EmptyDBException
from core.models import MenuItem

if TYPE_CHECKING:
    from core.management.populate_db_script.data_access import MenuDAO, MenuItemDAO
    from core.management.populate_db_script.providers import (
        RandomObjectFromListOrNoneProvider,
        RandomObjectFromListProvider,
        RandomTextProvider,
    )


class MenuItemFactory:
    """Contains methods for generating values for Menu object."""

    def __init__(
        self,
        random_text_provider: RandomTextProvider,
        random_menu_provider: RandomObjectFromListProvider,
        random_parent_provider: RandomObjectFromListOrNoneProvider,
        menu_dao: MenuDAO,
        menu_item_dao: MenuItemDAO,
    ):
        self._random_text_provider = random_text_provider
        self._random_menu_provider = random_menu_provider
        self._random_parent_provider = random_parent_provider
        self._menu_dao = menu_dao
        self._menu_item_dao = menu_item_dao

    def generate(self) -> MenuItem:
        """Generates random data for TweetDTO"""
        menu_list = self._menu_dao.get_objects_list()
        if menu_list == []:
            raise EmptyDBException("We can't generate new records because menu table is empty.")
        menu_items_list = self._menu_item_dao.get_objects_list()
        menu = self._random_menu_provider(values=menu_list)
        parent = self._random_parent_provider(menu_items_list)
        if parent:
            menu = parent.menu
        menu_item = MenuItem(
            name=f"Submenu_{self._random_text_provider(6, 15)}",
            description=self._random_text_provider(20, 50),
            menu=menu,
            parent=parent,
        )
        menu_item.url = menu_item.create_url()
        return menu_item
