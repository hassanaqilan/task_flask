from typing import Any, Dict, Generic, Type, TypeVar

from students_api.domain.entities.base_entity import BaseEntity

E = TypeVar('E', bound='BaseEntity')


mydatabase: Dict[str, dict[int, E]] = {}  # type: ignore


class BaseRepo(Generic[E]):
    def __init__(self, entity_name: str, entity: Type[E]) -> None:
        self.entity = entity
        self.entity_name = entity_name

    def insert(self, entity: E) -> E:
        if self.entity_name not in mydatabase:
            mydatabase[self.entity_name] = {}
        mydatabase[self.entity_name][entity.id] = entity
        return entity

    def get_all(self) -> list[E]:
        return list(mydatabase[self.entity_name].values())

    def get(self, id: int) -> E | None:
        if self.entity_name not in mydatabase:
            return None
        if id not in mydatabase[self.entity_name]:
            return None
        return mydatabase[self.entity_name].get(id)

    def update(self, id: int, data: dict[str, Any]) -> E | None:
        entity = mydatabase[self.entity_name].get(id)
        if entity:
            entity.update(data)
            return entity
        return None

    def delete(self, id: int) -> E | None:
        if id in mydatabase[self.entity_name]:
            return mydatabase[self.entity_name].pop(id)
        else:
            return None
