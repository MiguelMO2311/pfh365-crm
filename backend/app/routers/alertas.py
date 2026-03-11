from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.alerta import Alerta as AlertaModel
from app.schemas.alerta import Alerta, AlertaUpdate
from datetime import datetime

router = APIRouter(prefix="/alertas", tags=["Alertas"])

@router.get("/", response_model=List[Alerta])
def read_alertas_activas(db: Session = Depends(get_db)):
    return db.query(AlertaModel).filter(AlertaModel.resuelta == False).all()

@router.put("/{alerta_id}/resolver", response_model=Alerta)
def resolver_alerta(alerta_id: int, db: Session = Depends(get_db)):
    db_alerta = db.query(AlertaModel).filter(AlertaModel.id == alerta_id).first()
    if not db_alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    db_alerta.resuelta = True
    db_alerta.fecha_resolucion = datetime.now()
    db.commit()
    db.refresh(db_alerta)
    return db_alerta
