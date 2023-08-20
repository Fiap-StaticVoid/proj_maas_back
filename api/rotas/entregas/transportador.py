from fastapi import Depends
from api.modelos.entregas.transportador import TransportadorSaida, TransportadorEntrada
from fastapi.routing import APIRouter
from api.utilitarios.autenticacao import autenticar

from banco.repositorios import Repositorio
from banco.tabelas.cliente import Cliente
from banco.tabelas.transportador import Transportador
from uuid import UUID

router = APIRouter(prefix="/transportadores", tags=["Transportador"])
RepoTransportadores = Repositorio[TransportadorEntrada, Transportador]
iniciar_repo_transportadores = lambda: Repositorio(TransportadorEntrada, Transportador)


@router.post("/", status_code=201)
async def criar_transportador(
    transportador: TransportadorEntrada,
    repositorio: RepoTransportadores = Depends(iniciar_repo_transportadores),
    cliente: Cliente = Depends(autenticar),
) -> TransportadorSaida:
    _transportador = await repositorio.criar(transportador)
    return TransportadorSaida(**_transportador.dict())


@router.get("/", status_code=200)
async def listar_transportadores(
    repositorio: RepoTransportadores = Depends(iniciar_repo_transportadores),
    cliente: Cliente = Depends(autenticar),
) -> list[TransportadorSaida]:
    transportadores = await repositorio.listar()
    return [
        TransportadorSaida(**transportador.dict()) for transportador in transportadores
    ]


@router.get("/{id}", status_code=200)
async def obter_transportador(
    id: UUID,
    repositorio: RepoTransportadores = Depends(iniciar_repo_transportadores),
    cliente: Cliente = Depends(autenticar),
) -> TransportadorSaida:
    transportador = await repositorio.buscar(id)
    return TransportadorSaida(**transportador.dict())


@router.patch("/{id}", status_code=200)
async def atualizar_transportador(
    id: UUID,
    transportador: TransportadorEntrada,
    repositorio: RepoTransportadores = Depends(iniciar_repo_transportadores),
    cliente: Cliente = Depends(autenticar),
) -> TransportadorSaida:
    _transportador = await repositorio.atualizar(id, transportador)
    return TransportadorSaida(**_transportador.dict())


@router.delete("/{id}", status_code=204)
async def remover_transportador(
    id: UUID,
    repositorio: RepoTransportadores = Depends(iniciar_repo_transportadores),
    cliente: Cliente = Depends(autenticar),
) -> None:
    await repositorio.deletar(id)
