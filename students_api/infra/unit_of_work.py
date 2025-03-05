from sqlalchemy.orm import sessionmaker

from students_api.infra.db.connection import Connection
from typing import Any
SessionLocal = sessionmaker(bind=Connection().engine)


class UnitOfWork:
    def __init__(self) -> None:
        self.session = SessionLocal()

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()
        self.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
