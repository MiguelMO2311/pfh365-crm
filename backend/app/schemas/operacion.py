from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from app.models.operacion import TipoOperacion, EstadoOperacion
from app.schemas.carga import Carga
from app.schemas.documento import Documento
from app.schemas.checklist import Checklist

class OperacionBase(BaseModel):
    tipo_operacion: TipoOperacion
    estado: Optional[EstadoOperacion] = EstadoOperacion.PENDIENTE
    observaciones: Optional[str] = None

class OperacionCreate(OperacionBase):
    fecha_prevista_firma: Optional[datetime] = None

class OperacionUpdate(BaseModel):
    tipo_operacion: Optional[TipoOperacion] = None
    estado: Optional[EstadoOperacion] = None
    fecha_prevista_firma: Optional[datetime] = None
    fecha_firma_real: Optional[datetime] = None
    observaciones: Optional[str] = None

class Operacion(OperacionBase):
    id: int
    expediente_id: int
    fecha_inicio: datetime
    fecha_prevista_firma: Optional[datetime]
    fecha_firma_real: Optional[datetime]

    cargas: List[Carga] = []
    documentos: List[Documento] = []
    checklist: Optional[Checklist] = None

    class Config:
        from_attributes = True
