import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowUpRightIcon, ArrowDownRightIcon, DocumentTextIcon, CheckBadgeIcon, ExclamationTriangleIcon, BuildingLibraryIcon, ChartBarIcon } from '@heroicons/react/24/outline';
import Card from '../components/ui/Card';
import { apiClient } from '../services/apiCore';

interface DashboardStats {
  expedientes_totales: number;
  operaciones_curso: number;
  firmas_proximas: number;
  alertas_activas: number;
}

export default function DashboardPage() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const response = await apiClient.get('/dashboard/stats');
        setStats(response.data);
      } catch (error) {
        console.error("Error fetching dashboard stats:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboard();
  }, []);

  const statCards = [
    { name: 'Expedientes Totales', stat: stats?.expedientes_totales ?? '-', icon: DocumentTextIcon, link: '/expedientes', change: '12%', changeType: 'increase', color: 'from-blue-500 to-corporate-600' },
    { name: 'Operaciones Curso', stat: stats?.operaciones_curso ?? '-', icon: BuildingLibraryIcon, link: '/operaciones', change: '8', changeType: 'increase', color: 'from-indigo-500 to-purple-600' },
    { name: 'Firmas < 7 Días', stat: stats?.firmas_proximas ?? '-', icon: CheckBadgeIcon, link: '/expedientes', change: '3', changeType: 'increase', color: 'from-emerald-500 to-emerald-600' },
    { name: 'Alertas LCCI', stat: stats?.alertas_activas ?? '-', icon: ExclamationTriangleIcon, link: '/alertas', change: '2', changeType: 'decrease', color: 'from-red-500 to-critical-main' },
  ];

  if (loading) {
    return (
      <div className="flex items-center justify-center p-20">
         <div className="w-12 h-12 border-4 border-corporate-200 border-t-corporate-600 rounded-full animate-spin"></div>
      </div>
    );
  }

  return (
    <div className="animate-fade-in-up -mx-4 sm:-mx-6 lg:-mx-8 -mt-28">
      
      {/* Premium Hero Section */}
      <div 
        className="relative bg-corporate-900 border-b border-corporate-800 pt-36 pb-32 px-4 sm:px-6 lg:px-8 overflow-hidden"
        style={{
          backgroundImage: 'url(/assets/images/dashboard-bg.png)',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundBlendMode: 'overlay'
        }}
      >
        <div className="absolute inset-0 bg-gradient-to-b from-transparent to-gray-900/90 mix-blend-multiply" />
        <div className="absolute inset-0 bg-gradient-to-r from-corporate-900/80 to-transparent" />
        
        <div className="relative z-10 max-w-7xl mx-auto">
           <h1 className="text-4xl md:text-5xl lg:text-6xl font-black text-white tracking-tight drop-shadow-md">
             Centro de Control <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-corporate-400">PFH365</span>
           </h1>
           <p className="mt-4 text-lg md:text-xl text-gray-300 font-medium max-w-2xl drop-shadow-sm">
             Visión panorámica de toda la actividad hipotecaria, rendimiento de operaciones y monitoreo de riesgos LCCI en tiempo real.
           </p>
        </div>
      </div>

      {/* Main Content Area */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 -mt-16 relative z-20 pb-12">
        
        {/* Large Clickable Metric Cards */}
        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {statCards.map((item) => (
            <Link key={item.name} to={item.link} className="block group">
              <Card className="relative overflow-hidden h-full transform transition-all duration-300 hover:scale-[1.03] hover:-translate-y-2 border-white/40 shadow-xl bg-white/90 backdrop-blur-xl">
                
                {/* Decorative background circle */}
                <div className={`absolute -right-6 -top-6 w-24 h-24 bg-gradient-to-br ${item.color} rounded-full opacity-10 group-hover:scale-150 transition-transform duration-500`} />
                
                <dt className="flex items-center gap-4 mb-4">
                  <div className={`p-3 rounded-2xl bg-gradient-to-br ${item.color} shadow-lg shadow-gray-200`}>
                    <item.icon className="h-7 w-7 text-white" aria-hidden="true" />
                  </div>
                  <p className="text-base font-bold text-gray-600 truncate">{item.name}</p>
                </dt>
                
                <dd className="flex items-end justify-between">
                  <p className="text-5xl font-black text-gray-900 tracking-tight">{item.stat}</p>
                  
                  <div className="flex flex-col items-end">
                    <p
                      className={`flex items-center text-sm font-bold px-2.5 py-1 rounded-full ${
                        item.changeType === 'increase' ? 'bg-success-50 text-success-main' : 'bg-critical-50 text-critical-main'
                      }`}
                    >
                      {item.changeType === 'increase' ? (
                        <ArrowUpRightIcon className="h-4 w-4 mr-1 stroke-2" aria-hidden="true" />
                      ) : (
                        <ArrowDownRightIcon className="h-4 w-4 mr-1 stroke-2" aria-hidden="true" />
                      )}
                      {item.change}
                    </p>
                    <span className="text-xs text-gray-400 font-medium mt-1 group-hover:text-corporate-500 transition-colors flex items-center gap-1">
                      Ver detalles &rarr;
                    </span>
                  </div>
                </dd>
              </Card>
            </Link>
          ))}
        </div>
        
        {/* Big Dashboard Sections */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mt-10">
          <div className="lg:col-span-2">
            <Card className="h-[450px] flex flex-col pt-8 px-8 bg-white/90 shadow-xl border-gray-100 hover:shadow-2xl transition-all">
              <h3 className="text-2xl font-bold text-gray-900 mb-2">Volumen de Expedientes</h3>
              <p className="text-gray-500 font-medium">Histórico de firmas completadas en los últimos 6 meses</p>
              
              <div className="flex-1 mt-8 rounded-xl border-2 border-dashed border-gray-200 flex items-center justify-center bg-gray-50/50 mb-8 overflow-hidden relative group">
                <div className="absolute inset-0 bg-gradient-to-r from-corporate-500/5 to-purple-500/5" />
                <span className="text-gray-400 font-bold text-lg flex items-center gap-2 relative z-10">
                   <ChartBarIcon className="w-6 h-6"/> Gráfica Recharts Premium (Próximamente)
                </span>
              </div>
            </Card>
          </div>

          <div className="lg:col-span-1">
             <Card className="h-[450px] flex flex-col p-0 overflow-hidden shadow-xl border-gray-100 hover:shadow-2xl transition-all border-t-4 border-t-critical-main">
                <div className="p-6 border-b border-gray-100 bg-gray-50/50">
                  <h3 className="text-xl font-bold text-gray-900 flex items-center gap-2">
                    <ExclamationTriangleIcon className="w-6 h-6 text-critical-main" />
                    Atención Requerida
                  </h3>
                </div>
                <div className="flex-1 w-full bg-white divide-y divide-gray-100 overflow-y-auto">
                    {stats?.alertas_activas && stats.alertas_activas > 0 ? (
                      [1, 2, 3].map((i) => (
                        <Link key={i} to={`/expedientes/${i}`} className="block p-5 hover:bg-gray-50 transition-colors">
                          <div className="flex justify-between items-start mb-1">
                             <span className="font-bold text-corporate-600">EXP-2026-00{i}</span>
                             <span className="text-xs font-bold text-critical-main bg-critical-50 px-2 py-0.5 rounded text-center">DNI Cad.</span>
                          </div>
                          <p className="text-sm text-gray-600 font-medium mb-2">Juan Pérez García</p>
                          <p className="text-xs text-gray-400">Bloqueado por sistema LCCI. Requiere actualización.</p>
                        </Link>
                      ))
                    ) : (
                      <div className="p-10 text-center text-gray-500">
                        No hay alertas activas
                      </div>
                    )}
                </div>
             </Card>
          </div>
        </div>
      </div>

    </div>
  );
}
