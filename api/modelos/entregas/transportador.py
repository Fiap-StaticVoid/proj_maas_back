from pydantic import BaseModel, validator
from re import match

from api.modelos import BaseRecurso


class TransportadorEntrada(BaseModel):
    nome: str
    placa_veiculo: str

    @validator("placa_veiculo")
    def placa_eh_valida(cls, placa):

        if any(
            (
                match(r"^\w{3}-\d{4}$", placa),
                match(r"^\w{3}\d\w\d{2}$", placa),
            )
        ):
            return placa
        raise ValueError("Placa inválida")


class Transportador(BaseRecurso, TransportadorEntrada):
    pass
