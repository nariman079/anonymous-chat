from sqlalchemy import Column, Integer, String, Boolean
from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    telegram_id = Column(String, nullable=True, unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    additional_information = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)

