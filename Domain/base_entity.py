from typing import Dict


class BaseEntity:
    def __init__(self, id: int, name: str, age: int, grade: str) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self) -> Dict[str, int | str]:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade
        }
