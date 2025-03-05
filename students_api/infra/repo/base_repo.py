from typing import Any, Dict, Generic, Type, TypeVar

from sqlalchemy import delete, insert, select, update

from students_api.domain.entities.base_entity import BaseEntity
from students_api.infra.db.connection import Connection

E = TypeVar('E', bound='BaseEntity')
mydatabase: Dict[str, dict[int, E]] = {}  # type: ignore


class BaseRepo(Generic[E]):
    def __init__(self, entity_name: str, entity: Type[E]) -> None:
        self.entity = entity
        self.db_connection = Connection()
        self.entity_name = entity_name

        self.engine = self.db_connection.engine
        self.metadata = self.db_connection.metadata
        self.schema = self.db_connection.schema
        self.student_schema = self.schema.student()

    def insert(self, entity: E) -> E:
        stmt = insert(self.schema.student()).values(**entity.__dict__)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()

        return entity

    def get_all(self):
        with self.engine.connect() as conn:
            stmt = select(self.schema.student())
            result = conn.execute(stmt).fetchall()
        if result:
            return [dict(rs._mapping) for rs in result]

    def get(self, user_id: int):
        if user_id:
            stmt = select(self.schema.student()).where(self.schema.student().c.id == user_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchone()
        if result:
            return result._mapping
        return None

    def update(self, id: int, data: dict[str, Any]) -> E | None:
        table = self.schema.student()
        stmt = (
            update(table).returning(table.c.id, table.c.name)
            .where(table.c.id == id)
            .values(**data)
        )
        result = None
        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
            conn.commit()
        return result

    def delete(self, id: int) -> E | None:
        table = self.schema.student()
        result = None
        stmt = (
            delete(table).returning(table.c.id, table.c.name)
            .where(table.c.id == id))
        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
            conn.commit()
        return result
