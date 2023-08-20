from fastapi.security import HTTPBearer
from fastapi import Depends
from banco.repositorios.cliente import RepositorioCliente
from banco.tabelas.cliente import Cliente


async def autenticar(bearer: HTTPBearer = Depends(HTTPBearer())) -> Cliente:
    repo_cliente = RepositorioCliente.abrir()
    return await repo_cliente.buscar_cliente_por_token(bearer.credentials)
