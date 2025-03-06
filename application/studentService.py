from datetime import datetime
from typing import Any, Dict, List, Optional

from application.baseService import BaseService
from Domain.student_entity import Student
from Infra.repo.student_repo import StudentRepo
from Infra.unitOfWork.unitOfWork import UnitOfWork


class StudentService(BaseService):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)
        self.student_repo = StudentRepo()

    def get_students(self) -> List[Student]:
        return self.student_repo.get_all()

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        return self.student_repo.get_by_id(student_id)

    def create_student(self, data: Dict[str, Any]) -> Student:
        student = Student(
            id=data["id"],
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            created_at=datetime.now(),
        )
        with self.uow:
            self.student_repo.create(student)
            self.uow.commit()
        return student

    def update_student(self, id: int, req: Dict[str, Any]) -> Optional[Student]:
        with self.uow:
            student_data = self.student_repo.update(id, req)
            self.uow.commit()
        return Student(**student_data) if student_data else None

    def delete_student(self, id: int) -> Optional[Student]:
        with self.uow:
            student_data = self.student_repo.delete(id)
            self.uow.commit()
        return Student(**student_data) if student_data else None
