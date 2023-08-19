from typing import Any, Generic, Type, TypeVar, Iterator
from pydantic import BaseModel
from banco import Base, abrir_sessao
from uuid import UUID
from sqlalchemy import select
from dataclasses import dataclass
from enum import StrEnum

M = TypeVar("M", bound=BaseModel)
I = TypeVar("I", bound=Base)


class Operador(StrEnum):
    igual = "igual"


@dataclass
class Filtro:
    modelo: Type[Base]
    campo: str
    operador: Operador
    valor: Any

    def parse(self):
        match self.operador:
            case Operador.igual:
                return self.campo == self.valor


class Repositorio(Generic[M, I]):
    def __init__(self, modelo: Type[M], instancia: Type[I]):
        self.tipo_modelo = modelo
        self.tipo_instancia = instancia

    async def criar(self, dados: M) -> I:
        async with abrir_sessao() as sessao:
            instancia = self.tipo_instancia(**dados.dict())
            sessao.add(instancia)
            await sessao.commit()
            return instancia

    async def buscar(self, id: UUID) -> I:
        async with abrir_sessao() as sessao:
            return await sessao.scalar(
                select(self.tipo_instancia).where(self.tipo_instancia.id == id)
            )

    async def listar(self) -> Iterator[I]:
        async with abrir_sessao() as sessao:
            return await sessao.scalars(select(self.tipo_instancia))

    async def deletar(self, id: UUID):
        async with abrir_sessao() as sessao:
            instancia = await sessao.scalar(
                select(self.tipo_instancia).where(self.tipo_instancia.id == id)
            )
            await sessao.delete(instancia)
            await sessao.commit()

    async def atualizar(self, id: UUID, novos_dados: M) -> I:
        async with abrir_sessao() as sessao:
            instancia = await sessao.scalar(
                select(self.tipo_instancia).where(self.tipo_instancia.id == id)
            )
            for campo in novos_dados.dict():
                setattr(instancia, campo, getattr(novos_dados, campo))
            sessao.add(instancia)
            await sessao.commit()
            return instancia