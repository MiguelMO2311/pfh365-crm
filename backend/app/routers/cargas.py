from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.carga import Carga as CargaModel
from app.schemas.carga import Carga, CargaCreate, CargaUpdate

router = APIRouter(prefix="/cargas", tags=["Cargas"])

@router.post("/operacion/{operacion_id}", response_model=Carga, status_code=status.HTTP_201_CREATED)
def create_carga(operacion_id: int, carga: CargaCreate, db: Session = Depends(get_db)):
    db_carga = CargaModel(**carga.model_dump(), operacion_id=operacion_id)
    db.add(db_carga)
    db.commit()
    db.refresh(db_carga)
    return db_carga

@router.get("/operacion/{operacion_id}", response_model=List[Carga])
def read_cargas_operacion(operacion_id: int, db: Session = Depends(get_db)):
    return db.query(CargaModel).filter(CargaModel.operacion_id == operacion_id).all()

@router.put("/{carga_id}", response_model=Carga)
def update_carga(carga_id: int, carga: CargaUpdate, db: Session = Depends(get_db)):
    db_carga = db.query(CargaModel).filter(CargaModel.id == carga_id).first()
    if not db_carga:
        raise HTTPException(status_code=404, detail="Carga no encontrada")
    update_data = carga.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_carga, key, value)
    db.commit()
    db.refresh(db_carga)
    return db_carga

@router.delete("/{carga_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_carga(carga_id: int, db: Session = Depends(get_db)):
    db_carga = db.query(CargaModel).filter(CargaModel.id == carga_id).first()
    if not db_carga:
        raise HTTPException(status_code=404, detail="Carga no encontrada")
    db.delete(db_carga)
    db.commit()
    return None
