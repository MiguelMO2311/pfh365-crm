from sqlalchemy.orm import Session
from app.models.operacion import Operacion
from app.schemas.operacion import OperacionCreate, OperacionUpdate
from app.models.checklist import Checklist, ChecklistItem
from app.services.checklist_generator import generar_items_por_operacion
from typing import List, Optional

def get_operacion(db: Session, operacion_id: int) -> Optional[Operacion]:
    return db.query(Operacion).filter(Operacion.id == operacion_id).first()

def get_operaciones_by_expediente(db: Session, expediente_id: int) -> List[Operacion]:
    return db.query(Operacion).filter(Operacion.expediente_id == expediente_id).all()

def create_operacion(db: Session, expediente_id: int, operacion: OperacionCreate) -> Operacion:
    db_operacion = Operacion(**operacion.model_dump(), expediente_id=expediente_id)
    db.add(db_operacion)
    db.commit()
    db.refresh(db_operacion)
    
    # Generate checklist for the operation
    db_checklist = Checklist(operacion_id=db_operacion.id)
    db.add(db_checklist)
    db.commit()
    db.refresh(db_checklist)
    
    items = generar_items_por_operacion(db_operacion.tipo_operacion)
    for item in items:
        db_item = ChecklistItem(checklist_id=db_checklist.id, descripcion=item.descripcion, requerido_para_firma=item.requerido_para_firma)
        db.add(db_item)
    db.commit()
    
    return db_operacion

def update_operacion(db: Session, operacion_id: int, operacion: OperacionUpdate) -> Optional[Operacion]:
    db_operacion = get_operacion(db, operacion_id)
    if db_operacion:
        update_data = operacion.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_operacion, key, value)
        db.commit()
        db.refresh(db_operacion)
    return db_operacion

def delete_operacion(db: Session, operacion_id: int) -> bool:
    db_operacion = get_operacion(db, operacion_id)
    if db_operacion:
        db.delete(db_operacion)
        db.commit()
        return True
    return False
