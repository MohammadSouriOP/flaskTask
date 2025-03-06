from Infra.unitOfWork import unitOfWork


class BaseService:
    def __init__(self, uow: unitOfWork) -> None:
        self.uow = uow
