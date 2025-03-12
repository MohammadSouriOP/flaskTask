from src.infra.repo.student_repo import StudentRepo

from src.application.base_service import BaseService


class StudentServices(BaseService):
    def __init__(self, repo: StudentRepo) -> None:
        self.repo = repo
