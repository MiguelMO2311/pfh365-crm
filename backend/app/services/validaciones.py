from datetime import datetime, timedelta
from app.models.documento import Documento, TipoDocumento
from typing import List

def check_fein_plazo_legal(documentos: List[Documento], fecha_firma: datetime) -> bool:
    """Valida si la FEIN se entregó con el plazo legal de LCCI (10 días en España, 14 en Cataluña)"""
    fein = next((doc for doc in documentos if doc.tipo == TipoDocumento.FEIN and doc.valido), None)
    if not fein or not fecha_firma:
        return False
    # Simplificación: 10 días naturales (lo ideal son días naturales o hábiles según CCAA)
    dias_transcurridos = (fecha_firma - fein.fecha_subida).days
    return dias_transcurridos >= 10

def check_documentos_caducados(documentos: List[Documento]) -> List[Documento]:
    """Devuelve la lista de documentos que están caducados"""
    hoy = datetime.now(datetime.now().astimezone().tzinfo)
    return [doc for doc in documentos if doc.fecha_caducidad and doc.fecha_caducidad < hoy and doc.valido]

def check_acta_previa(documentos: List[Documento], fecha_firma: datetime) -> bool:
    """Valida que el acta previa (FIAE) se haya firmado al menos 1 día antes"""
    fiae = next((doc for doc in documentos if doc.tipo == TipoDocumento.FIAE and doc.valido), None)
    if not fiae or not fecha_firma:
        return False
    return fiae.fecha_subida < fecha_firma - timedelta(days=1)
