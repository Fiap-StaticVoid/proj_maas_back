from api.modelos.clientes.cliente import ClienteEntrada, ClienteSaida
from fastapi.routing import APIRouter
from fastapi import Depends
from banco.repositorios import Repositorio
from banco.tabelas.cliente import Cliente
from uuid import UUID

router = APIRouter(prefix="/clientes", tags=["Cliente"])
RepoCliente = Repositorio[ClienteEntrada, Cliente]
iniciar_repo_cliente = lambda: Repositorio(ClienteEntrada, Cliente)


@router.post("/", status_code=201)
async def criar_cliente(
    cliente: ClienteEntrada,
    repositorio: RepoCliente = Depends(iniciar_repo_cliente),
) -> ClienteSaida:
    _cliente = await repositorio.criar(cliente)
    return ClienteSaida(**_cliente.dict())


@router.get("/", status_code=200)
async def listar_clientes(
    repositorio: RepoCliente = Depends(iniciar_repo_cliente),
) -> list[ClienteSaida]:
    _clientes = await repositorio.listar()
    return [ClienteSaida(**cliente.dict()) for cliente in _clientes]


@router.get("/{id}", status_code=200)
async def obter_cliente(
    id: UUID,
    repositorio: RepoCliente = Depends(iniciar_repo_cliente),
) -> ClienteSaida:
    _cliente = await repositorio.buscar(id)
    return ClienteSaida(**_cliente.dict())


@router.patch("/{id}", status_code=200)
async def atualizar_cliente(
    id: UUID,
    cliente: ClienteEntrada,
    repositorio: RepoCliente = Depends(iniciar_repo_cliente),
) -> ClienteSaida:
    _cliente = await repositorio.atualizar(id, cliente)
    return ClienteSaida(**_cliente.dict())


@router.delete("/{id}", status_code=204)
async def remover_cliente(
    id: UUID,
    repositorio: RepoCliente = Depends(iniciar_repo_cliente),
) -> None:
    await repositorio.deletar(id)
