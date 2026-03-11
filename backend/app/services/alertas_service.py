from sqlalchemy.orm import Session
from app.models.alerta import Alerta, TipoAlerta, PrioridadAlerta
from app.models.expediente import Expediente, EstadoExpediente
from app.services.validaciones import check_documentos_caducados
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def generar_alerta(db: Session, expediente_id: int, tipo: TipoAlerta, prioridad: PrioridadAlerta, mensaje: str):
    # Evitar duplicados no resueltos
    alerta_existente = db.query(Alerta).filter(
        Alerta.expediente_id == expediente_id,
        Alerta.tipo == tipo,
        Alerta.resuelta == False
    ).first()
    
    if not alerta_existente:
        nueva_alerta = Alerta(
            expediente_id=expediente_id,
            tipo=tipo,
            prioridad=prioridad,
            mensaje=mensaje
        )
        db.add(nueva_alerta)
        db.commit()
        logger.info(f"Alerta generada para expediente {expediente_id}: {mensaje}")

def revisar_alertas_sistema(db: Session):
    """Revisa todos los expedientes para generar alertas automáticas."""
    expedientes_activos = db.query(Expediente).filter(
        Expediente.estado_expediente.in_([EstadoExpediente.PREFIRMA, EstadoExpediente.FIRMA_PROGRAMADA])
    ).all()
    
    hoy = datetime.now(datetime.now().astimezone().tzinfo)
    
    for exp in expedientes_activos:
        # Validar fechas próximas a firma (7 días)
        if exp.fecha_prevista_firma:
            dias_para_firma = (exp.fecha_prevista_firma - hoy).days
            if 0 <= dias_para_firma <= 7:
                generar_alerta(
                    db, exp.id, TipoAlerta.FIRMA_PROXIMA, PrioridadAlerta.ALTA,
                    f"Firma próxima en {dias_para_firma} días."
                )
        
        # Validar expediente parado (más de 30 días sin cambios en fecha de actualización si la tuviéramos,
        # simplificaremos a días desde creación)
        dias_desde_creacion = (hoy - exp.fecha_creacion).days
        if dias_desde_creacion > 30 and exp.estado_expediente == EstadoExpediente.PREFIRMA:
            generar_alerta(
                 db, exp.id, TipoAlerta.EXPEDIENTE_PARADO, PrioridadAlerta.MEDIA,
                 f"Expediente parado por más de 30 días en prefirma."
            )
        
        # Revisar documentos caducados en cada operación
        for op in exp.operaciones:
            docs_caducados = check_documentos_caducados(op.documentos)
            if docs_caducados:
                nombres_docs = ", ".join([d.nombre for d in docs_caducados])
                generar_alerta(
                    db, exp.id, TipoAlerta.DOC_CADUCADO, PrioridadAlerta.CRITICA,
                    f"Documentos caducados encontrados en operación {op.id}: {nombres_docs}"
                )
