from typing import Any, Dict, Optional, Tuple, Union

from flask import Response, jsonify, request
from flask.views import MethodView

from application.studentService import StudentService
from Domain.student_entity import Student
from Infra.unitOfWork.unitOfWork import UnitOfWork


class StudentListAPI(MethodView):

    def __init__(self) -> None:
        uow = UnitOfWork()
        self.student_service = StudentService(uow)
        super().__init__()

    def instance(self) -> Any:
        student_view = StudentListAPI.as_view('student_api')
        return student_view

    def post(self) -> Any:
        data = request.get_json()
        student = self.student_service.create_student(data)
        return jsonify(student.__dict__), 201

    def get(
        self, student_id: Optional[int] = None
    ) -> Union[Response, Tuple[Response, int]]:
        if student_id is None:
            students = self.student_service.get_students()
            return jsonify([s.__dict__ for s in students])
        else:
            student = self.student_service.get_student_by_id(student_id)
            if student:
                return jsonify(student.__dict__), 200
        return jsonify({'error': 'Student not found'}), 404

    def put(self, student_id: int) -> Union[Any, None, Student,
                                            Tuple[Dict[str, str], int],
                                            Dict[str, Any]]:
        try:
            req: Dict[str, Any] = request.get_json() or {}
            student = self.student_service.update_student(student_id, req)
            if student:
                return jsonify(student.__dict__), 200
            return jsonify({'error': 'Student not found'}), 404
        except (IndexError, KeyError) as e:
            return jsonify({'response': f'Error updating student: {str(e)}'}), 400

    def delete(self, student_id: int) -> Tuple[Dict[str, str], int]:
        try:
            response = self.student_service.delete_student(student_id)
            if response:
                return {'message': 'Student deleted successfully'}, 200
            return {'error': 'Student not found'}, 404
        except IndexError:
            return {'error': f'{student_id} not found'}, 404
