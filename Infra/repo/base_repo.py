from typing import Any, Dict, Generic, List, Type, TypeVar

from sqlalchemy import delete, insert, select, update

from Domain.base_entity import BaseEntity
from Infra.database.connection import Connection

E = TypeVar('E', bound='BaseEntity')


class BaseRepo(Generic[E]):

    def __init__(self, entity_name: str, entity: Type[E]) -> None:
        self.entity = entity
        self.db_connection = Connection()
        self.entity_name = entity_name
        self.engine = self.db_connection.engine
        self.metadata = self.db_connection.metadata
        self.schema = self.db_connection.schema
        self.student_schema = self.schema.student()

    def create(self, entity: E) -> E:
        stmt = insert(self.schema.student()).values(**entity.__dict__)
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            return entity

    def get_all(self) -> List[E]:
        with self.engine.connect() as conn:
            stmt = select(self.schema.student())
            result = conn.execute(stmt).fetchall()

        return [self.entity(**dict(rs._mapping)) for rs in result] if result else []

    def get_by_id(self, id: int) -> E | None:
        stmt = select(self.schema.student()).where(self.schema.student().c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchone()

        return self.entity(**dict(result._mapping)) if result else None

    def update(self, id: int, data: dict[str, Any]) -> Dict[str, Any] | None:
        table = self.schema.student()
        stmt = (
            update(table)
            .where(table.c.id == id)
            .values(**data)
            .returning(table)
        )

        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchone()
            conn.commit()

        return dict(result._mapping) if result else None

    def delete(self, student_id: int) -> Dict[str, Any] | None:
        table = self.schema.student()
        stmt = (
            delete(table)
            .where(table.c.student_id == student_id)
            .returning(table)  # Return full deleted row
        )

        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchone()
            conn.commit()

        return dict(result._mapping) if result else None
