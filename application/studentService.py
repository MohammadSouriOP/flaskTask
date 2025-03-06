from datetime import datetime

from application.baseService import BaseService
from Domain.student_entity import Student
from Infra.repo.student_repo import StudentRepo


class StudentService(BaseService):
    def __init__(self, uow):
        self.uow = uow
        self.student_repo = StudentRepo()
        super().__init__(uow)

    def get_students(self):
        return self.student_repo.get_all()

    def get_student_by_id(self, student_id: int):
        return self.student_repo.get_by_id(student_id)

    def create_student(self, data):
        student = Student(
            id=data['id'],
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
            created_at=datetime.now(),
        )
        with self.uow:
            self.student_repo.create(student)
            self.uow.commit()
        return student

    def update_student(self, id, req):
        with self.uow:
            student = self.student_repo.update(id, req)
            self.uow.commit()
        return student

    def delete_student(self, id):
        with self.uow:
            result = self.student_repo.delete(id)
            self.uow.commit()
        return result
