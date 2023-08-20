from api.modelos.clientes.cliente import (
    AutenticarCliente,
    ClienteAutenticado,
    ClienteEntrada,
    ClienteSaida,
)
from fastapi.routing import APIRouter
from fastapi import Depends
from api.utilitarios.autenticacao import autenticar
from banco.repositorios.cliente import RepositorioCliente
from banco.tabelas.cliente import Cliente
from uuid import UUID

router = APIRouter(prefix="/clientes", tags=["Cliente"])
iniciar_repo_cliente = lambda: RepositorioCliente(ClienteEntrada, Cliente)


@router.post("/", status_code=201)
async def criar_cliente(
    dados_entrada: ClienteEntrada,
    repositorio: RepositorioCliente = Depends(iniciar_repo_cliente),
) -> ClienteSaida:
    _cliente = await repositorio.criar(dados_entrada)
    return ClienteSaida(**_cliente.dict())


@router.get("/", status_code=200)
async def listar_clientes(
    repositorio: RepositorioCliente = Depends(iniciar_repo_cliente),
    cliente: Cliente = Depends(autenticar),
) -> list[ClienteSaida]:
    _clientes = await repositorio.listar()
    return [ClienteSaida(**cliente.dict()) for cliente in _clientes]


@router.get("/{id}", status_code=200)
async def obter_cliente(
    id: UUID,
    repositorio: RepositorioCliente = Depends(iniciar_repo_cliente),
    cliente: Cliente = Depends(autenticar),
) -> ClienteSaida:
    _cliente = await repositorio.buscar(id)
    return ClienteSaida(**_cliente.dict())


@router.patch("/{id}", status_code=200)
async def atualizar_cliente(
    id: UUID,
    dados_entrada: ClienteEntrada,
    repositorio: RepositorioCliente = Depends(iniciar_repo_cliente),
    cliente: Cliente = Depends(autenticar),
) -> ClienteSaida:
    _cliente = await repositorio.atualizar(id, dados_entrada)
    return ClienteSaida(**_cliente.dict())


@router.delete("/{id}", status_code=204)
async def remover_cliente(
    id: UUID,
    repositorio: RepositorioCliente = Depends(iniciar_repo_cliente),
    cliente: Cliente = Depends(autenticar),
) -> None:
    await repositorio.deletar(id)


@router.post("/autenticar", status_code=200)
async def autenticar_cliente(
    dados: AutenticarCliente,
    repositorio: RepositorioCliente = Depends(iniciar_repo_cliente),
) -> ClienteAutenticado:
    cliente, credencial = await repositorio.autenticar(**dados.dict())
    return ClienteAutenticado(id=cliente.id, token=credencial.token)
