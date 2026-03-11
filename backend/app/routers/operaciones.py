from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.operacion import Operacion, OperacionCreate, OperacionUpdate
from app.schemas.checklist import Checklist
from app.services import operacion_service
from app.models.checklist import Checklist as ChecklistModel

router = APIRouter(prefix="/operaciones", tags=["Operaciones"])

@router.post("/expediente/{expediente_id}", response_model=Operacion, status_code=status.HTTP_201_CREATED)
def create_operacion(expediente_id: int, operacion: OperacionCreate, db: Session = Depends(get_db)):
    return operacion_service.create_operacion(db=db, expediente_id=expediente_id, operacion=operacion)

@router.get("/expediente/{expediente_id}", response_model=List[Operacion])
def read_operaciones_expediente(expediente_id: int, db: Session = Depends(get_db)):
    return operacion_service.get_operaciones_by_expediente(db, expediente_id=expediente_id)

@router.get("/{operacion_id}", response_model=Operacion)
def read_operacion(operacion_id: int, db: Session = Depends(get_db)):
    db_operacion = operacion_service.get_operacion(db, operacion_id=operacion_id)
    if db_operacion is None:
        raise HTTPException(status_code=404, detail="Operación no encontrada")
    return db_operacion

@router.put("/{operacion_id}", response_model=Operacion)
def update_operacion(operacion_id: int, operacion: OperacionUpdate, db: Session = Depends(get_db)):
    db_operacion = operacion_service.update_operacion(db, operacion_id=operacion_id, operacion=operacion)
    if db_operacion is None:
        raise HTTPException(status_code=404, detail="Operación no encontrada")
    return db_operacion

@router.delete("/{operacion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_operacion(operacion_id: int, db: Session = Depends(get_db)):
    success = operacion_service.delete_operacion(db, operacion_id=operacion_id)
    if not success:
        raise HTTPException(status_code=404, detail="Operación no encontrada")
    return None

@router.post("/{operacion_id}/generar-checklist", response_model=Checklist)
def generar_checklist_manual(operacion_id: int, db: Session = Depends(get_db)):
    """Si se necesita recrear o generar un checklist."""
    # Como ya se crea automáticamente, dejaremos esto como stub o reinicio de items si es necesario
    # Simplificación: Retornamos el actual si existe
    db_checklist = db.query(ChecklistModel).filter(ChecklistModel.operacion_id == operacion_id).first()
    if not db_checklist:
        raise HTTPException(status_code=404, detail="No se encontró o no se pudo generar el checklist")
    return db_checklist
