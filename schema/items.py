from pydantic import BaseModel, Field


class ItemSchema(BaseModel):
    id: int
    title: str
    description: str
    amount: int = Field(ge=0)
    is_hidden: bool


class ItemCreateSchema(BaseModel):
    title: str
    description: str
    amount: int = Field(ge=0)
    is_hidden: bool


class ItemUpdateSchema(BaseModel):
    title: str | None = None
    description: str | None = None
    amount: int | None = Field(ge=0, default=None)
    is_hidden: bool | None = None
