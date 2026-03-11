from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base

class TipoOperacion(str, enum.Enum):
    HIPOTECA = "HIPOTECA"
    COMPRAVENTA = "COMPRAVENTA"
    CANCELACION = "CANCELACION"
    CONDICION_RESOLUTORIA = "CONDICION_RESOLUTORIA"
    EMBARGO = "EMBARGO"
    HERENCIA = "HERENCIA"
    TASACION = "TASACION"

class EstadoOperacion(str, enum.Enum):
    PENDIENTE = "pendiente"
    EN_CURSO = "en_curso"
    FINALIZADA = "finalizada"
    CANCELADA = "cancelada"

class Operacion(Base):
    __tablename__ = "operaciones"

    id = Column(Integer, primary_key=True, index=True)
    expediente_id = Column(Integer, ForeignKey("expedientes.id", ondelete="CASCADE"), nullable=False)
    tipo_operacion = Column(SQLEnum(TipoOperacion), nullable=False)
    estado = Column(SQLEnum(EstadoOperacion), default=EstadoOperacion.PENDIENTE)
    fecha_inicio = Column(DateTime(timezone=True), server_default=func.now())
    fecha_prevista_firma = Column(DateTime(timezone=True))
    fecha_firma_real = Column(DateTime(timezone=True))
    observaciones = Column(String)

    expediente = relationship("Expediente", back_populates="operaciones")
    cargas = relationship("Carga", back_populates="operacion", cascade="all, delete-orphan")
    documentos = relationship("Documento", back_populates="operacion", cascade="all, delete-orphan")
    checklist = relationship("Checklist", back_populates="operacion", cascade="all, delete-orphan", uselist=False)
