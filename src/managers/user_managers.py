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
