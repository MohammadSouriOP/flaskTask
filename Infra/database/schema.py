from sqlalchemy import Column, DateTime, Engine, Integer, MetaData, String, Table


class Schema:
    def __init__(self, metadata: MetaData, engine: Engine) -> None:

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

    def student(self) -> Table:
        return self.student_table