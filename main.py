from uvicorn import run
from servidor import criar_app

app = criar_app()
if __name__ == "__main__":
    run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True,
    )
