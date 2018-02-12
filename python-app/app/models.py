from sqlalchemy import Table, Column, Integer, MetaData, Text
from app import db_engine, session
from app.utils.db_utils.write import write_demo_records

metadata = MetaData()

demo_table = Table('table_name', metadata,
                   Column('ID', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True),
                   Column('name', Text))

metadata.create_all(db_engine)


# Fill the test table if it empty
if not session.query(demo_table).first():
    write_demo_records()
