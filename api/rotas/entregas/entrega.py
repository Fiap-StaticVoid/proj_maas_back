from uuid import UUID
from fastapi import Depends
from api.modelos.entregas.entrega import EntregaSaida, EntregaEntrada
from fastapi.routing import APIRouter
from banco.repositorios import Repositorio
from banco.tabelas.entrega import Entrega

router = APIRouter(prefix="/entregas", tags=["Entrega"])
RepoEntregas = Repositorio[EntregaEntrada, Entrega]
iniciar_repo_entregas = lambda: Repositorio(EntregaEntrada, Entrega)


@router.post("/", status_code=201)
async def criar_entrega(
    entrega: EntregaEntrada, repositorio: RepoEntregas = Depends(iniciar_repo_entregas)
) -> EntregaSaida:
    _entrega = await repositorio.criar(entrega)
    return EntregaSaida(**_entrega.dict())


@router.get("/", status_code=200)
async def listar_entregas(
    repositorio: RepoEntregas = Depends(iniciar_repo_entregas),
) -> list[EntregaSaida]:
    entregas = await repositorio.listar()
    return [EntregaSaida(**entrega.dict()) for entrega in entregas]


@router.get("/{id}", status_code=200)
async def obter_entrega(
    id: UUID, repositorio: RepoEntregas = Depends(iniciar_repo_entregas)
) -> EntregaSaida:
    entrega = await repositorio.buscar(id)
    return EntregaSaida(**entrega.dict())


@router.patch("/{id}", status_code=200)
async def atualizar_entrega(
    id: UUID,
    entrega: EntregaEntrada,
    repositorio: RepoEntregas = Depends(iniciar_repo_entregas),
) -> EntregaSaida:
    _entrega = await repositorio.atualizar(id, entrega)
    return EntregaSaida(**_entrega.dict())


@router.delete("/{id}", status_code=204)
async def remover_entrega(
    id: UUID, repositorio: RepoEntregas = Depends(iniciar_repo_entregas)
) -> None:
    await repositorio.deletar(id)
