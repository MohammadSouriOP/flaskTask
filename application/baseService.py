from Infra.unitOfWork.unitOfWork import UnitOfWork


class BaseService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow
