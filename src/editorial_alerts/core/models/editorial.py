from datetime import datetime, timezone
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.editorial_alerts.core.models.base import Base


class Article(Base):
    __tablename__= "Articles"

    identificador: Mapped[int] = mapped_column(primary_key=True),
    titulo: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    prazo: Mapped[datetime] = mapped_column(DateTime())
    data_criacao: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())
# Fazer Relação entre a classe Article 
# E a classe Editorial Update
# Relação 1:N

class EditorialUpdate(Base):
    pass