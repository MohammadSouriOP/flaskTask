from flask import Flask

from src.presentaion.student import StudentView


def register_routes(app: Flask) -> None:

    student_view = StudentView.as_view('student_view')

    app.add_url_rule('/students', view_func=student_view, methods=['GET', 'POST'])
    app.add_url_rule('/students/<int:id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])
