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
