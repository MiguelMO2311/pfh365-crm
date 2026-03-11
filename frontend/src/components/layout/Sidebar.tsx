import { Link, useLocation } from 'react-router-dom';
import { 
  HomeIcon, 
  FolderOpenIcon, 
  ChartBarIcon, 
  Cog6ToothIcon 
} from '@heroicons/react/24/outline';
import { clsx } from 'clsx';

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: HomeIcon },
  { name: 'Expedientes', href: '/expedientes', icon: FolderOpenIcon },
  { name: 'Reportes', href: '#', icon: ChartBarIcon },
  { name: 'Ajustes', href: '#', icon: Cog6ToothIcon },
];

export default function Sidebar() {
  const location = useLocation();

  return (
    <div className="flex h-full w-64 flex-col bg-corporate-900 shadow-xl border-r border-corporate-800">
      <div className="flex h-16 shrink-0 items-center px-6 border-b border-corporate-800 bg-corporate-900/50 backdrop-blur-sm">
        <h1 className="text-xl font-bold text-white tracking-widest flex items-center gap-2">
          <span className="bg-corporate-500 rounded text-white p-1 text-xs">PFH</span>
          365 CRM
        </h1>
      </div>
      <div className="flex flex-1 flex-col overflow-y-auto">
        <nav className="flex-1 space-y-1 px-4 py-6">
          {navigation.map((item) => {
            const current = location.pathname.startsWith(item.href) && item.href !== '#';
            return (
              <Link
                key={item.name}
                to={item.href}
                className={clsx(
                  current
                    ? 'bg-corporate-800 text-white shadow-inner'
                    : 'text-corporate-200 hover:bg-corporate-800/50 hover:text-white',
                  'group flex items-center rounded-lg px-3 py-2.5 text-sm font-medium transition-all duration-200'
                )}
              >
                <item.icon
                  className={clsx(
                    current ? 'text-white' : 'text-corporate-300 group-hover:text-white',
                    'mr-3 h-5 w-5 flex-shrink-0 transition-colors duration-200'
                  )}
                  aria-hidden="true"
                />
                {item.name}
              </Link>
            );
          })}
        </nav>
      </div>
      <div className="border-t border-corporate-800 p-4">
        <div className="flex items-center gap-x-3 rounded-lg p-2 bg-corporate-800/50 cursor-pointer hover:bg-corporate-800 transition-colors">
            <div className="h-8 w-8 rounded-full bg-corporate-600 flex items-center justify-center font-bold text-white shadow-inner text-sm">
                JP
            </div>
            <div className="flex flex-col">
                <span className="text-sm font-semibold text-white">Juan Pérez</span>
                <span className="text-xs text-corporate-300">Gestor Hipotecario</span>
            </div>
        </div>
      </div>
    </div>
  );
}
