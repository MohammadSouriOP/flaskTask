from datetime import datetime
from typing import Any, Dict, Optional, Tuple, Union

from flask import Response, jsonify, request
from flask.views import MethodView

from Domain.student_entity import Student
from Infra.student_repo import StudentRepo


class StudentListAPI(MethodView):

    def instance(self) -> Any:
        student_view = StudentListAPI.as_view('student_api')
        return student_view

    def get(self, student_id: Optional[int] = None) -> Union[Response, Tuple[Response, int]]:

        studentRepo = StudentRepo()
        if student_id is None:
            students = studentRepo.get_all()
            return jsonify([student.to_dict() for student in students])
        else:
            student = studentRepo.get(student_id)
            if student:
                return jsonify(student.__dict__)
        return jsonify('Student Not Found')

    def post(self) -> Any:

        data = request.get_json()
        student = Student(
            student_id=data['student_id'],
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
            created_at=datetime.now(),
        )
        studentRepo = StudentRepo()
        studentRepo.insert(student)
        return jsonify(student), 201

    def put(self, student_id: int) -> Union[Any, None, Student, Tuple[Dict[str, str], int], Dict[str, Any]]:
        try:
            req = request.json
            studentRepo = StudentRepo()
            student = studentRepo.get(student_id)

            if not isinstance(student, Student):
                return {'response': 'Student not found'}, 404
            student.update(req)
            return student.__dict__
        except (IndexError, KeyError) as e:
            return {'response': f'Error updating student: {str(e)}'}, 400

    def delete(self, student_id: int) -> Tuple[Dict[str, str], int]:
        try:
            studentRepo = StudentRepo()
            studentRepo.delete(student_id)
            return {'response': f'{student_id} has been removed'}, 200
        except IndexError:
            return {'response': f'{student_id} not found'}, 404
