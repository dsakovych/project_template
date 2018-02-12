# import sqlalchemy.types as types
#
# from sqlalchemy import Column
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
#
# class Invoices(Base):
#     __tablename__ = 'table_name'
#
#     id = Column(types.INTEGER, primary_key=True, nullable=False, autoincrement=True, unique=True)
#     name = Column(types.TEXT, nullable=False)


from sqlalchemy import Table, Column, Integer, MetaData, Text
from app import db_engine as engine

metadata = MetaData()

demo_table = Table('table_name', metadata,
                   Column('ID', Integer, primary_key=True, nullable=False, autoincrement=True, unique=True),
                   Column('name', Text))

metadata.create_all(engine)
