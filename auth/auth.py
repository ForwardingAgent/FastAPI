from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy


# 23:41 5 урок, докум FASTApi-Transport-Cookie
cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

SECRET = "SECRET"


# 24:00 5 урок, докум FASTApi-Strategies-JWT
def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


# 5 урок 25:00 создаем переменную из докум FASTApi-create a backend
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)