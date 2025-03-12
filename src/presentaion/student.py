from typing import Any, Dict, Optional

from flask import Response, abort, jsonify, request
from flask.views import MethodView

from src.application.student_service import StudentServices
from src.domain.student_entity import Student
from src.infra.repo.student_repo import StudentRepo


class StudentView(MethodView):
    def __init__(self) -> None:
        self.student_repo = StudentRepo()
        self.service = StudentServices(self.student_repo)

    def get(self, id: Optional[int] = None) -> Response | None:
        if id is None:
            all_students: list[Dict[str, Any]] = self.service. get_all(self.student_repo)
            return jsonify(all_students)
        else:
            student: Dict[str, Any] | None = self.service.get_by_id(int(id), self.student_repo)
            if student is None:
                abort(404, description='Student not found')
                return None
            return jsonify(student)

    def post(self) -> Response | None:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid data")

        entity = Student(
            id=None,
            name=data.get('name'),
            age=data.get('age'),
            grade=data.get('grade')
        )
        if not all([entity.name, entity.age]):
            abort(400, description='Required fields missing')
            return None

        result = self.service.add(entity, self.student_repo)
        if result:
            return jsonify(vars(result))
        abort(500, description='Error adding student')

    def put(self, id: int) -> Response | None:
        data = request.get_json()
        if not data:
            abort(400, description="Invalid JSON data")
            return None

        entity = Student(
            id=None,
            name=data.get('name'),
            age=data.get('age'),
            grade=data.get('grade')
        )

        result = self.service.update(id, entity, self.student_repo)
        if not result:
            abort(404, description='Student not found')
            return None
        return jsonify(message='Student updated successfully')

    def delete(self, id: int) -> Response | None:
        result = self.service.delete(id, self.student_repo)
        if not result:
            abort(404, description='Student not found')
            return None

        return jsonify(message='Student deleted successfully')
