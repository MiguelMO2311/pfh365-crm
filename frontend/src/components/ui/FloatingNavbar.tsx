import { Link, useLocation } from 'react-router-dom';
import { HomeIcon, FolderOpenIcon, ChartBarIcon, BellIcon, ArrowRightOnRectangleIcon } from '@heroicons/react/24/outline';
import { clsx } from 'clsx';
import { useAuth } from '../../context/AuthContext';

export default function FloatingNavbar() {
  const location = useLocation();
  const { userName, logout } = useAuth();

  const navItems = [
    { name: 'Dashboard', href: '/dashboard', icon: HomeIcon },
    { name: 'Expedientes', href: '/expedientes', icon: FolderOpenIcon },
    { name: 'Operaciones', href: '/operaciones', icon: ChartBarIcon },
  ];

  return (
    <div className="fixed top-4 left-1/2 transform -translate-x-1/2 z-50 w-[95%] max-w-5xl">
      <div className="bg-white/70 backdrop-blur-md rounded-2xl shadow-xl border border-gray-200 p-2 flex items-center justify-between transition-all duration-300 hover:shadow-2xl hover:bg-white/80">
        
        {/* Logo/Brand */}
        <div className="flex items-center gap-2 pl-4">
          <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-corporate-500 to-corporate-700 flex items-center justify-center shadow-inner">
            <span className="text-white font-bold text-xs tracking-wider">P365</span>
          </div>
          <span className="font-bold text-gray-900 hidden sm:block tracking-tight text-lg">PFH CRM <span className="text-corporate-500">V2</span></span>
        </div>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center gap-1 bg-gray-50/50 p-1 rounded-xl border border-gray-100/50">
          {navItems.map((item) => {
            const isActive = location.pathname.startsWith(item.href) && item.href !== '#';
            return (
              <Link
                key={item.name}
                to={item.href}
                className={clsx(
                  'flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200',
                  isActive 
                    ? 'bg-white text-corporate-600 shadow-xl ring-1 ring-gray-900/5' 
                    : 'text-gray-500 hover:text-gray-900 hover:bg-gray-100/50'
                )}
              >
                <item.icon className={clsx("h-4 w-4", isActive ? "text-corporate-500" : "text-gray-400")} />
                {item.name}
              </Link>
            )
          })}
        </nav>

        {/* User Actions */}
        <div className="flex items-center gap-3 pr-2">
          <Link to="/alertas" className="relative p-2 text-gray-400 hover:text-corporate-500 transition-colors rounded-full hover:bg-gray-100">
            <BellIcon className="h-5 w-5" />
            <span className="absolute top-1.5 right-2 h-2 w-2 rounded-full bg-critical-main ring-2 ring-white animate-pulse"></span>
          </Link>
          <div className="flex items-center gap-3 pl-2 border-l border-gray-200/50">
            <div className="hidden sm:block text-right">
              <p className="text-xs font-bold text-gray-900">{userName}</p>
              <p className="text-[10px] text-gray-500 font-medium">Administrador</p>
            </div>
            <div className="h-8 w-8 rounded-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 p-[2px] shadow-sm">
              <div className="h-full w-full rounded-full bg-white flex items-center justify-center overflow-hidden">
                <span className="text-xs font-bold text-gray-700">{userName?.charAt(0) || 'U'}</span>
              </div>
            </div>
          </div>
          <button 
            onClick={logout}
            className="p-2 text-gray-400 hover:text-critical-main transition-colors rounded-full hover:bg-critical-50 ml-1"
            title="Cerrar sesión"
          >
            <ArrowRightOnRectangleIcon className="h-5 w-5" />
          </button>
        </div>

      </div>
    </div>
  );
}
