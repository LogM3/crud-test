from typing import Annotated

from fastapi import APIRouter, Depends, status, Query

from schema.items import ItemSchema, ItemCreateSchema, ItemUpdateSchema
from services.items import ItemService
from dependency import get_item_service


router: APIRouter = APIRouter(prefix='/items', tags=['crud'])


@router.get(
    '/{item_id}',
    response_model=ItemSchema,
    responses={404: {'description': 'Item not found'}},
    description=''
)
async def get(
    item_id: int,
    service: Annotated[ItemService, Depends(get_item_service)]
):
    return await service.get_item(item_id)


@router.get('/', response_model=list[ItemSchema])
async def list(
    service: Annotated[ItemService, Depends(get_item_service)],
    limit: int = Query(ge=1, description='Макс. кол-во записей', default=20),
    offset: int = Query(ge=0, description='Пропустить N записей', default=0)
):
    return await service.get_all(limit, offset)


@router.post(
    '/',
    response_model=ItemSchema,
    status_code=status.HTTP_201_CREATED,
    responses={409: {'description': 'Title must be unique'}}
)
async def create(
    item: ItemCreateSchema,
    service: Annotated[ItemService, Depends(get_item_service)]
):
    return await service.create_item(item)


@router.put(
    '/{item_id}',
    response_model=ItemSchema,
    responses={
        404: {'description': 'Item not found'},
        409: {'description': 'Title must be unique'}
    }
)
async def update(
    item_id: int,
    item_update_data: ItemUpdateSchema,
    service: Annotated[ItemService, Depends(get_item_service)]
):
    return await service.update_item(item_id, item_update_data)


@router.delete(
    '/{item_id}',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {'description': 'Item not found'}}
)
async def delete(
    item_id: int,
    service: Annotated[ItemService, Depends(get_item_service)]
):
    return await service.delete_item(item_id)
