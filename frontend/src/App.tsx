import { BrowserRouter, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import AppLayout from './components/layout/AppLayout';
import DashboardPage from './pages/DashboardPage';
import ExpedientesListPage from './pages/ExpedienteList';
import ExpedientePage from './pages/ExpedienteDetail';
import LoginPage from './pages/LoginPage';
import OperacionesPage from './pages/OperacionesPage';
import AlertasPage from './pages/AlertasPage';
import { AuthProvider, useAuth } from './context/AuthContext';

function ProtectedRoute({ children }: { children: JSX.Element }) {
  const { isAuthenticated, loadingAuth } = useAuth();
  const location = useLocation();

  if (loadingAuth) {
    return (
      <div className="w-full h-screen flex items-center justify-center text-white">
        Cargando...
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return children;
}

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />

          <Route
            path="/"
            element={
              <ProtectedRoute>
                <AppLayout />
              </ProtectedRoute>
            }
          >
            <Route index element={<Navigate to="/dashboard" replace />} />
            <Route path="dashboard" element={<DashboardPage />} />
            <Route path="expedientes" element={<ExpedientesListPage />} />
            <Route path="expedientes/:id" element={<ExpedientePage />} />
            <Route path="operaciones" element={<OperacionesPage />} />
            <Route path="alertas" element={<AlertasPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
