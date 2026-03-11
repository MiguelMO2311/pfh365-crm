from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.expediente import Expediente, ExpedienteCreate, ExpedienteUpdate
from app.schemas.alerta import Alerta
from app.repositories.expediente_repo import expediente_repo
from app.core.dependencies import get_current_active_user, RoleChecker
from app.models.usuario import Usuario
from app.services.audit_service import log_action

router = APIRouter(prefix="/expedientes", tags=["Expedientes"])

allow_write_roles = RoleChecker(["admin", "gestor", "supervisor"])
allow_read_roles = RoleChecker(["admin", "gestor", "supervisor", "lectura"])

@router.post("/", response_model=Expediente, status_code=status.HTTP_201_CREATED)
def create_expediente(
    expediente: ExpedienteCreate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(allow_write_roles)
):
    db_exp = expediente_repo.create(db=db, obj_in=expediente)
    log_action(db, accion="crear_expediente", entidad="Expediente", entidad_id=db_exp.id, usuario_id=current_user.id)
    return db_exp

@router.get("/", response_model=List[Expediente])
def read_expedientes(
    skip: int = 0, limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(allow_read_roles)
):
    return expediente_repo.get_multi(db, skip=skip, limit=limit)

@router.get("/{expediente_id}", response_model=Expediente)
def read_expediente(
    expediente_id: int, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(allow_read_roles)
):
    db_expediente = expediente_repo.get(db, id=expediente_id)
    if not db_expediente:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return db_expediente

@router.put("/{expediente_id}", response_model=Expediente)
def update_expediente(
    expediente_id: int, 
    expediente: ExpedienteUpdate, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(allow_write_roles)
):
    db_expediente = expediente_repo.get(db, id=expediente_id)
    if not db_expediente:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    
    updated_exp = expediente_repo.update(db=db, db_obj=db_expediente, obj_in=expediente)
    log_action(db, accion="actualizar_expediente", entidad="Expediente", entidad_id=expediente_id, usuario_id=current_user.id)
    return updated_exp

@router.delete("/{expediente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expediente(
    expediente_id: int, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(RoleChecker(["admin"])) # Only admin can delete
):
    db_expediente = expediente_repo.get(db, id=expediente_id)
    if not db_expediente:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    
    expediente_repo.remove(db=db, id=expediente_id)
    log_action(db, accion="eliminar_expediente", entidad="Expediente", entidad_id=expediente_id, usuario_id=current_user.id)
    return None

@router.get("/{expediente_id}/alertas", response_model=List[Alerta])
def get_alertas_expediente(
    expediente_id: int, 
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(allow_read_roles)
):
    db_expediente = expediente_repo.get(db, id=expediente_id)
    if not db_expediente:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return db_expediente.alertas
