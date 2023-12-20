from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MenuItem:
    name: str
    url: str
    children: list["MenuItem" | None]
