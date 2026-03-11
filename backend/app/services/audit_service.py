from sqlalchemy.orm import Session
from app.models.audit import AuditLog
from typing import Optional

def log_action(db: Session, accion: str, entidad: str, entidad_id: Optional[int] = None, detalles: Optional[str] = None, usuario_id: Optional[int] = None):
    audit_entry = AuditLog(
        usuario_id=usuario_id,
        accion=accion,
        entidad=entidad,
        entidad_id=entidad_id,
        detalles=detalles
    )
    db.add(audit_entry)
    db.commit()
    db.refresh(audit_entry)
    return audit_entry
