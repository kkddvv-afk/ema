from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title="Web App API", version="0.1.0")

    allowed_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/health")
    def health_check() -> dict:
        return {"status": "ok"}

    @app.get("/api/hello")
    def say_hello(name: str | None = None) -> dict:
        greeting_name = name or "мир"
        return {"message": f"Привет, {greeting_name}!"}

    return app


app = create_app()

