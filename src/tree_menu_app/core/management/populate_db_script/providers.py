from random import choice, randint
from string import ascii_letters, digits
from typing import Optional

from django.db.models import QuerySet

SYMBOLS = ascii_letters + digits


class GenerateNextIdProvider:
    """Provider that generates random number."""

    def __call__(self, values: list[QuerySet]) -> int:
        return len(values) + 1


class RandomTextProvider:
    """Provider that generates random text from ASCII letters and digits."""

    def __call__(self, min_length: int = 10, max_length: int = 30) -> str:
        random_text: str = ""
        for _ in range(randint(min_length, max_length)):
            random_text += choice(SYMBOLS)
        return random_text.capitalize()


class RandomObjectFromListProvider:
    """Provider that selects random object from list."""

    def __call__(self, values: list[QuerySet]) -> QuerySet:
        random_obj = choice(values)
        return random_obj


class RandomObjectFromListOrNoneProvider:
    """Provider that selects a random object from the list."""

    def __call__(self, values: list[QuerySet]) -> Optional[QuerySet]:
        if len(values) == 0:
            return None
        else:
            random_value = choice(values)
            final_result: Optional[object] = choice([random_value, None])
            return final_result
