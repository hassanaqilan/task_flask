from sqlalchemy import Table, Column, Integer, String, DateTime


class Schema:
    def __init__(self, metadata, engine):

        self.metadata_obj = metadata
        self.engine = engine
        self.student_table = Table(
            "students",
            self.metadata_obj,
            Column("id", Integer, primary_key=True),
            Column("name", String(16)),
            Column("grade", Integer),
            Column("age", Integer),
            Column("created_at", DateTime))
        self.metadata_obj.create_all(self.engine)

    def student(self):
        return self.student_table
