from typing import List
from app.models.operacion import TipoOperacion
from app.schemas.checklist import ChecklistItemCreate   # ✅ IMPORT CORRECTO

def generar_items_por_operacion(tipo_operacion: TipoOperacion) -> List[ChecklistItemCreate]:
    """
    Genera los items de checklist según el tipo de operación hipotecaria.
    Devuelve objetos ChecklistItemCreate (Pydantic), compatibles con seed_data.py.
    """

    if tipo_operacion == TipoOperacion.HIPOTECA:
        return [
            ChecklistItemCreate(descripcion="FEIN firmada", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="FIAE firmada (Acta previa notarial)", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Tasación válida", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Seguro de hogar", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Nota simple actualizada", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="DNI vigente de los titulares", requerido_para_firma=True),
        ]

    if tipo_operacion == TipoOperacion.COMPRAVENTA:
        return [
            ChecklistItemCreate(descripcion="Contrato de arras", requerido_para_firma=False),
            ChecklistItemCreate(descripcion="Nota simple actualizada", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="DNI vigente de compradores/vendedores", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Certificado energético", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Último recibo de IBI", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Certificado de comunidad de propietarios", requerido_para_firma=True),
        ]

    if tipo_operacion == TipoOperacion.CANCELACION:
        return [
            ChecklistItemCreate(descripcion="Certificado de deuda cero", requerido_para_firma=True),
            ChecklistItemCreate(descripcion="Provisión de fondos", requerido_para_firma=True),
        ]

    # Default para operaciones no definidas
    return [
        ChecklistItemCreate(descripcion="Documentación básica de la operación", requerido_para_firma=True)
    ]
