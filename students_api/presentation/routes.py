from datetime import datetime
from typing import Any, Dict, Optional, Tuple, Union

from domain.entities.student import Student
from flask import Response, jsonify, request
from flask.views import MethodView
from infra.repo.student_repo import StudentRepo


class StudentAPI(MethodView):

    def __init__(self) -> None:
        super().__init__()

    def instance(self) -> Any:
        student_view = StudentAPI.as_view('student_api')
        return student_view

    def post(self) -> Any:
        data = request.get_json()
        student = Student(
            id=data['id'],
            name=data['name'],
            age=data['age'],
            grade=data['grade'],
            created_at=datetime.now(),
        )
        student_repo = StudentRepo()
        student_repo.insert(student)
        return jsonify(student), 201

    def get(
        self, student_id: Optional[int] = None
    ) -> Union[Response, Tuple[Response, int]]:
        student_repo = StudentRepo()
        if student_id is None:
            students = student_repo.get_all()
            return jsonify({'students':
                            [student.__dict__ for student in students]})
        else:
            student = student_repo.get(student_id)
            if student:
                return jsonify(student.__dict__)

        return jsonify({'error': 'Student not found'}), 404

    def put(self, student_id: int) -> Union[Dict[str, Any],
                                            Tuple[Dict[str, str], int]]:
        try:
            req = request.json
            student_repo = StudentRepo()
            student = student_repo.get(student_id)
            student.update(req)
            return student.__dict__  # type: ignore
        except (IndexError, KeyError) as e:
            return {'response': f'Error updating student: {str(e)}'}, 400

    def delete(self, student_id: int) -> Tuple[Dict[str, str], int]:
        try:
            student_repo = StudentRepo()
            student_repo.delete(student_id)
            return {'response': f'{student_id} has been removed'}, 200
        except IndexError:
            return {'response': f'{student_id} not found'}, 404
