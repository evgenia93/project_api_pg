import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Text, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session, sessionmaker

connection = psycopg2.connect(
    user='postgres',
    password='postgres',
    host='192.168.1.100',
    port='5432'
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

with connection.cursor() as cursor:
    sql_creat_database = cursor.execute('create database quiz')

connection.close()


engine = create_engine('postgresql+psycopg2://postgres:postgres@192.168.1.100/quiz')
session = sessionmaker(bind=engine)

class Base(DeclarativeBase): pass

class Questions(Base):
    __tablename__ = 'questions'
    id_question = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(String(50))
    date_create = Column(DateTime())

Base.metadata.create_all(engine)