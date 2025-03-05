from students_api.infra.unit_of_work import UnitOfWork
class BaseService:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow
