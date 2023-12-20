from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Type

logger = getLogger(__name__)

if TYPE_CHECKING:
    from django.db.models import Model


class BaseDAO:
    """Base Data access object."""

    def __init__(self, db_model: Type[Model]) -> None:
        self._db_model = db_model

    def create_record(self, data: list) -> int:
        """Executes data writing to a PostgreSQL table of passed model."""

        records_before = self._db_model.objects.count()
        self._db_model.objects.bulk_create(data, ignore_conflicts=True)
        records_after = self._db_model.objects.count()
        num: int = records_after - records_before
        return num
