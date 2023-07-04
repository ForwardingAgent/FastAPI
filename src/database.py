from typing import AsyncGenerator

# from fastapi import Depends
# from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
# from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from sqlalchemy import MetaData  # Column, String, Boolean, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
# from src.auth.models import role  6 урок, у нас нет role

#  postgresql и драйвер asyncpg для асинхронной работы с базой данных
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# class Base(DeclarativeBase):
#    pass
# Base: DeclarativeMeta = declarative_base()
Base = declarative_base()  #  6 урок изменили Base
# Base исмользуется ниже для создания модели таблицы User

# class User(SQLAlchemyBaseUserTable(UUID), Base): по умолчанию UUID, а у нас в models.py user для 'id' Integer - используем [int]
#  6 урок, убрали class User
# class User(SQLAlchemyBaseUserTable[int], Base):
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)
#     username = Column(String, nullable=False)
#     registered_at = Column(TIMESTAMP, default=datetime.utcnow)
#     role_id = Column(Integer, ForeignKey(role.c.id))  # role.c.id - '.c.' это показывает что у role есть колонка с названием id
#     hashed_password: str = Column(String(length=1024), nullable=False)
#     is_active: bool = Column(Boolean, default=True, nullable=False)
#     is_superuser: bool = Column(Boolean, default=False, nullable=False)
#     is_verified: bool = Column(Boolean, default=False, nullable=False)


# Надо понять два момента:
# 1. тип через двоеточие после имени переменной:
# hashed_password: str = Column(String(length=1024), nullable=False)
# Это не объявление типа, это подсказка типа. Если будете искать больше информации, то ищите type hinting. 
# Подсказка не накладывает никаких ограничений, по факту в переменной может лежать любой тип. 
# Это именно что подсказка для разработчика (подсказки синтаксические будут от IDE итд)
# 2. id имеет тип int и тут же тоже пихаем в него "Column"
# Если вкратце - это ORM. Задача ORM - абстрагировать разработчика от работы с БД. 
# Мы используем один и тот же класс для определения таблицы в базе и для работы с объектами в нашей программе. 
# То есть Column нужно для того чтобы библиотека делала корректные запросы при обращении к БД. 
# Когда же мы будем работать с экземпляром класса User в коде, в поле id будет лежать int.
# Для понимания, обратите внимание, как в https://github.com/artemonsh/fastapi_course/blob/main/Lesson_05/main.py#L43 мы берем поле username экземпляра класса User. 
# И хоть в классе бы объявили это поле как класс Column https://github.com/artemonsh/fastapi_course/blob/main/Lesson_05/auth/database.py#L21, при обращении к полю username мы получим строку (потому что в базе в колонке username лежит строковое значение).


#  engine точка входа SQLAlchemy в наше приложение, далее с помощью engine создаются async_sessionmaker - сессии(временные соединения)
#  для работы с БД чтобы можно было вставить/обновить/удалить данные
engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# удаляем (урок 5 19:40), тк она создает БД и таблицы при каждом запуске приложения, а у нас таблицы созданы и заполнены.
# async def create_db_and_tables():
#    async with engine.begin() as conn:
#        await conn.run_sync(Base.metadata.create_all)


# получение асинхронной сессии, через контекстный менеджер получается сессия
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


#  получение пользователя, (5 урок 20:10) Depends - ф-я из FASTApi, она отвечает за инекцию зависимостей, те использовать внешние ф-ии чтобы использовать в нашей ф-ии
#  6 урок, убрали функцию
# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#    yield SQLAlchemyUserDatabase(session, User)

#  мы получаем пользователя ф-ей async def get_user_db(session: AsyncSession = Depends(get_async_session)) 
#  у нас есть связь с БД (session) и модель пользователя (User)