from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.carga import TipoCarga, EstadoCarga

class CargaBase(BaseModel):
    tipo_carga: TipoCarga
    descripcion: str
    estado: Optional[EstadoCarga] = EstadoCarga.VIGENTE
    genera_operacion_adicional: Optional[bool] = False

class CargaCreate(CargaBase):
    pass

class CargaUpdate(BaseModel):
    tipo_carga: Optional[TipoCarga] = None
    descripcion: Optional[str] = None
    estado: Optional[EstadoCarga] = None
    genera_operacion_adicional: Optional[bool] = None

class Carga(CargaBase):
    id: int
    operacion_id: int

    class Config:
        from_attributes = True
