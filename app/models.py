from sqlalchemy import Table, Column, Integer, MetaData, Text
from app import db_engine as engine

metadata = MetaData()

demo_table = Table('table_name', metadata,
                   Column('ID', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True),
                   Column('name', Text))

metadata.create_all(engine)
