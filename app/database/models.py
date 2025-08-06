from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str]
    description: Mapped[str]
    amount: Mapped[int]
    is_hidden: Mapped[bool]
