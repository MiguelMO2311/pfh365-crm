from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class TipoCarga(str, enum.Enum):
    HIPOTECA = "HIPOTECA"
    CONDICION_RESOLUTORIA = "CONDICION_RESOLUTORIA"
    EMBARGO = "EMBARGO"
    AFECCION = "AFECCION"
    OTROS = "OTROS"

class EstadoCarga(str, enum.Enum):
    VIGENTE = "vigente"
    EN_CANCELACION = "en_cancelacion"
    CANCELADA = "cancelada"

class Carga(Base):
    __tablename__ = "cargas"

    id = Column(Integer, primary_key=True, index=True)
    operacion_id = Column(Integer, ForeignKey("operaciones.id", ondelete="CASCADE"), nullable=False)
    tipo_carga = Column(SQLEnum(TipoCarga), nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(SQLEnum(EstadoCarga), default=EstadoCarga.VIGENTE)
    genera_operacion_adicional = Column(Boolean, default=False)

    operacion = relationship("Operacion", back_populates="cargas")
