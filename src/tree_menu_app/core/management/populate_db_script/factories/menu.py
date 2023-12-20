from __future__ import annotations

from typing import TYPE_CHECKING

from core.models import Menu

if TYPE_CHECKING:
    from core.management.populate_db_script.data_access import MenuDAO
    from core.management.populate_db_script.providers import (
        GenerateNextIdProvider,
        RandomTextProvider,
    )


class MenuFactory:
    """Contains methods for generating values for Menu object."""

    def __init__(
        self, random_text_provider: RandomTextProvider, menu_number: GenerateNextIdProvider, menu_dao: MenuDAO
    ):
        self._random_text_provider = random_text_provider
        self._menu_number = menu_number
        self._menu_dao = menu_dao

    def generate(self) -> Menu:
        """Generates random data for TweetDTO"""

        menu_ids = self._menu_dao.get_objects_list()
        return Menu(name=f"Menu_{self._menu_number(values=menu_ids)}", description=self._random_text_provider(20, 50))
