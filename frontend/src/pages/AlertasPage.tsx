import { ExclamationTriangleIcon } from '@heroicons/react/24/outline';

export default function AlertasPage() {
  return (
    <div className="space-y-6 animate-fade-in-up">
      <div className="sm:flex sm:items-center sm:justify-between mb-8">
        <div>
          <h2 className="text-3xl font-bold tracking-tight text-critical-main flex items-center gap-2">
            <ExclamationTriangleIcon className="h-8 w-8" />
            Centro de Alertas LCCI
          </h2>
          <p className="mt-2 text-sm text-gray-500">
            Monitoreo de caducidades documentales y violaciones de plazos legales.
          </p>
        </div>
      </div>
      <div className="bg-critical-50/50 backdrop-blur-md rounded-2xl border border-dashed border-critical-200 h-64 flex items-center justify-center text-critical-main/60 font-medium shadow-sm">
         En construcción - Panel Integral de Alertas Próximamente
      </div>
    </div>
  );
}
