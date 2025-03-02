from students_api.domain.entities.student import Student
from students_api.infra.repo.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        super().__init__(entity_name='students', entity=Student)
