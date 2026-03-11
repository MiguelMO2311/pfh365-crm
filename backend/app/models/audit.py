from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="SET NULL"), nullable=True)
    accion = Column(String, nullable=False) # ej: "expediente_creado"
    entidad = Column(String, nullable=False) # ej: "Expediente"
    entidad_id = Column(Integer, nullable=True)
    detalles = Column(String, nullable=True)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
