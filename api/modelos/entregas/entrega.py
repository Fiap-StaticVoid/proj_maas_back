from datetime import datetime

from pydantic import BaseModel

from api.modelos import BaseRecurso


class EntregaEntrada(BaseModel):
    data_da_solicitacao: datetime
    data_da_entrega: datetime
    produtos: list[str]

    id_cliente: int
    id_transportador: int

    @property
    def tempo_de_entrega(self):
        return self.data_da_entrega - self.data_da_solicitacao


class Entrega(BaseRecurso, EntregaEntrada):
    pass
