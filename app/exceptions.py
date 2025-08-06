from fastapi import HTTPException, status


class ItemIdNotExists(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            'Сущности с таким id не существует!'
        )


class ItemTitleDuplicated(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status.HTTP_409_CONFLICT,
            'Сущность с таким названием уже существует!'
        )
