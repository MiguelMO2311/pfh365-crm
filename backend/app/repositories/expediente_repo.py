from sqlalchemy.orm import Session
from app.models.expediente import Expediente
from app.schemas.expediente import ExpedienteCreate, ExpedienteUpdate
from app.repositories.base import CRUDBase
from typing import Optional

class CRUDExpediente(CRUDBase[Expediente, ExpedienteCreate, ExpedienteUpdate]):
    def get_by_numero(self, db: Session, numero: str) -> Optional[Expediente]:
        return db.query(self.model).filter(self.model.numero_expediente == numero).first()

expediente_repo = CRUDExpediente(Expediente)
