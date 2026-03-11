import { clsx } from 'clsx';

type StatusType = 'Prefirma' | 'Firma Programada' | 'Firmado' | 'Bloqueado' | 'En Curso' | 'Cancelado' | string;

interface StatusBadgeProps {
  status: StatusType;
  className?: string;
}

export default function StatusBadge({ status, className }: StatusBadgeProps) {
  const getStatusStyles = (s: string) => {
    switch (s.toLowerCase()) {
      case 'prefirma':
      case 'en curso':
        return 'bg-blue-100/80 text-blue-700 ring-1 ring-blue-500/20';
      case 'firma programada':
        return 'bg-yellow-100/80 text-yellow-700 ring-1 ring-yellow-500/20';
      case 'firmado':
        return 'bg-success-light/80 text-success-dark ring-1 ring-success-main/20';
      case 'bloqueado':
      case 'cancelado':
        return 'bg-critical-light/80 text-critical-dark ring-1 ring-critical-main/20';
      default:
        return 'bg-gray-100/80 text-gray-700 ring-1 ring-gray-500/20';
    }
  };

  return (
    <span className={clsx(
      "inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold shadow-sm transition-colors duration-200",
      getStatusStyles(status),
      className
    )}>
      {status}
    </span>
  );
}
