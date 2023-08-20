from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, UniqueConstraint
from banco.tipos import UUIDPK
from banco import Base
from secrets import token_urlsafe


class Credencial(Base):
    __tablename__ = "credenciais"
    __table_args__ = (UniqueConstraint("id_cliente"),)

    id: Mapped[UUIDPK]
    token: Mapped[str] = mapped_column(default=token_urlsafe(128))
    id_cliente: Mapped[UUID] = mapped_column(ForeignKey("clientes.id"))

    @property
    def senha(self):
        return self._senha

    def dict(self):
        return {"id": self.id, "token": self.token}
