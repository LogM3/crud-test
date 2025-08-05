from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker
)

from settings import Settings


class Base(DeclarativeBase):
    pass


engine: AsyncEngine = create_async_engine(url=Settings().db_url)

sessionmaker: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)
