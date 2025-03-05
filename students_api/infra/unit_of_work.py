from sqlalchemy.orm import sessionmaker
from students_api.infra.db.connection import Connection

SessionLocal = sessionmaker(bind=Connection().engine)


class UnitOfWork:
    def __init__(self) -> None:
        self.session = SessionLocal()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
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
