from sqlalchemy import MetaData, create_engine

from students_api.infra.db.schema import Schema


class Connection:
    DATABASE_URL = "postgresql://postgres:secret@localhost:5432/my_company"

    def __init__(self) -> None:
        self.engine = create_engine(self.DATABASE_URL)
        self.metadata = MetaData()
        self.schema = Schema(self.metadata, self.engine)
