from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database import Base

class TipoDocumento(str, enum.Enum):
    FEIN = "FEIN"
    FIAE = "FIAE"
    TASACION = "TASACION"
    NOTA_SIMPLE = "NOTA_SIMPLE"
    IBI = "IBI"
    CERT_ENERGETICO = "CERT_ENERGETICO"
    DNI = "DNI"
    ESCRITURA = "ESCRITURA"
    OTROS = "OTROS"

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    operacion_id = Column(Integer, ForeignKey("operaciones.id", ondelete="CASCADE"), nullable=False)
    nombre = Column(String, nullable=False)
    tipo = Column(SQLEnum(TipoDocumento), nullable=False)
    fecha_subida = Column(DateTime(timezone=True), server_default=func.now())
    fecha_caducidad = Column(DateTime(timezone=True))
    valido = Column(Boolean, default=True)
    ruta_archivo = Column(String)

    operacion = relationship("Operacion", back_populates="documentos")
