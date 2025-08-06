from typing import Sequence

from fastapi import HTTPException

from database.models import Item
from repositories.items import ItemRepository
from schema.items import ItemCreateSchema, ItemUpdateSchema
from exceptions import ItemIdNotExists, ItemTitleDuplicated


class ItemService:
    def __init__(self, repo: ItemRepository) -> None:
        self.repo = repo

    async def get_all(
            self,
            limit: int = 0,
            offset: int = 0
    ) -> Sequence[Item | None]:
        return await self.repo.get_all(limit, offset)

    async def get_item(self, item_id: int) -> Item | HTTPException:
        result = await self.repo.get_item(item_id)
        if not result:
            raise ItemIdNotExists()
        return result

    async def create_item(
        self,
        item_data: ItemCreateSchema
    ) -> Item | HTTPException:
        if await self.repo.check_item_title_duplicate(item_data.title):
            raise ItemTitleDuplicated()

        return await self.repo.create_item(item_data)

    async def update_item(
        self,
        item_id: int,
        item_data: ItemUpdateSchema
    ) -> Item | HTTPException:
        item: Item | None = await self.repo.get_item(item_id)
        if not item:
            raise ItemIdNotExists()

        if item_data.title and item_data.title != item.title:
            if await self.repo.check_item_title_duplicate(item_data.title):
                raise ItemTitleDuplicated()

        return await self.repo.update_item(item, item_data)

    async def delete_item(self, item_id: int) -> None | HTTPException:
        item: Item | None = await self.repo.get_item(item_id)
        if not item:
            raise ItemIdNotExists()

        await self.repo.delete_item(item)
