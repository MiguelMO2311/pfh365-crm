from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models.alerta import TipoAlerta, PrioridadAlerta

class AlertaBase(BaseModel):
    tipo: TipoAlerta
    prioridad: Optional[PrioridadAlerta] = PrioridadAlerta.MEDIA
    mensaje: str
    resuelta: Optional[bool] = False

class AlertaCreate(AlertaBase):
    expediente_id: Optional[int] = None

class AlertaUpdate(BaseModel):
    resuelta: bool
    fecha_resolucion: Optional[datetime] = None

class Alerta(AlertaBase):
    id: int
    expediente_id: Optional[int]
    fecha_creacion: datetime
    fecha_resolucion: Optional[datetime]

    class Config:
        from_attributes = True
