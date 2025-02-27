from datetime import date

from domain.entities.base_entity import BaseEntity


class Student(BaseEntity):
    def __init__(self, id: int, name: str, age: int, grade: int):
        super().__init__(id, date.today())
        self.name = name
        self.age = age
        self.grade = grade
