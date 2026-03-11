import { useNavigate } from 'react-router-dom';
import { PlusIcon, FunnelIcon, MagnifyingGlassIcon } from '@heroicons/react/20/solid';
import DataTable from '../components/ui/DataTable';
import StatusBadge from '../components/ui/StatusBadge';

const expedientes = [
  { id: 1, numero: 'EXP-2026-001', cliente: 'Juan Pérez', tipo: 'Hipoteca + Compraventa', estado: 'Firma Programada', fecha: '12/03/2026' },
  { id: 2, numero: 'EXP-2026-002', cliente: 'María López', tipo: 'Hipoteca', estado: 'Prefirma', fecha: 'Pendiente' },
  { id: 3, numero: 'EXP-2026-003', cliente: 'Carlos Sainz', tipo: 'Cancelación', estado: 'En Curso', fecha: '28/02/2026' },
  { id: 4, numero: 'EXP-2026-004', cliente: 'Ana García', tipo: 'Compraventa', estado: 'Firmado', fecha: '01/03/2026' },
  { id: 5, numero: 'EXP-2026-005', cliente: 'Luis Torres', tipo: 'Hipoteca', estado: 'Bloqueado', fecha: 'Pendiente' },
];

export default function ExpedientesListPage() {
  const navigate = useNavigate();

  const columns = [
    { key: 'numero', header: 'Expediente', render: (item: any) => <span className="font-semibold text-corporate-600">{item.numero}</span> },
    { key: 'cliente', header: 'Cliente' },
    { key: 'tipo', header: 'Operación' },
    { key: 'estado', header: 'Estado', render: (item: any) => <StatusBadge status={item.estado} /> },
    { key: 'fecha', header: 'Fecha Firma' },
  ];

  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="sm:flex sm:items-center sm:justify-between mb-8">
        <div>
          <h2 className="text-3xl font-bold tracking-tight text-gray-900">
            Expedientes Activos
          </h2>
          <p className="mt-2 text-sm text-gray-500">
            Gestión de expedientes hipotecarios, compraventas y cancelaciones.
          </p>
        </div>
        <div className="mt-4 sm:ml-16 sm:mt-0 sm:flex-none flex gap-3">
          <div className="relative rounded-md shadow-sm">
            <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
              <MagnifyingGlassIcon className="h-5 w-5 text-gray-400" aria-hidden="true" />
            </div>
            <input
              type="text"
              name="search"
              id="search"
              className="block w-full rounded-lg border-0 py-2 pl-10 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-corporate-500 sm:text-sm sm:leading-6"
              placeholder="Buscar cliente, número..."
            />
          </div>
          <button type="button" className="btn btn-secondary gap-2">
            <FunnelIcon className="h-4 w-4 text-gray-400" />
          </button>
          <button type="button" className="btn btn-primary gap-2">
            <PlusIcon className="h-5 w-5" /> Nuevo
          </button>
        </div>
      </div>

      <DataTable 
        data={expedientes} 
        columns={columns} 
        keyExtractor={(item) => item.id}
        onRowClick={(item) => navigate(`/expedientes/${item.id}`)}
      />
    </div>
  );
}
