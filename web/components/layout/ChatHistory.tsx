"use client";

import { useMemo } from "react";
import { MessageSquare, Pin, Trash2, Plus } from "lucide-react";
import { useChatStore } from "@/lib/store";
import { cn, formatDate } from "@/lib/utils";

export function ChatHistory() {
  const {
    conversations,
    activeConversationId,
    pinnedIds,
    searchQuery,
    createConversation,
    setActiveConversation,
    deleteConversation,
    pinConversation,
  } = useChatStore();

  const filtered = useMemo(() => {
    const q = searchQuery.trim().toLowerCase();
    const matches = q
      ? conversations.filter((c) => c.title.toLowerCase().includes(q))
      : conversations;
    const pinnedSet = new Set(pinnedIds);
    return [...matches].sort((a, b) => {
      const ap = pinnedSet.has(a.id) ? 1 : 0;
      const bp = pinnedSet.has(b.id) ? 1 : 0;
      if (ap !== bp) return bp - ap;
      return b.updatedAt - a.updatedAt;
    });
  }, [conversations, pinnedIds, searchQuery]);

  return (
    <div className="flex flex-col min-h-0 flex-1">
      <div className="px-3 pt-3 pb-2">
        <button
          onClick={() => createConversation()}
          className="flex w-full items-center gap-2 rounded-md bg-brand-600 px-3 py-2 text-xs font-medium text-white transition-colors hover:bg-brand-500"
        >
          <Plus className="h-4 w-4" aria-hidden="true" />
          New conversation
        </button>
      </div>

      <div className="flex-1 overflow-y-auto px-2 pb-2">
        {filtered.length === 0 ? (
          <p className="px-3 py-6 text-center text-xs text-surface-500">
            No conversations yet.
          </p>
        ) : (
          <ul className="space-y-0.5">
            {filtered.map((c) => {
              const isPinned = pinnedIds.includes(c.id);
              const isActive = c.id === activeConversationId;
              return (
                <li key={c.id}>
                  <div
                    className={cn(
                      "group flex items-center gap-2 rounded-md px-2.5 py-2 text-xs transition-colors",
                      isActive
                        ? "bg-surface-800 text-surface-100"
                        : "text-surface-400 hover:bg-surface-800/60 hover:text-surface-200"
                    )}
                  >
                    <button
                      onClick={() => setActiveConversation(c.id)}
                      className="flex min-w-0 flex-1 items-center gap-2 text-left"
                    >
                      <MessageSquare className="h-3.5 w-3.5 flex-shrink-0" aria-hidden="true" />
                      <span className="min-w-0 flex-1 truncate">{c.title}</span>
                      <span className="flex-shrink-0 text-[10px] text-surface-500">
                        {formatDate(c.updatedAt)}
                      </span>
                    </button>
                    <div className="flex flex-shrink-0 items-center gap-0.5 opacity-0 transition-opacity group-hover:opacity-100">
                      <button
                        onClick={() => pinConversation(c.id)}
                        title={isPinned ? "Unpin" : "Pin"}
                        aria-label={isPinned ? "Unpin conversation" : "Pin conversation"}
                        className={cn(
                          "rounded p-1 hover:bg-surface-700",
                          isPinned ? "text-brand-400" : "text-surface-500"
                        )}
                      >
                        <Pin className="h-3 w-3" aria-hidden="true" />
                      </button>
                      <button
                        onClick={() => deleteConversation(c.id)}
                        title="Delete"
                        aria-label="Delete conversation"
                        className="rounded p-1 text-surface-500 hover:bg-surface-700 hover:text-red-400"
                      >
                        <Trash2 className="h-3 w-3" aria-hidden="true" />
                      </button>
                    </div>
                  </div>
                </li>
              );
            })}
          </ul>
        )}
      </div>
    </div>
  );
}
