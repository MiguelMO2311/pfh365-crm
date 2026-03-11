from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.documento import Documento as DocumentoModel
from app.schemas.documento import Documento, DocumentoCreate, DocumentoUpdate

router = APIRouter(prefix="/documentos", tags=["Documentos"])

@router.post("/operacion/{operacion_id}", response_model=Documento, status_code=status.HTTP_201_CREATED)
def create_documento(operacion_id: int, documento: DocumentoCreate, db: Session = Depends(get_db)):
    db_documento = DocumentoModel(**documento.model_dump(), operacion_id=operacion_id)
    db.add(db_documento)
    db.commit()
    db.refresh(db_documento)
    return db_documento

@router.get("/operacion/{operacion_id}", response_model=List[Documento])
def read_documentos_operacion(operacion_id: int, db: Session = Depends(get_db)):
    return db.query(DocumentoModel).filter(DocumentoModel.operacion_id == operacion_id).all()

@router.put("/{documento_id}", response_model=Documento)
def update_documento(documento_id: int, documento: DocumentoUpdate, db: Session = Depends(get_db)):
    db_documento = db.query(DocumentoModel).filter(DocumentoModel.id == documento_id).first()
    if not db_documento:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    update_data = documento.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_documento, key, value)
    db.commit()
    db.refresh(db_documento)
    return db_documento

@router.delete("/{documento_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_documento(documento_id: int, db: Session = Depends(get_db)):
    db_documento = db.query(DocumentoModel).filter(DocumentoModel.id == documento_id).first()
    if not db_documento:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    db.delete(db_documento)
    db.commit()
    return None
