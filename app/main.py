from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fashion OS v1",
    description="Sistema operacional para criação, gestão, produção e lançamento de moda com IA, agentes Claude e stack gratuita.",
    version="1.0.0",
)

app.include_router(router)
