from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy

#  6 урок 5:30 добваили 3 импорта
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.config import SECRET_AUTH

# 23:41 5 урок, докум FASTApi-Transport-Cookie
cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)


# 6 убрали добавили ниже secret=SECRET_AUTH
# SECRET = "SECRET"


# 24:00 5 урок, докум FASTApi-Strategies-JWT
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)


# 5 урок 25:00 создаем переменную из докум FASTApi-create a backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

# 6 урок в нчале добавли
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
