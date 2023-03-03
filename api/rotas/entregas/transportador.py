from api.modelos.entregas.transportador import Transportador, TransportadorEntrada
from fastapi.routing import APIRouter
from uuid import uuid4
from api.modelos import BaseRecurso


router = APIRouter(prefix="/transportadores", tags=["Transportadores"])
_trasportadores = [
    Transportador(id=uuid4(), nome="João", placa_veiculo="ABC-1234"),
    Transportador(id=uuid4(), nome="Maria", placa_veiculo="DEF5G67"),
]


@router.post("/", status_code=201)
async def criar_transportador(transportador: TransportadorEntrada) -> BaseRecurso:
    _trasportadores.append(transportador)
    return {"id": transportador.id}


@router.get("/", status_code=200)
async def listar_transportadores() -> list[Transportador]:
    return _trasportadores


@router.get("/{id}", status_code=200)
async def obter_transportador(id: int) -> Transportador:
    return _trasportadores[id - 1]


@router.patch("/{id}", status_code=200)
async def atualizar_transportador(
    id: int, transportador: TransportadorEntrada
) -> BaseRecurso:
    _trasportadores[id - 1] = transportador
    return {"id": transportador.id}


@router.delete("/{id}", status_code=204)
async def remover_transportador(id: int) -> None:
    _trasportadores.pop(id - 1)
