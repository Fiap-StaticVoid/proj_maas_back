from sqlalchemy.orm import Mapped, mapped_column
from banco.tipos import UUIDPK
from banco import Base
from uuid import UUID
from sqlalchemy import ForeignKey


class Transportador(Base):
    __tablename__ = "transportadores"

    id: Mapped[UUIDPK]
    nome: Mapped[str]
    placa_veiculo: Mapped[str]
    id_cliente: Mapped[UUID] = mapped_column(ForeignKey("clientes.id"))

    def dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "placa_veiculo": self.placa_veiculo,
            "id_cliente": self.id_cliente,
        }
