from pydantic import BaseModel

from api.modelos import BaseRecurso


class ClienteEntrada(BaseModel):
    nome: str


class ClienteSaida(BaseRecurso, ClienteEntrada):
    pass
