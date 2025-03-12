from dataclasses import dataclass
from typing import Any

from src.domain.base_entity import BaseEntity


@dataclass
class Student(BaseEntity):
    name: str
    age: int
    grade: int

    def update(self, data: Any) -> 'Student':
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self
