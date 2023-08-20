from sqlalchemy.orm import Mapped
from banco.tipos import UUIDPK
from banco import Base
from bcrypt import hashpw, gensalt


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[UUIDPK]
    nome: Mapped[str]
    nome_de_usuario: Mapped[str]
    _senha: Mapped[str]

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha: str):
        self._senha = hashpw(senha.encode(), gensalt()).decode()

    def dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nome_de_usuario": self.nome_de_usuario,
        }
