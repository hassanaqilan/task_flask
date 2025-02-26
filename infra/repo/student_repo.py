from domain.entities.student import Student
from infra.repo.base_repo import BaseRepo


class StudentRepo(BaseRepo[Student]):
    def __init__(self) -> None:
        entity_name = "students"
        super().__init__(entitty_name=entity_name, entity=Student)
