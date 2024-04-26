from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.services import user_services
from src.schemas.user_schemas import ShowUser, UserCreate, TelegramUserCreate, ShowTelegramUser


user_router = APIRouter()


@user_router.post('/', response_model=ShowUser)
async def create_user(
        body: UserCreate,
        async_session: AsyncSession = Depends(get_db)) -> ShowUser:
    """ Создание обычного пользователя """
    return await user_services._create_new_user(body, async_session)


@user_router.post('/telegram_users/', response_model=ShowTelegramUser)
async def create_telegram_user(
        body: TelegramUserCreate,
        async_session: AsyncSession = Depends(get_db)) -> ShowTelegramUser:
    """ Создание telegram пользователя """
    return await user_services._create_new_telegram_user(body, async_session)
