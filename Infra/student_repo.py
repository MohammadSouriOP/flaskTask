from Domain.student_entity import Student
from Infra.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        entity_name = 'students'
        super().__init__(entity_name=entity_name, entity=Student)
