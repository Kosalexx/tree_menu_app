from core.management.populate_db_script.data_access import MenuDAO, MenuItemDAO
from core.management.populate_db_script.factories import MenuFactory, MenuItemFactory
from core.management.populate_db_script.populate_table_command import PopulateTable
from core.management.populate_db_script.providers import (
    GenerateNextIdProvider,
    RandomObjectFromListOrNoneProvider,
    RandomObjectFromListProvider,
    RandomTextProvider,
)
from core.models import Menu, MenuItem


def populate_menu_table(num: int) -> None:
    """Populates menu table with random data."""

    menu_dao = MenuDAO(db_model=Menu)
    menu_factory = MenuFactory(
        random_text_provider=RandomTextProvider(), menu_number=GenerateNextIdProvider(), menu_dao=menu_dao
    )
    PopulateTable(records_number=num, dao=menu_dao, fake_factory=menu_factory).execute()


def populate_menu_items_table(num: int) -> None:
    """Populates menu table with random data."""

    menu_item_dao = MenuItemDAO(db_model=MenuItem)
    menu_dao = MenuDAO(db_model=Menu)
    menu_item_factory = MenuItemFactory(
        random_text_provider=RandomTextProvider(),
        random_menu_provider=RandomObjectFromListProvider(),
        random_parent_provider=RandomObjectFromListOrNoneProvider(),
        menu_item_dao=menu_item_dao,
        menu_dao=menu_dao,
    )
    PopulateTable(records_number=num, dao=menu_item_dao, fake_factory=menu_item_factory).execute()


def populate_db(num: int, tables: list[str]) -> None:
    """Populates database with random data."""

    if "menu" in tables:
        populate_menu_table(num=num)
    if "menu_items" in tables:
        populate_menu_items_table(num=num)
