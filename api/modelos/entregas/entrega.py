from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from api.modelos import BaseRecurso


class EntregaEntrada(BaseModel):
    data_da_solicitacao: datetime
    data_da_entrega: datetime
    produtos: list[str]

    id_cliente: UUID
    id_transportador: UUID

    @property
    def tempo_de_entrega(self):
        return self.data_da_entrega - self.data_da_solicitacao


class EntregaSaida(BaseRecurso, EntregaEntrada):
    pass
