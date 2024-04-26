from fastapi import APIRouter

from src.database import async_session
from src.managers.user_managers import UserManager
from src.schemas.user_schemas import ShowUser, UserCreate

user_router = APIRouter()


async def _create_new_user(body: UserCreate) -> ShowUser:
    """  Асинхронное создание пользователя """
    async with async_session() as session:
        async with session.begin():
            user_manage = UserManager(session)
            user = await user_manage.create_user(
                username=body.username,
                email=body.email
            )
            return ShowUser(
                id=user.id,
                username=user.username,
                email=user.email,
                is_active=user.is_active
            )


@user_router.post('/', response_model=ShowUser)
async def create_user(body: UserCreate) -> ShowUser:
    return await _create_new_user(body)
