from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from .base import BaseDAO

logger = getLogger(__name__)

if TYPE_CHECKING:
    from core.models import MenuItem


class MenuItemDAO(BaseDAO):
    def get_objects_list(self) -> list[MenuItem]:
        """Gets ids from PostgreSQL table."""

        ids_list: list[MenuItem] = list(self._db_model.objects.select_related("menu", "parent").all())
        return ids_list
