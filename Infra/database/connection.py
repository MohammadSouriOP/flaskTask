from sqlalchemy import MetaData, create_engine

from Infra.database.schema import Schema


class Connection:
    DATABASE_URL = "postgresql://mohammad:password@localhost:5432/flask"

    def __init__(self) -> None:
        self.engine = create_engine(self.DATABASE_URL)
        self.metadata = MetaData()
        self.schema = Schema(self.metadata, self.engine)
