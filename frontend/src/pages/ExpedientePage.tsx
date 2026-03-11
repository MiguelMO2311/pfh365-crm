import { DocumentCheckIcon, BuildingLibraryIcon, ShieldCheckIcon, DocumentPlusIcon, PlusIcon } from '@heroicons/react/24/outline';
import Card from '../components/ui/Card';
import StatusBadge from '../components/ui/StatusBadge';
import Timeline, { TimelineEvent } from '../components/ui/Timeline';

export default function ExpedientePage() {
  const expediente = {
    numero: 'EXP-2026-001',
    cliente: 'Juan Pérez',
    telefono: '600 123 456',
    estado: 'Prefirma',
    banco: 'Banco Santander',
    importe: '150.000 €',
    direccion: 'Calle Falsa 123, Madrid'
  };

  const checklist = [
    { id: 1, text: 'FEIN Firmada (Hace 12 días)', done: true, requerido: true },
    { id: 2, text: 'DNI Titulares', done: false, requerido: true, error: true },
    { id: 3, text: 'Tasación Válida', done: true, requerido: true },
    { id: 4, text: 'Seguro de Hogar', done: false, requerido: true },
  ];

  const timelineEvents: TimelineEvent[] = [
    { id: 1, type: 'creation', title: 'Expediente Creado', description: 'Creado por Gestor Principal', date: '01/03/2026' },
    { id: 2, type: 'document', title: 'FEIN Subida', description: 'Documento procesado correctamente', date: '02/03/2026' },
    { id: 3, type: 'alert', title: 'DNI Caducado detectado', description: 'Sistema LCCI ha bloqueado la viabilidad', date: 'Hoy', isActive: true },
  ];

  return (
    <div className="space-y-6 max-w-7xl mx-auto pb-12 animate-fade-in-up">
      {/* Header Profile Section */}
      <div className="bg-white/60 backdrop-blur-xl rounded-3xl p-8 border border-gray-100 shadow-sm relative overflow-hidden">
         <div className="absolute top-0 right-0 p-8 opacity-10">
            <BuildingLibraryIcon className="w-48 h-48 text-corporate-600 transform translate-x-12 -translate-y-12" />
         </div>

         <div className="relative z-10 md:flex md:items-center md:justify-between">
          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-4">
               <h2 className="text-3xl font-black tracking-tight text-gray-900">
                 {expediente.numero}
               </h2>
               <StatusBadge status={expediente.estado} className="text-sm px-3 py-1" />
            </div>
            <div className="mt-4 flex flex-col sm:flex-row sm:flex-wrap sm:space-x-8">
              <div className="flex items-center text-sm font-medium text-gray-600 bg-white/50 px-4 py-2 rounded-xl backdrop-blur-sm border border-gray-200/50">
                <span className="text-gray-400 mr-2">Cliente</span> {expediente.cliente} &middot; {expediente.telefono}
              </div>
              <div className="mt-2 sm:mt-0 flex items-center text-sm font-medium text-gray-600 bg-white/50 px-4 py-2 rounded-xl backdrop-blur-sm border border-gray-200/50">
                <BuildingLibraryIcon className="mr-2 h-5 w-5 flex-shrink-0 text-corporate-500" />
                {expediente.banco} <span className="text-gray-400 mx-2">|</span> {expediente.importe}
              </div>
            </div>
          </div>
          <div className="mt-6 flex md:ml-4 md:mt-0 space-x-3">
            <button type="button" className="btn btn-secondary text-critical-main hover:bg-critical-50 hover:border-critical-200 transition-colors">
              Bloquear
            </button>
            <button type="button" className="btn btn-primary bg-gradient-to-r from-corporate-500 to-corporate-600 shadow-corporate-500/30">
              Programar Notaría
            </button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
        {/* Left Col - Info y Operaciones */}
        <div className="lg:col-span-2 space-y-6">
          <Card noPadding>
            <div className="border-b border-gray-100/80 px-6 py-5 flex justify-between items-center bg-gray-50/30">
              <h3 className="text-lg font-bold text-gray-900">Estructura Operativa</h3>
              <button className="text-sm font-bold text-corporate-600 hover:text-corporate-700 transition-colors flex items-center gap-1">
                <PlusIcon className="w-4 h-4"/> Añadir
              </button>
            </div>
            <div className="p-2">
              {[ {id:1, tipo:'Hipoteca'}, {id:2, tipo:'Compraventa'} ].map((op) => (
                <div key={op.id} className="m-2 p-4 rounded-xl border border-gray-100 bg-white hover:border-corporate-200 hover:shadow-md transition-all group cursor-pointer flex items-center justify-between">
                   <div className="flex items-center gap-4">
                      <div className="h-12 w-12 rounded-xl bg-corporate-50 flex items-center justify-center group-hover:bg-corporate-100 transition-colors">
                        <DocumentCheckIcon className="h-6 w-6 text-corporate-600" />
                      </div>
                      <div>
                        <h4 className="font-bold text-gray-900">{op.tipo}</h4>
                        <p className="text-sm text-gray-500">En curso &middot; 0 cargas</p>
                      </div>
                   </div>
                   <div className="h-8 w-8 rounded-full bg-gray-50 flex items-center justify-center group-hover:bg-corporate-50 transition-colors text-gray-400 group-hover:text-corporate-600">
                      &rarr;
                   </div>
                </div>
              ))}
            </div>
          </Card>

          <Card>
            <h3 className="text-lg font-bold text-gray-900 mb-6">Historial y Timeline</h3>
            <Timeline events={timelineEvents} />
          </Card>
        </div>

        {/* Right Col - Checklist Inteligente */}
        <div className="col-span-1 space-y-6">
          <Card noPadding className="border-0 shadow-lg ring-1 ring-black/5">
            <div className="bg-gradient-to-b from-corporate-800 to-corporate-950 px-6 py-6 text-white text-center">
              <ShieldCheckIcon className="h-10 w-10 mx-auto text-corporate-300 mb-2" />
              <h3 className="text-lg font-bold">Viabilidad LCCI</h3>
              <p className="text-corporate-200 text-sm mt-1">2/4 Requisitos completados</p>
            </div>
            <div className="p-6 bg-white">
              <ul className="space-y-4">
                {checklist.map((item) => (
                  <li key={item.id} className="flex items-start gap-3 group">
                    <div className="flex h-6 items-center">
                      <input
                        type="checkbox"
                        checked={item.done}
                        readOnly
                        className="h-5 w-5 rounded-md border-gray-300 text-corporate-600 focus:ring-corporate-600 cursor-not-allowed bg-gray-50 transition-all"
                      />
                    </div>
                    <div className="text-sm leading-6 flex-1">
                      <label className={`font-medium transition-colors ${item.error ? 'text-critical-main' : item.done ? 'text-gray-900' : 'text-gray-500'}`}>
                        {item.text} {item.requerido && <span className="text-critical-main ml-0.5" title="Requerido">*</span>}
                      </label>
                      {item.error && <p className="text-critical-main/90 text-xs mt-1 font-medium bg-critical-50 p-2 rounded border border-critical-100">Carga nuevo documento urgente.</p>}
                    </div>
                  </li>
                ))}
              </ul>
              
              <div className="mt-8">
                <button className="w-full btn btn-secondary flex justify-center gap-2 items-center bg-gray-50 hover:bg-gray-100 border-dashed border-2 border-gray-300">
                  <DocumentPlusIcon className="w-5 h-5 text-gray-400" />
                  <span className="text-gray-600 font-semibold">Subir Documento</span>
                </button>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
