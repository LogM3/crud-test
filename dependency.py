from database.database import get_db_connection
from repositories.items import ItemRepository
from services.items import ItemService

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


async def get_item_repository(
    session: AsyncSession = Depends(get_db_connection)
) -> ItemRepository:
    return ItemRepository(session)


async def get_item_service(
        item_repo: ItemRepository = Depends(get_item_repository)
) -> ItemService:
    return ItemService(item_repo)
