from flask import Flask

from Presentaion.student import StudentListAPI


def myApp() -> Flask:
    app = Flask(__name__)
    student_view = StudentListAPI().instance()

    app.add_url_rule('/students/', view_func=student_view, methods=['POST', 'GET'])
    app.add_url_rule(
        '/students/<int:student_id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'], )

    return app


if __name__ == '__main__':
    app = myApp()
    app.run(debug=True)
