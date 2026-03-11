from sqlalchemy.orm import Session
from app.models.expediente import Expediente
from app.schemas.expediente import ExpedienteCreate, ExpedienteUpdate
from typing import List, Optional

def get_expediente(db: Session, expediente_id: int) -> Optional[Expediente]:
    return db.query(Expediente).filter(Expediente.id == expediente_id).first()

def get_expedientes(db: Session, skip: int = 0, limit: int = 100) -> List[Expediente]:
    return db.query(Expediente).offset(skip).limit(limit).all()

def create_expediente(db: Session, expediente: ExpedienteCreate) -> Expediente:
    db_expediente = Expediente(**expediente.model_dump())
    db.add(db_expediente)
    db.commit()
    db.refresh(db_expediente)
    return db_expediente

def update_expediente(db: Session, expediente_id: int, expediente: ExpedienteUpdate) -> Optional[Expediente]:
    db_expediente = get_expediente(db, expediente_id)
    if db_expediente:
        update_data = expediente.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_expediente, key, value)
        db.commit()
        db.refresh(db_expediente)
    return db_expediente

def delete_expediente(db: Session, expediente_id: int) -> bool:
    db_expediente = get_expediente(db, expediente_id)
    if db_expediente:
        db.delete(db_expediente)
        db.commit()
        return True
    return False
