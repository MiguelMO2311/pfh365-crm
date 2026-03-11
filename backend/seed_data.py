import sys
import os
from datetime import datetime, timedelta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, engine, Base
from app.models.expediente import Expediente, EstadoExpediente
from app.models.operacion import Operacion, TipoOperacion, EstadoOperacion
from app.models.carga import Carga, TipoCarga, EstadoCarga
from app.models.documento import Documento, TipoDocumento
from app.models.alerta import Alerta, TipoAlerta, PrioridadAlerta
from app.services.checklist_generator import generar_items_por_operacion
from app.models.checklist import Checklist, ChecklistItem

def seed_db():
    print("Creating tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    print("Generating seed data...")
    # Expediente 1
    exp1 = Expediente(
        numero_expediente="EXP-2026-001",
        cliente_nombre="Juan Pérez",
        cliente_dni="12345678A",
        telefono="600123456",
        email="juan.perez@example.com",
        direccion_inmueble="Calle Falsa 123, Madrid",
        banco="Banco Santander",
        importe_hipoteca=150000.0,
        estado_expediente=EstadoExpediente.PREFIRMA,
        fecha_prevista_firma=datetime.now() + timedelta(days=5)
    )
    db.add(exp1)
    db.commit()
    db.refresh(exp1)

    # Operacion 1: Hipoteca
    op1 = Operacion(
        expediente_id=exp1.id,
        tipo_operacion=TipoOperacion.HIPOTECA,
        estado=EstadoOperacion.EN_CURSO,
        fecha_prevista_firma=exp1.fecha_prevista_firma
    )
    db.add(op1)
    db.commit()
    db.refresh(op1)

    # Checklist for Operacion 1
    chk1 = Checklist(operacion_id=op1.id)
    db.add(chk1)
    db.commit()
    db.refresh(chk1)
    items = generar_items_por_operacion(op1.tipo_operacion)
    for i, item in enumerate(items):
        db_item = ChecklistItem(checklist_id=chk1.id, descripcion=item.descripcion, requerido_para_firma=item.requerido_para_firma, completado=bool(i%2))
        db.add(db_item)
    db.commit()

    # Operacion 2: Compraventa
    op2 = Operacion(
        expediente_id=exp1.id,
        tipo_operacion=TipoOperacion.COMPRAVENTA,
        estado=EstadoOperacion.EN_CURSO,
        fecha_prevista_firma=exp1.fecha_prevista_firma
    )
    db.add(op2)
    db.commit()
    
    # Documentos
    doc1 = Documento(
        operacion_id=op1.id,
        nombre="FEIN_JuanPerez.pdf",
        tipo=TipoDocumento.FEIN,
        valido=True,
        fecha_subida=datetime.now() - timedelta(days=12)
    )
    db.add(doc1)

    doc2 = Documento(
        operacion_id=op1.id,
        nombre="DNI_JuanPerez_Caducado.pdf",
        tipo=TipoDocumento.DNI,
        valido=True,
        fecha_caducidad=datetime.now() - timedelta(days=10)
    )
    db.add(doc2)

    # Cargas
    carga1 = Carga(
        operacion_id=op2.id,
        tipo_carga=TipoCarga.HIPOTECA,
        descripcion="Hipoteca previa con BBVA",
        estado=EstadoCarga.VIGENTE,
        genera_operacion_adicional=True
    )
    db.add(carga1)
    db.commit()
    
    # Alertas
    alerta1 = Alerta(
        expediente_id=exp1.id,
        tipo=TipoAlerta.DOC_CADUCADO,
        prioridad=PrioridadAlerta.CRITICA,
        mensaje="DNI caducado para el titular."
    )
    alerta2 = Alerta(
        expediente_id=exp1.id,
        tipo=TipoAlerta.FIRMA_PROXIMA,
        prioridad=PrioridadAlerta.ALTA,
        mensaje="Firma de hipoteca en 5 días."
    )
    db.add(alerta1)
    db.add(alerta2)
    db.commit()
    
    print("Seed data completed (1 expediente generated for demo). Run script again to configure more or test.")
    db.close()

if __name__ == "__main__":
    seed_db()
