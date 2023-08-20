from uuid import UUID
from pydantic import BaseModel

from api.modelos import BaseRecurso


class ClienteBase(BaseModel):
    nome: str
    nome_de_usuario: str


class ClienteEntrada(ClienteBase):
    senha: str


class ClienteSaida(BaseRecurso, ClienteBase):
    pass


class AutenticarCliente(BaseModel):
    nome_de_usuario: str
    senha: str


class ClienteAutenticado(BaseModel):
    id: UUID
    token: str
