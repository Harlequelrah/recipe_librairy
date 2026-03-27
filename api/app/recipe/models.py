from datetime import datetime

from sqlalchemy import Text

from app.settings.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Recipe(Base):
    __tablename__ = "recipes"
    id: Mapped[int] = mapped_column(primary_key=True)
    titre : Mapped[str]
    ingredients : Mapped[str]=mapped_column(Text)
    temps_cuisson:Mapped[float]
    date_created: Mapped[datetime] = mapped_column(default=func.now())
    date_updated: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(default=False)
    date_deleted: Mapped[datetime] = mapped_column(default=None)
