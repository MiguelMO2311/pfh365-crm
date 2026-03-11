from sqlalchemy import Column, Integer, String, Float, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class EstadoExpediente(str, enum.Enum):
    PREFIRMA = "prefirma"
    FIRMA_PROGRAMADA = "firma_programada"
    FIRMADA = "firmada"
    ARCHIVADO = "archivado"

class Expediente(Base):
    __tablename__ = "expedientes"

    id = Column(Integer, primary_key=True, index=True)
    numero_expediente = Column(String, unique=True, index=True, nullable=False)
    cliente_nombre = Column(String, nullable=False)
    cliente_dni = Column(String, nullable=False)
    telefono = Column(String)
    email = Column(String)
    direccion_inmueble = Column(String)
    banco = Column(String)
    importe_hipoteca = Column(Float)
    estado_expediente = Column(SQLEnum(EstadoExpediente), default=EstadoExpediente.PREFIRMA)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_prevista_firma = Column(DateTime(timezone=True))
    fecha_firma_real = Column(DateTime(timezone=True))

    operaciones = relationship("Operacion", back_populates="expediente", cascade="all, delete-orphan")
    alertas = relationship("Alerta", back_populates="expediente", cascade="all, delete-orphan")
