from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.prediccion_router import router
from fastapi.responses import FileResponse
import os

app = FastAPI(
    title="IA Recomendacion de Cultivos",
    description="API para prediccion de cultivos usando Random Forest y SVM",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return FileResponse("web/index.html")
