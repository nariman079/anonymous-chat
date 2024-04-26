from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user_models import User


class UserManager:
    """
    Data access layer for operation with user info
    """
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
            self, username: str, email: str,
    ) -> User:
        """ Создание нового пользователя """
        new_user = User(
            username=username,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def create_telegram_user(
            self, **kwargs,
    ) -> User:
        """ Создание нового telegram пользователя """

        # Получение нужных данных
        telegram_id = kwargs.get('telegram_id')
        username = kwargs.get('username')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        additional_information = kwargs.get('additional_information')
        is_active = True if telegram_id else False

        new_user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            additional_information=additional_information,
            is_active=is_active
        )

        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

