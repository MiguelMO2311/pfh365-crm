import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { BuildingLibraryIcon } from '@heroicons/react/24/solid';
import { useAuth } from '../context/AuthContext';
import Card from '../components/ui/Card';
import { apiClient } from '../services/apiCore';

export default function LoginPage() {
  const [username, setUsername] = useState('admin@pfh365.com');
  const [password, setPassword] = useState('admin123');
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg('');
    
    try {
      const params = new URLSearchParams();
      params.append('username', username);
      params.append('password', password);

      const response = await apiClient.post('/auth/login', params, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });
      
      const { access_token } = response.data;
      
      login(access_token, 'Admin PFH365');
      navigate('/dashboard');
    } catch (error: any) {
      console.error("Login Error:", error);
      setErrorMsg(error.response?.data?.detail || 'Error de credenciales o servidor');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen relative flex items-center justify-center overflow-hidden">
      
      {/* Background */}
      <div 
        className="absolute inset-0 z-0 bg-cover bg-center"
        style={{ backgroundImage: 'url(/assets/images/corporate-bg.png)' }}
      >
        <div className="absolute inset-0 bg-gray-900/60 backdrop-blur-sm mix-blend-multiply" />
        <div className="absolute inset-0 bg-gradient-to-t from-gray-950 via-transparent to-transparent opacity-90" />
      </div>

      {/* Login Card */}
      <div className="relative z-10 w-full max-w-md px-6 animate-fade-in-up">
        <Card className="!p-8 bg-white/20 backdrop-blur-xl border border-white/30 shadow-2xl rounded-3xl text-center">

          {/* Logo */}
          <div className="flex justify-center mb-6">
            <div className="h-16 w-16 rounded-2xl bg-gradient-to-br from-corporate-500 to-corporate-700 flex items-center justify-center shadow-lg shadow-corporate-500/30">
              <BuildingLibraryIcon className="h-8 w-8 text-white" />
            </div>
          </div>

          {/* Title */}
          <h2 className="text-3xl font-bold tracking-tight text-white mb-2">
            PFH<span className="text-corporate-400">365</span> CRM
          </h2>
          <p className="text-sm text-gray-200 mb-8">
            Plataforma Enterprise de Gestión Hipotecaria
          </p>

          {/* Form */}
          <form onSubmit={handleLogin} className="space-y-6 text-left">

            {/* Email */}
            <div>
              <label className="block text-sm font-medium leading-6 text-gray-100">
                Correo Electrónico
              </label>
              <div className="mt-2">
                <input
                  type="email"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="block w-full rounded-xl border border-white/40 py-3 px-4 
                             bg-white/80 text-gray-900 placeholder-gray-600
                             focus:ring-2 focus:ring-corporate-400 outline-none transition-all"
                  required
                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label className="block text-sm font-medium leading-6 text-gray-100">
                Contraseña
              </label>
              <div className="mt-2">
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="block w-full rounded-xl border border-white/40 py-3 px-4 
                             bg-white/80 text-gray-900 placeholder-gray-600
                             focus:ring-2 focus:ring-corporate-400 outline-none transition-all"
                  required
                />
              </div>
            </div>

            {/* Error */}
            {errorMsg && (
              <div className="text-red-100 bg-red-600/40 border border-red-600/50 p-3 rounded-lg text-sm text-center backdrop-blur-sm">
                {errorMsg}
              </div>
            )}

            {/* Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-gradient-to-r from-corporate-500 to-corporate-600 
                         hover:from-corporate-600 hover:to-corporate-700 
                         text-white py-3 rounded-xl shadow-lg shadow-corporate-500/25 
                         flex justify-center text-base font-semibold"
            >
              {loading ? 'Iniciando sesión...' : 'Ingresar al Portal'}
            </button>

          </form>
        </Card>
      </div>
    </div>
  );
}
