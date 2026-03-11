/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        corporate: {
          50: '#f0f5fa',
          100: '#e1ecf4',
          200: '#c3d9e9',
          300: '#a5c6de',
          400: '#69a0c8',
          500: '#2d7ab2', // corporate blue
          600: '#286e9f',
          700: '#225b85',
          800: '#1b496b',
          900: '#163c57',
        },
        graphite: {
          50: '#f4f5f6',
          100: '#e9ebee',
          200: '#c8cbd2',
          300: '#a7abb7',
          400: '#656b80',
          500: '#232b49', // graphite gray
          600: '#202742',
          700: '#1a2037',
          800: '#151a2c',
          900: '#111524',
        },
        success: {
          light: '#d0f2cd',
          main: '#35a62d', // success green
          dark: '#267b20',
        },
        critical: {
          light: '#fcd3d3',
          main: '#d62f2f', // critical red
          dark: '#9e2222',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
