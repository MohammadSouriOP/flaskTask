from typing import Any

from flask import jsonify, request
from flask.views import MethodView

from Infra.base_repo import BaseRepo

repo = BaseRepo()


class StudentListAPI(MethodView):
    def get(self) -> Any:

        students = repo.get_all()
        return jsonify([student.to_dict() for student in students])

    def post(self) -> Any:

        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        grade = data.get('grade')

        if not name or not age or not grade:
            return jsonify({'error': 'Missing required fields: name, age, or grade'}), 400

        student = repo.create(name, age, grade)
        return jsonify(student.to_dict()), 201


class StudentAPI(MethodView):
    def get(self, student_id: int) -> Any:

        student = repo.get_by_id(student_id)
        if student:
            return jsonify(student.to_dict())
        return jsonify({'error': 'Student not found'}), 404

    def put(self, student_id: int) -> Any:

        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        grade = data.get('grade')

        student = repo.update(student_id, name, age, grade)
        if student:
            return jsonify(student.to_dict())
        return jsonify({'error': 'Student not found'}), 404

    def delete(self, student_id: int) -> Any:

        if repo.delete(student_id):
            return jsonify({'message': 'Student deleted successfully'}), 200
        return jsonify({'error': 'Student not found'}), 404
