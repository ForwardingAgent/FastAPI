from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from datetime import datetime

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),  # nullable - не может принимать ноль
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),  # TIMESTAMP - когда ползоваетль зарегистрирован, datetime - автоматом записывается время
    Column("role_id", Integer, ForeignKey(role.c.id)),  # ссылка внешний ключ на таблицу с ролями
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
# для чего использовать ForeignKey: 
# более понятна связь таблиц в БД (что конкретно юзер (user) берется из таблицы ролей (role)
# если вбиваетс несуществующая роль то будет ошибка (такой роли нет, вы не можете на нее ссылаться)
# не получится удалить таблицу role, тк есть связанная таблица user


# пока БД пуста, надо перенести в нее таблицы, обычно из документации используется код ниже 
# создается движок engine, из sqlalchemy импортируется create_engine и указывается адрес БД (DATABASE_URL)
# затем metadata позволяет создать все таблицы create_all если их нет

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine) 

# в нашем случае мы будем использовать миграции и они помогут создать все таблицы