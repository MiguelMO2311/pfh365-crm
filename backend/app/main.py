from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base

from app.routers import expedientes, operaciones, cargas, documentos, alertas, dashboard, auth

# Initialize DB models
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(dashboard.router, prefix=settings.API_V1_STR)
app.include_router(expedientes.router, prefix=settings.API_V1_STR)
app.include_router(operaciones.router, prefix=settings.API_V1_STR)
app.include_router(cargas.router, prefix=settings.API_V1_STR)
app.include_router(documentos.router, prefix=settings.API_V1_STR)
app.include_router(alertas.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": "Welcome to PFH365 CRM API"}
