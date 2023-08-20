from banco.repositorios import Repositorio
from bcrypt import checkpw
from api.modelos.clientes.cliente import ClienteEntrada
from banco.tabelas.cliente import Cliente
from banco.tabelas.autenticacao import Credencial
from banco import abrir_sessao
from sqlalchemy import select
from fastapi import HTTPException
from dataclasses import dataclass


@dataclass
class ClienteNaoEncontrado(HTTPException):
    nome_de_usuario: str
    status_code: int = 404

    def __post_init__(self):
        self.detail = f"Cliente {self.nome_de_usuario} não encontrado"


@dataclass
class SenhaIncorreta(HTTPException):
    status_code: int = 401


class RepositorioCliente(Repositorio[ClienteEntrada, Cliente]):
    @classmethod
    def abrir(cls):
        return cls(ClienteEntrada, Cliente)

    async def autenticar(
        self, nome_de_usuario: str, senha: str
    ) -> tuple[Cliente, Credencial]:
        async with abrir_sessao() as sessao:
            cliente = await sessao.scalar(
                select(Cliente).where(Cliente.nome_de_usuario == nome_de_usuario)
            )
            if not cliente:
                raise ClienteNaoEncontrado(nome_de_usuario)
            if not checkpw(senha.encode(), cliente.senha.encode()):
                raise SenhaIncorreta()

            credencial = await sessao.scalar(
                select(Credencial).where(Credencial.id_cliente == cliente.id)
            )
            if credencial:
                await sessao.delete(credencial)
                await sessao.commit()

            credencial = Credencial(id_cliente=cliente.id)
            sessao.add(credencial)
            await sessao.commit()
            return cliente, credencial

    async def buscar_cliente_por_token(self, token: str) -> Cliente:
        async with abrir_sessao() as sessao:
            cliente = await sessao.scalar(
                select(Cliente)
                .join(Credencial, Cliente.id == Credencial.id_cliente)
                .where(Credencial.token == token)
            )
            if not cliente:
                raise HTTPException(status_code=401)

            return cliente
