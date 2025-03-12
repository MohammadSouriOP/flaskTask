from .base_repo import BaseRepo
from src.domain.student_entity import Student
from src.infra.database.schema import students


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(Student, students)
