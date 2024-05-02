from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.services.user_services import (_create_new_user,
                                        _create_new_telegram_user,
                                        _delete_user)
from src.schemas.user_schemas import ShowUser, UserCreate, TelegramUserCreate, ShowTelegramUser, DeleteUser

user_router = APIRouter()


@user_router.post('/', response_model=ShowUser)
async def create_user(
        body: UserCreate,
        async_session: AsyncSession = Depends(get_db)) -> ShowUser:
    """ Создание обычного пользователя """
    return await _create_new_user(body, async_session)


@user_router.post('/telegram_users/', response_model=ShowTelegramUser)
async def create_telegram_user(
        body: TelegramUserCreate,
        async_session: AsyncSession = Depends(get_db)) -> ShowTelegramUser:
    """ Создание telegram пользователя """
    return await _create_new_telegram_user(body, async_session)


@user_router.delete('/', response_model=DeleteUser)
async def delete_user(
        user_id: int,
        async_session: AsyncSession = Depends(get_db)
) -> DeleteUser:
    deleted_user_id = await _delete_user(user_id, async_session)
    if not deleted_user_id:
        raise HTTPException(
            status_code=404,
            detail="Такого пользователя не существует"
        )
    return DeleteUser(user_id=deleted_user_id)
