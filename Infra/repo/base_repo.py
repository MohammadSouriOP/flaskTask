from typing import Any, Generic, List, Type, TypeVar

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

    def get_all(self) -> List[E]:
        with self.engine.connect() as conn :
            stmt = select(self.schema.student())
            result = conn.execute(stmt).fetchall()
        if result:
            return [dict(rs._mapping) for rs in result]
        
    def get_by_id(self, id: int) -> E | None:
        if id:
            stmt = select(self.schema.student()).where(self.schema.student().c.id == id)
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

    def delete(self, student_id: int) -> E | None:
        table = self.schema.student()
        result = None
        stmt = (
            delete(table).returning(table.c.student_id, table.c.name)
            .where(table.c.student_id == student_id))
        with self.engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
            conn.commit()
        return result
