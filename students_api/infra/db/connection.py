from sqlalchemy import create_engine, MetaData
from students_api.infra.db.schema import Schema


class Connection:
    DATABASE_URL = "postgresql://postgres:secret@localhost:5432/my_company"

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL)
        self.metadata = MetaData()
        self.schema = Schema(self.metadata, self.engine)
