from dataclasses import dataclass
from datetime import datetime
from typing import Any
from typing import Optional


@dataclass
class BaseEntity:
    id: Optional[int]
    # created_at: datetime

    def update(self, data: dict[str, Any]) -> 'BaseEntity':
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self
