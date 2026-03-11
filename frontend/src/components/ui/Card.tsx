import { ReactNode } from 'react';
import { clsx } from 'clsx';

interface CardProps {
  children: ReactNode;
  className?: string;
  noPadding?: boolean;
}

export default function Card({ children, className, noPadding = false }: CardProps) {
  return (
    <div className={clsx(
      "bg-white/80 backdrop-blur-md rounded-2xl shadow-sm border border-gray-100/80 overflow-hidden transition-all duration-300 hover:shadow-xl hover:-translate-y-1 group",
      !noPadding && "p-6",
      className
    )}>
      {children}
    </div>
  );
}
