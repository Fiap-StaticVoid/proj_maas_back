from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///./banco/banco.db")
sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def abrir_sessao():
    return sessionmaker()


def carregar_tabelas():
    # from banco.tabelas import *
    pass


async def criar_banco() -> None:
    carregar_tabelas()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
