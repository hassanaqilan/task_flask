from typing import Any, Generic, Type, TypeVar

from domain.entities.base_entity import BaseEntity

E = TypeVar('E', bound='BaseEntity')


mydatabase = {}


class BaseRepo(Generic[E]):
    def __init__(self, entitty_name: str, entity: Type[E]) -> None:
        self.entity = entity
        self.entitty_name = entitty_name

    def insert(self, entity: E) -> E:
        if self.entitty_name not in mydatabase:
            mydatabase[self.entitty_name] = {}
        mydatabase[self.entitty_name][entity.id] = entity
        return entity

    def get_all(self) -> list[E]:
        return list(mydatabase[self.entitty_name].values())

    def get(self, id: int) -> E:
        return mydatabase[self.entitty_name].get(id)

    def update(self, id: int, data: dict[str, Any]) -> bool:
        entity = mydatabase[self.entitty_name].get(id)
        if entity:
            entity.update(data)
            return True
        return False

    def delete(self, id: int) -> None:
        mydatabase[self.entitty_name].pop(id)
        return None
