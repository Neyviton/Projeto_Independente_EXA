from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.editorial_alerts.core.models.base import Base


class Article(Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    deadline: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    updates: Mapped[list[EditorialUpdate]] = relationship(back_populates="article", cascade="all, delete-orphan")


class EditorialUpdate(Base):
    __tablename__ = "editorial_updates"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    remaining_word_count: Mapped[int] = mapped_column(nullable=False)
    hours_until_deadline: Mapped[float] = mapped_column(nullable=False)
    remaining_editorial_steps: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"), nullable=False)
    article: Mapped[Article] = relationship(back_populates="updates")

    predictions: Mapped[list[Prediction]] = relationship(back_populates="editorial_update", cascade="all, delete-orphan")


class Prediction(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(primary_key=True)
    origin: Mapped[str] = mapped_column(String(50), nullable=False)
    model_version: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    result: Mapped[str | None] = mapped_column(nullable=True)
    error_message: Mapped[str | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    editorial_update_id: Mapped[int] = mapped_column(ForeignKey("editorial_updates.id"), nullable=False)
    editorial_update: Mapped[EditorialUpdate] = relationship(back_populates="predictions")