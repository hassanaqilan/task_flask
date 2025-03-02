from students_api.domain.entities.student import Student
from students_api.infra.repo.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        entity_name = 'students'
        super().__init__(entity_name=entity_name, entity=Student)
