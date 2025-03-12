from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('age', Integer),
    Column('grade', Integer),
)