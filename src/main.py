# from fastapi_users import fastapi_users
# from fastapi_users import FastAPIUsers
# 
from fastapi import FastAPI
import uvicorn
# from pydantic import BaseModel, Field
# from typing import List, Optional
# from datetime import datetime
# from enum import Enum

from .auth.base_config import auth_backend, fastapi_users
from .auth.schemas import UserRead, UserCreate
# from auth.schemas import UserRead, UserCreate
# from auth.manager import get_user_manager
# from fastapi import Depends
from src.operations.router import router as router_operation


app = FastAPI(
    title="Trading App"
)

# 6 урок убрали
# урок 5 29:30 роутеры
# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],   # к какой группе пренадлежит endpoint
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],  # к какой группе пренадлежит endpoint
)


app.include_router(router_operation)


# 6 урок все что ниже убрали

# current_user = fastapi_users.current_user()


#  из https://fastapi-users.github.io/fastapi-users/12.0/usage/current-user/
#  5 урок 43:00 юзера можно делать активным/верифицированым/супер/не активным
#  тоже исползуется Depends
# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.username}"
# 
# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, anonym"

