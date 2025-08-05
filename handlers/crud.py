from fastapi import APIRouter

from schema.items import ItemSchema, ItemCreateSchema

router: APIRouter = APIRouter(prefix='/items', tags=['crud'])


@router.get('/{item_id}', response_model=ItemSchema)
async def get(item_id: int):
    pass


@router.get('/', response_model=list[ItemSchema])
async def list():
    pass


@router.post('/', response_model=ItemSchema)
async def create(item: ItemCreateSchema):
    return item


@router.put('/{item_id}', response_model=ItemSchema)
async def update(item_id: int):
    pass


@router.delete('/{item_id}')
async def delete(item_id: int):
    pass
