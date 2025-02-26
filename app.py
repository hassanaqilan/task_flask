from flask import Flask
from presentation.routes import StudentAPI


def create_app():
    app = Flask(__name__)
    studentapi = StudentAPI()

    student_view = studentapi.instance()
    app.add_url_rule('/students/', view_func=student_view,
                     methods=['POST', 'GET'])
    app.add_url_rule('/students/<int:student_id>', view_func=student_view,
                     methods=['GET', 'PUT', 'DELETE'])

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
