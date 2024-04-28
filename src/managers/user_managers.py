from sqlalchemy import update, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.enums.status_enums import AccountStatus
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

        # Получение данных
        telegram_id = kwargs.get('telegram_id')
        username = kwargs.get('username')
        first_name = kwargs.get('first_name')
        last_name = kwargs.get('last_name')
        additional_information = kwargs.get('additional_information')

        new_user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            additional_information=additional_information,
            account_status=AccountStatus.ACTIVE,
        )

        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def delete_user(self, user_id: int) -> None | int:
        """ Удаление пользователя """

        query = update(
            User
        ).where(
            and_(
                User.id == user_id,
                not User.telegram_id
            )
        ).values(
            account_status=AccountStatus.DELETED
        ).returning(
            User.id
        )

        res = await self.db_session.execute(query)
        deleted_user_id_row = res.fetchone()

        if deleted_user_id_row:
            return deleted_user_id_row[0]
