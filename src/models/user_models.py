from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from src.database import Base
from src.enums.status_enums import AccountStatus


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    telegram_id = Column(String, nullable=True, unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    additional_information = Column(String, nullable=True)
    account_status = Column(PgEnum(AccountStatus, name='account_status_enum'), default=AccountStatus.NO_ACTIVE, nullable=False)

