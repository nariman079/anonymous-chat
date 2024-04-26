from typing import Generator

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


async def get_db() -> Generator:
    """ Dependency for getting async session """
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
