import { Outlet } from 'react-router-dom';
import FloatingNavbar from '../ui/FloatingNavbar';
import AnimatedBackground from '../ui/AnimatedBackground';
import CustomCursor from '../ui/CustomCursor';

export default function AppLayout() {
  return (
    <>
      <CustomCursor />
      <AnimatedBackground />
      <div className="min-h-screen font-sans relative">
        <FloatingNavbar />
        
        {/* Main Content Area */}
        {/* pt-28 accounts for the floating navbar height + top margin + padding */}
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-28 pb-12 transition-all duration-300">
          <div className="animate-fade-in-up">
            <Outlet />
          </div>
        </main>
      </div>
    </>
  );
}
