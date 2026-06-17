"use client";

import { Plus, Search, Settings } from "lucide-react";
import { useChatStore } from "@/lib/store";

export function QuickActions() {
  const { createConversation, openSearch, openSettings } = useChatStore();

  const actions = [
    { icon: Plus, label: "New chat", onClick: () => createConversation() },
    { icon: Search, label: "Search", onClick: () => openSearch() },
    { icon: Settings, label: "Settings", onClick: () => openSettings() },
  ];

  return (
    <div className="flex flex-shrink-0 items-center justify-around border-t border-surface-800 px-2 py-2">
      {actions.map(({ icon: Icon, label, onClick }) => (
        <button
          key={label}
          onClick={onClick}
          title={label}
          aria-label={label}
          className="flex flex-col items-center gap-1 rounded-md px-3 py-1.5 text-[10px] text-surface-500 transition-colors hover:bg-surface-800/60 hover:text-surface-300"
        >
          <Icon className="h-4 w-4" aria-hidden="true" />
          {label}
        </button>
      ))}
    </div>
  );
}
