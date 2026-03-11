from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ChecklistItemBase(BaseModel):
    descripcion: str
    completado: Optional[bool] = False
    requerido_para_firma: Optional[bool] = True

class ChecklistItemCreate(ChecklistItemBase):
    pass

class ChecklistItemUpdate(BaseModel):
    descripcion: Optional[str] = None
    completado: Optional[bool] = None
    requerido_para_firma: Optional[bool] = None

class ChecklistItem(ChecklistItemBase):
    id: int
    checklist_id: int

    class Config:
        from_attributes = True

class ChecklistBase(BaseModel):
    completado: Optional[bool] = False

class ChecklistCreate(ChecklistBase):
    operacion_id: int

class ChecklistUpdate(BaseModel):
    completado: Optional[bool] = None
    fecha_completado: Optional[datetime] = None

class Checklist(ChecklistBase):
    id: int
    operacion_id: int
    fecha_creacion: datetime
    fecha_completado: Optional[datetime]
    items: List[ChecklistItem] = []

    class Config:
        from_attributes = True
