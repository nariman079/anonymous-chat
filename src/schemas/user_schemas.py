from fastapi.exceptions import HTTPException
from pydantic import BaseModel, EmailStr, validator

from src.schemas.base_schemas import TunedModel


class UserCreate(BaseModel):
    username: str
    email: EmailStr

    @validator("username")
    def validate_username(cls, value):
        if len(value) <= 4:
            raise HTTPException(
                status_code=422,
                detail="Minimal len username is 4 symbols"
            )
        return value


class TelegramUserCreate(BaseModel):
    username: str
    telegram_id: str
    first_name: str
    last_name: str
    additional_information: str


class ShowUser(TunedModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool


class ShowTelegramUser(TunedModel):
    id: int
    username: str
    telegram_id: str
    first_name: str
    last_name: str
    additional_information: str
    is_active: bool
