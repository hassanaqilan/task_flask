from dataclasses import dataclass

from domain.entities.base_entity import BaseEntity


@dataclass
class Student(BaseEntity):
    name: str
    age: int
    grade: int
