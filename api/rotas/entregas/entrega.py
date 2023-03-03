from api.modelos import BaseRecurso
from api.modelos.entregas.entrega import Entrega, EntregaEntrada
from fastapi.routing import APIRouter
from uuid import uuid4
from datetime import datetime, timedelta

router = APIRouter(prefix="/entregas", tags=["Entrega"])
_entregas = [
    Entrega(
        id=uuid4(),
        data_da_solicitacao=datetime.now(),
        data_da_entrega=datetime.now() + timedelta(days=1),
        produtos=["Arroz", "Feijão", "Macarrão"],
        id_cliente=1,
        id_transportador=1,
    ),
    Entrega(
        id=uuid4(),
        data_da_solicitacao=datetime.now(),
        data_da_entrega=datetime.now() + timedelta(days=1),
        produtos=["Arroz", "Feijão", "Macarrão"],
        id_cliente=2,
        id_transportador=2,
    ),
]


@router.post("/", status_code=201)
async def criar_entrega(entrega: EntregaEntrada) -> BaseRecurso:
    _entregas.append(entrega)
    return {"id": entrega.id}


@router.get("/", status_code=200)
async def listar_entregas() -> list[Entrega]:
    return _entregas


@router.get("/{id}", status_code=200)
async def obter_entrega(id: int) -> Entrega:
    return _entregas[id - 1]


@router.patch("/{id}", status_code=200)
async def atualizar_entrega(id: int, entrega: EntregaEntrada) -> BaseRecurso:
    _entregas[id - 1] = entrega
    return {"id": entrega.id}


@router.delete("/{id}", status_code=204)
async def remover_entrega(id: int) -> None:
    _entregas.pop(id - 1)
