import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = 'postgresql+asyncpg://test_fast_api:test_fast_api@localhost/localdb_fast_api'

engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=True
)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()