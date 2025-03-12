from typing import Any, TypeVar

from psycopg2 import OperationalError

from src.domain.base_entity import BaseEntity
from src.infra.repo.base_repo import BaseRepo
from src.infra.unitOfWork.unit_of_work import UnitOfWork

E = TypeVar('E', bound=BaseEntity)
T = TypeVar('T', bound=BaseRepo[Any])


class BaseService:

    def add(self, entity: E, repo: T) -> E | None:
        try:
            with UnitOfWork(repo) as uow:
                result = uow.repo.insert(entity, uow.session)
                return result
        except OperationalError as e:
            raise e

    def get_all(self, repo: T) -> list[E]:
        try:
            with UnitOfWork(repo) as uow:
                students = uow.repo.get_all(uow.session)
            return students
        except OperationalError as e:
            raise e

    def get_by_id(self, id: int, repo: T) -> E | None:
        try:
            with UnitOfWork(repo) as uow:
                student_entity = uow.repo.get(id, uow.session)
            return student_entity
        except OperationalError as e:
            raise e

    def update(self, id: int, entity: E, repo: T) -> bool:
        try:
            with UnitOfWork(repo) as uow:
                subject = uow.repo.get(id, uow.session)
                if subject is None:
                    return False
                else:
                    subject = entity
                uow.repo.update(subject, id, uow.session)
            return True
        except OperationalError as e:
            raise e

    def delete(self, id: int, repo: T) -> bool:
        try:
            with UnitOfWork(repo) as uow:
                result = uow.repo.delete(id, uow.session)
            return result
        except OperationalError as e:
            raise e
