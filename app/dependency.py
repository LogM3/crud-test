from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_db_connection
from app.repositories.items import ItemRepository
from app.services.items import ItemService


async def get_item_repository(
    session: AsyncSession = Depends(get_db_connection)
) -> ItemRepository:
    return ItemRepository(session)


async def get_item_service(
        item_repo: ItemRepository = Depends(get_item_repository)
) -> ItemService:
    return ItemService(item_repo)
