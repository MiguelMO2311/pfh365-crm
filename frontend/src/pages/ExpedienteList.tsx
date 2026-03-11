import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { PlusIcon, FunnelIcon, MagnifyingGlassIcon } from '@heroicons/react/20/solid';
import DataTable from '../components/ui/DataTable';
import StatusBadge from '../components/ui/StatusBadge';
import { apiClient } from '../services/apiCore';

export default function ExpedienteList() {
  const navigate = useNavigate();
  const [expedientes, setExpedientes] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchExpedientes = async () => {
      try {
        const response = await apiClient.get('/expedientes/?skip=0&limit=100');
        setExpedientes(response.data);
      } catch (error) {
        console.error("Error fetching expedientes:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchExpedientes();
  }, []);

  const columns = [
    { key: 'numero_expediente', header: 'Expediente', render: (item: any) => <span className="font-semibold text-corporate-600">{item.numero_expediente}</span> },
    { key: 'cliente_nombre', header: 'Cliente' },
    { key: 'estado', header: 'Estado', render: (item: any) => <StatusBadge status={item.estado} /> },
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

      {loading ? (
        <div className="flex justify-center p-12">
          <div className="w-8 h-8 border-4 border-corporate-200 border-t-corporate-600 rounded-full animate-spin"></div>
        </div>
      ) : (
        <DataTable 
          data={expedientes} 
          columns={columns} 
          keyExtractor={(item) => item.id}
          onRowClick={(item) => navigate(`/expedientes/${item.id}`)}
        />
      )}
    </div>
  );
}
