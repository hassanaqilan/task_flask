from typing import Any, Generic, Type, TypeVar, Union

from students_api.domain.entities.base_entity import BaseEntity

E = TypeVar('E', bound='BaseEntity')


mydatabase = {}  # type: ignore


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

    def get(self, id: int) -> Union[E, tuple[str, int], Any]:
        if self.entity_name not in mydatabase:
            return 'database is empty', 400
        if id not in mydatabase[self.entity_name]:
            return 'not found', 404
        return mydatabase[self.entity_name].get(id)

    def update(self, id: int, data: dict[str, Any]) -> bool:
        entity = mydatabase[self.entity_name].get(id)
        if entity:
            entity.update(data)
            return True
        return False

    def delete(self, id: int) -> None:
        if id in mydatabase[self.entity_name]:
            mydatabase[self.entity_name].pop(id)
        else:
            # Optionally handle the case where the ID does not exist
            print(f'Entity with id {id} not found.')
        return None
