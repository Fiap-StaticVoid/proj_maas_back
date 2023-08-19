from sqlalchemy.orm import Mapped
from banco.tipos import UUIDPK
from banco import Base


class Transportador(Base):
    __tablename__ = "transportadores"

    id: Mapped[UUIDPK]
    nome: Mapped[str]
    placa_veiculo: Mapped[str]

    def dict(self):
        return {"id": self.id, "nome": self.nome, "placa_veiculo": self.placa_veiculo}
