from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from banco.tipos import UUIDPK
from uuid import UUID
from banco import Base
from datetime import datetime
from json import dumps, loads


class Entrega(Base):
    __tablename__ = "entregas"

    id: Mapped[UUIDPK]
    data_da_solicitacao: Mapped[datetime]
    data_da_entrega: Mapped[datetime]
    _produtos: Mapped[str]

    id_cliente: Mapped[UUID] = mapped_column(ForeignKey("clientes.id"))
    id_transportador: Mapped[UUID] = mapped_column(ForeignKey("transportadores.id"))

    @property
    def produtos(self) -> list[str]:
        return loads(self._produtos)

    @produtos.setter
    def produtos(self, value: list[str]):
        self._produtos = dumps(value)

    def dict(self):
        return {
            "id": self.id,
            "data_da_solicitacao": self.data_da_solicitacao,
            "data_da_entrega": self.data_da_entrega,
            "produtos": self.produtos,
            "id_cliente": self.id_cliente,
            "id_transportador": self.id_transportador,
        }
