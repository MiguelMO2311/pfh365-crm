import { clsx } from 'clsx';
import { CheckCircleIcon, ClockIcon, ExclamationCircleIcon, DocumentCheckIcon } from '@heroicons/react/24/solid';

export type TimelineEventType = 'creation' | 'document' | 'alert' | 'status_change';

export interface TimelineEvent {
  id: string | number;
  type: TimelineEventType;
  title: string;
  description: string;
  date: string;
  isActive?: boolean;
}

interface TimelineProps {
  events: TimelineEvent[];
}

export default function Timeline({ events }: TimelineProps) {
  const getEventIcon = (type: TimelineEventType, isActive?: boolean) => {
    const className = clsx("h-6 w-6 relative z-10 rounded-full ring-4 ring-white shadow-sm", 
      isActive ? "animate-pulse" : ""
    );
    
    switch (type) {
      case 'creation': return <CheckCircleIcon className={clsx(className, "text-corporate-500 bg-white")} />;
      case 'document': return <DocumentCheckIcon className={clsx(className, "text-indigo-500 bg-white")} />;
      case 'alert': return <ExclamationCircleIcon className={clsx(className, "text-critical-main bg-white")} />;
      case 'status_change': return <ClockIcon className={clsx(className, "text-yellow-500 bg-white")} />;
      default: return <div className={clsx(className, "bg-gray-200")} />;
    }
  };

  return (
    <div className="flow-root">
      <ul role="list" className="-mb-8">
        {events.map((event, eventIdx) => (
          <li key={event.id}>
            <div className="relative pb-8 group">
              {eventIdx !== events.length - 1 ? (
                <span className="absolute left-3 top-4 -ml-px h-full w-0.5 bg-gray-200 group-hover:bg-corporate-200 transition-colors duration-300" aria-hidden="true" />
              ) : null}
              <div className="relative flex space-x-3 items-start">
                <div>
                  {getEventIcon(event.type, event.isActive)}
                </div>
                <div className="flex min-w-0 flex-1 justify-between space-x-4 pt-1.5 transition-all duration-200 hover:translate-x-1">
                  <div>
                    <p className="text-sm text-gray-900 font-medium">{event.title}</p>
                    <p className="mt-0.5 text-sm text-gray-500">{event.description}</p>
                  </div>
                  <div className="whitespace-nowrap text-right text-xs text-gray-400 font-medium">
                    {event.date}
                  </div>
                </div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
