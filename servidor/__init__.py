from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.rotas.entregas.entrega import router as router_entrega
from api.rotas.entregas.transportador import router as router_transportador


def criar_app():
    app = FastAPI()

    @app.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url="/docs")

    app.include_router(router_entrega)
    app.include_router(router_transportador)
    return app
