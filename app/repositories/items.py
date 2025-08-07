from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete

from app.database.models import Item
from app.schema.items import ItemCreateSchema, ItemUpdateSchema


class ItemRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def check_item_title_duplicate(self, title: str) -> bool:
        async with self.session as session:
            print(type(Item.title))
            result = await session.execute(
                select(Item).where(Item.title == title)
            )
        return True if result.first() else False

    async def get_all(self, limit: int, offset: int) -> Sequence[Item | None]:
        async with self.session as session:
            result = await session.execute(
                select(Item).offset(offset).limit(limit)
            )
        return result.scalars().all()

    async def get_item(self, item_id: int) -> Item | None:
        async with self.session as session:
            result = await session.execute(
                select(Item).where(Item.id == item_id)
            )
        return result.scalar_one_or_none()

    async def create_item(self, data: ItemCreateSchema) -> Item:
        async with self.session as session:
            result = await session.execute(
                insert(Item).values(data.model_dump()).returning(Item)
            )
            await session.commit()
        return result.scalar_one()

    async def update_item(
        self,
        item_id: int,
        data: ItemUpdateSchema
    ) -> Item:
        update_data = data.model_dump(exclude_unset=True)
        async with self.session as session:
            item: Item = (
                await session.execute(select(Item).where(Item.id == item_id))
            ).scalar_one()

            for field, value in update_data.items():
                setattr(item, field, value)

            await session.commit()
        return item

    async def delete_item(
            self,
            item_id: int
    ) -> None:
        async with self.session as session:
            await session.execute(delete(Item).where(Item.id == item_id))
            await session.commit()
