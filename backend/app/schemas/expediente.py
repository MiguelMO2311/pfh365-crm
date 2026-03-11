from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from app.models.expediente import EstadoExpediente
from app.schemas.operacion import Operacion
from app.schemas.alerta import Alerta

class ExpedienteBase(BaseModel):
    numero_expediente: str
    cliente_nombre: str
    cliente_dni: str
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    direccion_inmueble: Optional[str] = None
    banco: Optional[str] = None
    importe_hipoteca: Optional[float] = None
    estado_expediente: Optional[EstadoExpediente] = EstadoExpediente.PREFIRMA

class ExpedienteCreate(ExpedienteBase):
    fecha_prevista_firma: Optional[datetime] = None

class ExpedienteUpdate(BaseModel):
    cliente_nombre: Optional[str] = None
    cliente_dni: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[EmailStr] = None
    direccion_inmueble: Optional[str] = None
    banco: Optional[str] = None
    importe_hipoteca: Optional[float] = None
    estado_expediente: Optional[EstadoExpediente] = None
    fecha_prevista_firma: Optional[datetime] = None
    fecha_firma_real: Optional[datetime] = None

class Expediente(ExpedienteBase):
    id: int
    fecha_creacion: datetime
    fecha_prevista_firma: Optional[datetime]
    fecha_firma_real: Optional[datetime]

    operaciones: List[Operacion] = []
    alertas: List[Alerta] = []

    class Config:
        from_attributes = True
