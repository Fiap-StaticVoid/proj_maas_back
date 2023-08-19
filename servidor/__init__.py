from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.rotas.clientes.cliente import router as router_cliente
from api.rotas.entregas.entrega import router as router_entrega
from api.rotas.entregas.transportador import router as router_transportador
from banco import criar_banco


def criar_app():
    app = FastAPI()

    @app.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url="/docs")

    @app.on_event("startup")
    async def startup():
        await criar_banco()

    app.include_router(router_cliente)
    app.include_router(router_entrega)
    app.include_router(router_transportador)
    return app
