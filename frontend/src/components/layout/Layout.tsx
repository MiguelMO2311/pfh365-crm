import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Topbar from './Topbar';

export default function Layout() {
  return (
    <div className="flex h-screen bg-gray-50 flex-col md:flex-row font-sans">
      {/* Sidebar for desktop */}
      <div className="hidden md:flex md:w-64 md:flex-col md:fixed md:inset-y-0 z-20">
        <Sidebar />
      </div>
      
      {/* Main content wrapper */}
      <div className="flex w-full flex-col md:pl-64 h-screen overflow-hidden">
        <Topbar />
        
        <main className="flex-1 overflow-y-auto w-full p-4 sm:p-6 lg:p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
