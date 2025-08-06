from fastapi import HTTPException


class ItemIdNotExists(HTTPException):
    def __init__(self) -> None:
        super().__init__(404, 'Сущности с таким id не существует!')


class ItemTitleDuplicated(HTTPException):
    def __init__(self) -> None:
        super().__init__(409, 'Сущность с таким названием уже существует!')
