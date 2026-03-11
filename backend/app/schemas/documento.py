from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.documento import TipoDocumento

class DocumentoBase(BaseModel):
    nombre: str
    tipo: TipoDocumento
    valido: Optional[bool] = True
    ruta_archivo: Optional[str] = None

class DocumentoCreate(DocumentoBase):
    fecha_caducidad: Optional[datetime] = None

class DocumentoUpdate(BaseModel):
    nombre: Optional[str] = None
    tipo: Optional[TipoDocumento] = None
    valido: Optional[bool] = None
    ruta_archivo: Optional[str] = None
    fecha_caducidad: Optional[datetime] = None

class Documento(DocumentoBase):
    id: int
    operacion_id: int
    fecha_subida: datetime
    fecha_caducidad: Optional[datetime]

    class Config:
        from_attributes = True
