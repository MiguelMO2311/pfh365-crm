from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base

class TipoAlerta(str, enum.Enum):
    PLAZO_LCCI = "plazo_lcci"
    DOC_CADUCADO = "doc_caducado"
    CARGA_PENDIENTE = "carga_pendiente"
    FIRMA_PROXIMA = "firma_proxima"
    EXPEDIENTE_PARADO = "expediente_parado"

class PrioridadAlerta(str, enum.Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"
    CRITICA = "critica"

class Alerta(Base):
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    expediente_id = Column(Integer, ForeignKey("expedientes.id", ondelete="CASCADE"), nullable=True)
    tipo = Column(SQLEnum(TipoAlerta), nullable=False)
    prioridad = Column(SQLEnum(PrioridadAlerta), default=PrioridadAlerta.MEDIA)
    mensaje = Column(String, nullable=False)
    resuelta = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_resolucion = Column(DateTime(timezone=True))

    expediente = relationship("Expediente", back_populates="alertas")
