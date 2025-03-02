from typing import Any, Dict, Generic, List, Type, TypeVar

from Domain.base_entity import BaseEntity

E = TypeVar('E', bound='BaseEntity')

student: Dict[str, dict[int, E]] = {}


class BaseRepo(Generic[E]):

    def __init__(self, entity_name: str, entity: Type[E]) -> None:
        self.entity = entity
        self.entity_name = entity_name

    def create(self, entity: E) -> E:
        if self.entity_name not in student:
            student[self.entity_name] = {}
        student[self.entity_name][entity.id] = entity
        return entity

    def get_all(self) -> List[E]:

        return list(student[self.entity_name].values())

    def get_by_id(self, student_id: int) -> E | None:
        if self.entity_name not in student:
            return None
        if student_id not in student[self.entity_name]:
            return None
        return student[self.entity_name].get(student_id)

    def update(self, student_id: int, data: dict[str, Any]) -> E | None:
        entity = student[self.entity_name].get(student_id)
        if entity:
            entity.update(data)
            return entity
        return None

    def delete(self, student_id: int) -> E | None:

        if student_id in student[self.entity_name]:
            return student[self.entity_name].pop(student_id)
        else:
            return None
