from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.management.populate_db_script.data_access import BaseDAO
    from core.management.populate_db_script.factories.interfaces import (
        FakeFactoryProtocol,
    )


logger = logging.getLogger(__name__)


class PopulateTable:
    """Contains methods and logic for writing data to the database."""

    def __init__(self, records_number: int, dao: BaseDAO, fake_factory: FakeFactoryProtocol) -> None:
        self._records_number = records_number
        self._dao = dao
        self._fake_factory = fake_factory

    def execute(self) -> None:
        """Executes a data recording into the database.

        In this case, the method of entering each record with a separate database query instead of bulk_create is
        specifically used because it is necessary to dynamically retrieve object ids from the database when new
        records are generated."""

        records_num = 0
        for _ in range(self._records_number):
            new_record = self._fake_factory.generate()
            rec = self._dao.create_record([new_record])
            if rec > 0:
                records_num += 1
        logger.info(
            f"Successfully added {records_num} records from {self._records_number}. "
            f"DAO: {self._dao.__module__}; FACTORY: {self._fake_factory.__module__}."
        )
