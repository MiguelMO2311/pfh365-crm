# PFH365 CRM - Gestión Hipotecaria Enterprise

Sistema CRM full-stack para gestión de expedientes hipotecarios en España. Abarca prefirma, formalización documental (FEIN, FIAE) y control de cargas.

## 🏗️ Arquitectura del Proyecto

El proyecto está diseñado como un **Monorepo** con dos componentes principales:
* `/backend`: API RESTful en Python usando **FastAPI** y **SQLite** (preparado para PostgreSQL).
* `/frontend`: Single Page Application (SPA) en **React** construida con **Vite**, **TypeScript** y **Tailwind CSS**.

### Estructura
```text
/pfh365-crm
├── backend/
│   ├── app/
│   │   ├── main.py                (Punto de entrada FastAPI)
│   │   ├── config.py              (Variables de entorno)
│   │   ├── database.py            (Conexión SQLAlchemy)
│   │   ├── models/                (Modelos Pydantic y BD)
│   │   ├── routers/               (Endpoints)
│   │   └── services/              (Lógica y validación LCCI)
│   ├── seed_data.py               (Generador de datos MOCK)
│   └── requirements.txt           (Dependencias)
│
└── frontend/
    ├── src/
    │   ├── api/                   (Cliente Axios)
    │   ├── components/            (Layouts, Sidebar, Topbar)
    │   ├── pages/                 (Dashboard, Listado y Detalle)
    │   ├── App.tsx                (Routing)
    │   ├── main.tsx
    │   └── index.css              (Estilos Tailwind y Componentes UI)
    ├── tailwind.config.js         (Paleta corporativa)
    └── package.json               (Dependencias NPM)
```

## 🚀 Instalación y Ejecución Local

### Paso 1: Ejecutar el Backend (FastAPI)
Abre una terminal y navega al directorio del backend:
```bash
cd pfh365-crm/backend
```
Instala las dependencias y crea la base de datos con datos de prueba:
```bash
pip install -r requirements.txt
python seed_data.py
```
Ejecuta el servidor FastAPI con Uvicorn:
```bash
uvicorn app.main:app --reload --port 8000
```
La API estará disponible en `http://localhost:8000` y la documentación (Swagger) en `http://localhost:8000/api/v1/openapi.json`.

### Paso 2: Ejecutar el Frontend (React + Vite)
Adicionalmente, abre una **nueva terminal** y navega al frontend:
```bash
cd pfh365-crm/frontend
```
*(Nota: Si hiciste scaffold manual con Vite, asegúrate de que esté configurado. React ha sido instalado manualmente por el asistente).*
Instala los módulos de Node e inicia el servidor de desarrollo:
```bash
npm install
npm run dev
```
La aplicación web estará disponible típicamente en `http://localhost:5173`.

## ✨ Características Funcionales
1. **Métricas en Vivo:** Gráficos (Dashboard) con expedientes pendientes y alertas.
2. **Validaciones LCCI Automáticas:** Reglas estrictas de 10 días para la FEIN, control de caducidad documental (DNI/Tasación) y bloqueos de firma.
3. **Cargas Registrales:** Registro de hipotecas previas y embargos vinculados de Expedientes y Operaciones.
4. **Diseño Enterprise:** UI minimalista, optimizada y profesional diseñada con Tailwind CSS.

> [!TIP]
> Puedes re-ejecutar `python seed_data.py` en cualquier momento para reiniciar e incluir nuevos expedientes de pruebas.
