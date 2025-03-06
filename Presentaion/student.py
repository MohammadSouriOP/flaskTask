from typing import Any, Dict, Optional, Tuple, Union

from flask import Response, jsonify, request
from flask.views import MethodView

from application.studentService import StudentService
from Domain.student_entity import Student
from Infra.unitOfWork.unitOfWork import UnitOfWork


class StudentListAPI(MethodView):

    def __init__(self):
        uow = UnitOfWork()
        self.student_service = StudentService(uow)
        super().__init__()

    def instance(self) -> Any:
        student_view = StudentListAPI.as_view('student_api')
        return student_view

    def post(self) -> Any:
        data = request.get_json()
        student = self.student_service.create_student(data)
        return jsonify(student), 201

    def get(
        self, student_id: Optional[int] = None
    ) -> Union[Response, Tuple[Response, int]]:
        if student_id is None:
            students = self.student_service.get_students()
            return jsonify(students)
        else:
            student = self.student_service.get_student_by_id(student_id)
            if student:
                return dict(student)
        return jsonify({'error': 'Student not found'}), 404

    def put(self, student_id: int) -> Union[Any, None, Student,
                                            Tuple[Dict[str, str], int],
                                            Dict[str, Any]]:
        try:
            req = request.json
            student = self.student_service.update_student(student_id, req)
            return dict(student)
        except (IndexError, KeyError) as e:
            return {'response': f'Error updating student: {str(e)}'}, 400

    def delete(self, student_id: int) -> Tuple[Dict[str, str], int]:
        try:
            response = self.student_service.delete_student(student_id)
            return dict(response)
        except IndexError:
            return {'response': f'{student_id} not found'}, 404
