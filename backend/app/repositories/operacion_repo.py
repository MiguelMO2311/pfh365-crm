from sqlalchemy.orm import Session
from typing import List
from app.models.operacion import Operacion
from app.schemas.operacion import OperacionCreate, OperacionUpdate
from app.repositories.base import CRUDBase

class CRUDOperacion(CRUDBase[Operacion, OperacionCreate, OperacionUpdate]):
    def get_by_expediente(self, db: Session, expediente_id: int) -> List[Operacion]:
        return db.query(self.model).filter(self.model.expediente_id == expediente_id).all()
        
    def create_with_expediente(self, db: Session, obj_in: OperacionCreate, expediente_id: int) -> Operacion:
        db_obj = self.model(**obj_in.model_dump(), expediente_id=expediente_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

operacion_repo = CRUDOperacion(Operacion)
