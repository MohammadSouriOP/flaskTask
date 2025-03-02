from typing import Dict, List, Optional

from base_entity import BaseEntity


class BaseRepo:
    def __init__(self) -> None:
        self.students: Dict[int, BaseEntity] = {}
        self.next_id: int = 1

    def create(self, name: str, age: int, grade: str) -> BaseEntity:

        student = BaseEntity(self.next_id, name, age, grade)
        self.students[self.next_id] = student
        self.next_id += 1
        return student

    def get_all(self) -> List[BaseEntity]:

        return list(self.students.values())

    def get_by_id(self, student_id: int) -> Optional[BaseEntity]:

        return self.students.get(student_id)

    def update(self, student_id: int,
               name: Optional[str], age: Optional[int], grade: Optional[str]) -> Optional[BaseEntity]:

        student = self.get_by_id(student_id)
        if student:
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            return student
        return None

    def delete(self, student_id: int) -> bool:

        student = self.get_by_id(student_id)
        if student:
            del self.students[student_id]
            return True
        return False
