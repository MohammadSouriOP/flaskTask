from flask import Flask

from student import StudentAPI, StudentListAPI

app = Flask(__name__)


app.add_url_rule('/students', view_func=StudentListAPI.as_view('students'))
app.add_url_rule('/students/<int:student_id>', view_func=StudentAPI.as_view('student'))

if __name__ == '__main__':
    app.run(debug=True)
