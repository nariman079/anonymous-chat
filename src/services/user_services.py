from sqlalchemy.ext.asyncio import AsyncSession

from src.managers.user_managers import UserManager
from src.schemas.user_schemas import ShowUser, UserCreate, TelegramUserCreate


async def _create_new_user(body: UserCreate, async_session: AsyncSession) -> ShowUser:
    """  Асинхронное создание пользователя """
    async with async_session as session:
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


async def _create_new_telegram_user(body: TelegramUserCreate, async_session: AsyncSession) -> ShowUser:
    """  Асинхронное создание пользователя """
    async with async_session as session:
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
