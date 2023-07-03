from fastapi import FastAPI, Body
import requests
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Text, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session, sessionmaker

app = FastAPI()
# data = {'questions_num': 2}

@app.post("/post_num")
def post_num(questions_num: int):

    сount_same_question = 0
    # получаем данные с сайта

    response = requests.get(f"https://jservice.io/api/random?count={questions_num}")

    # подключаемся к БД и считываем данные

    engine = create_engine('postgresql+psycopg2://postgres:postgres@192.168.1.100/quiz')
    session = Session(bind=engine)

    class Base(DeclarativeBase):
        pass

    class Questions(Base):
        __tablename__ = 'questions'
        id_question = Column(Integer, primary_key=True)
        question = Column(Text)
        answer = Column(String(50))
        date_create = Column(DateTime())

    data = session.query(Questions).all()
    id_bd = [d.id_question for d in data]

    # проверяем есть ли уже полученные данные в бд

    for i in range(questions_num):
        if response.json()[i]['id'] in id_bd:
            print('break')
            сount_same_question += 1
        else:
            questions1 = Questions(
                id_question=response.json()[i]['id'],
                question=response.json()[i]['question'],
                answer=response.json()[i]['answer'],
                date_create=response.json()[i]['created_at']
            )
            session.add(questions1)
            session.commit()

    # запрашиваем еще данные при совпадении

    if сount_same_question != 0:
        post_num(сount_same_question)

    return response.json()[-1]