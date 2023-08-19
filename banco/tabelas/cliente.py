from sqlalchemy.orm import Mapped
from banco.tipos import UUIDPK
from banco import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[UUIDPK]
    nome: Mapped[str]

    def dict(self):
        return {"id": self.id, "nome": self.nome}
