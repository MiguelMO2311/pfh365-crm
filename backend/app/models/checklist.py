from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Checklist(Base):
    __tablename__ = "checklists"

    id = Column(Integer, primary_key=True, index=True)
    operacion_id = Column(Integer, ForeignKey("operaciones.id", ondelete="CASCADE"), nullable=False, unique=True)
    completado = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_completado = Column(DateTime(timezone=True))

    operacion = relationship("Operacion", back_populates="checklist")
    items = relationship("ChecklistItem", back_populates="checklist", cascade="all, delete-orphan")

class ChecklistItem(Base):
    __tablename__ = "checklist_items"

    id = Column(Integer, primary_key=True, index=True)
    checklist_id = Column(Integer, ForeignKey("checklists.id", ondelete="CASCADE"), nullable=False)
    descripcion = Column(String, nullable=False)
    completado = Column(Boolean, default=False)
    requerido_para_firma = Column(Boolean, default=True)

    checklist = relationship("Checklist", back_populates="items")
