import uuid

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import Base

class User(Base):

    __tablename__ = "ritik"

    id : Mapped[uuid.UUID] = mapped_column(
        primary_key=True
    )

    full_name : Mapped[str] = mapped_column(
        String(30)
    )

    email : Mapped[str] = mapped_column(
        String(225),
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )