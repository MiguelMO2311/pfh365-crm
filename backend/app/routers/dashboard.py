from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db

from app.models.expediente import Expediente, EstadoExpediente
from app.models.operacion import Operacion, EstadoOperacion
from app.models.alerta import Alerta, PrioridadAlerta

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/metrics")
def get_dashboard_metrics(db: Session = Depends(get_db)):
    # 1. Expedientes por estado
    expedientes_estado = db.query(Expediente.estado_expediente, func.count(Expediente.id)).group_by(Expediente.estado_expediente).all()
    expedientes_resumen = {str(estado.value): count for estado, count in expedientes_estado}

    # 2. Operaciones por tipo
    operaciones_tipo = db.query(Operacion.tipo_operacion, func.count(Operacion.id)).group_by(Operacion.tipo_operacion).all()
    operaciones_resumen = {str(tipo.value): count for tipo, count in operaciones_tipo}

    # 3. Próximas firmas
    proximas_firmas = db.query(Expediente).filter(
        Expediente.estado_expediente == EstadoExpediente.FIRMA_PROGRAMADA
    ).order_by(Expediente.fecha_prevista_firma.asc()).limit(5).all()

    proximas_firmas_resumen = [{"id": exp.id, "numero": exp.numero_expediente, "cliente": exp.cliente_nombre, "fecha": exp.fecha_prevista_firma} for exp in proximas_firmas if exp.fecha_prevista_firma]

    # 4. Alertas Críticas
    alertas_criticas = db.query(Alerta).filter(
        Alerta.prioridad == PrioridadAlerta.CRITICA,
        Alerta.resuelta == False
    ).limit(5).all()

    alertas_criticas_resumen = [{"id": a.id, "expediente_id": a.expediente_id, "mensaje": a.mensaje, "tipo": a.tipo} for a in alertas_criticas]

    return {
        "expedientes_por_estado": expedientes_resumen,
        "operaciones_por_tipo": operaciones_resumen,
        "proximas_firmas": proximas_firmas_resumen,
        "alertas_criticas": alertas_criticas_resumen,
        "total_expedientes": db.query(Expediente).count()
    }
