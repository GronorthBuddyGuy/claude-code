"use client";

import { useState } from "react";
import { Check, CornerDownRight, Send, X } from "lucide-react";
import { cn, formatDate } from "@/lib/utils";
import { useCollaborationContextOptional } from "./CollaborationProvider";

interface AnnotationThreadProps {
  messageId: string;
  onClose: () => void;
}

export function AnnotationThread({ messageId, onClose }: AnnotationThreadProps) {
  const ctx = useCollaborationContextOptional();
  const [draft, setDraft] = useState("");
  const [replyDrafts, setReplyDrafts] = useState<Record<string, string>>({});

  if (!ctx) return null;

  const annotations = ctx.annotations[messageId] ?? [];

  const submitComment = () => {
    const text = draft.trim();
    if (!text) return;
    ctx.addAnnotation(messageId, text);
    setDraft("");
  };

  const submitReply = (annotationId: string) => {
    const text = (replyDrafts[annotationId] ?? "").trim();
    if (!text) return;
    ctx.replyAnnotation(annotationId, text);
    setReplyDrafts((d) => ({ ...d, [annotationId]: "" }));
  };

  return (
    <div className="overflow-hidden rounded-lg border border-surface-700 bg-surface-900 shadow-lg">
      <div className="flex items-center justify-between border-b border-surface-800 px-3 py-2">
        <span className="text-xs font-semibold text-surface-200">
          Comments{annotations.length > 0 ? ` (${annotations.length})` : ""}
        </span>
        <button
          onClick={onClose}
          aria-label="Close comments"
          className="rounded p-1 text-surface-500 hover:bg-surface-800 hover:text-surface-300"
        >
          <X className="h-3.5 w-3.5" aria-hidden="true" />
        </button>
      </div>

      <div className="max-h-72 overflow-y-auto px-3 py-2">
        {annotations.length === 0 ? (
          <p className="py-4 text-center text-xs text-surface-500">No comments yet.</p>
        ) : (
          <ul className="space-y-3">
            {annotations.map((a) => (
              <li key={a.id} className={cn("text-xs", a.resolved && "opacity-60")}>
                <div className="flex items-center gap-2">
                  <span className="font-medium text-surface-200" style={{ color: a.author.color }}>
                    {a.author.name}
                  </span>
                  <span className="text-[10px] text-surface-500">{formatDate(a.createdAt)}</span>
                  <button
                    onClick={() => ctx.resolveAnnotation(a.id, !a.resolved)}
                    title={a.resolved ? "Reopen" : "Resolve"}
                    aria-label={a.resolved ? "Reopen comment" : "Resolve comment"}
                    className={cn(
                      "ml-auto rounded p-0.5 hover:bg-surface-800",
                      a.resolved ? "text-green-400" : "text-surface-500"
                    )}
                  >
                    <Check className="h-3 w-3" aria-hidden="true" />
                  </button>
                </div>
                <p className="mt-0.5 whitespace-pre-wrap text-surface-300">{a.text}</p>

                {a.replies.length > 0 && (
                  <ul className="mt-1.5 space-y-1.5 border-l border-surface-800 pl-2">
                    {a.replies.map((r) => (
                      <li key={r.id}>
                        <div className="flex items-center gap-2">
                          <CornerDownRight className="h-3 w-3 text-surface-600" aria-hidden="true" />
                          <span className="font-medium text-surface-300" style={{ color: r.author.color }}>
                            {r.author.name}
                          </span>
                          <span className="text-[10px] text-surface-500">{formatDate(r.createdAt)}</span>
                        </div>
                        <p className="mt-0.5 whitespace-pre-wrap pl-5 text-surface-400">{r.text}</p>
                      </li>
                    ))}
                  </ul>
                )}

                <div className="mt-1.5 flex items-center gap-1.5 pl-2">
                  <input
                    value={replyDrafts[a.id] ?? ""}
                    onChange={(e) => setReplyDrafts((d) => ({ ...d, [a.id]: e.target.value }))}
                    onKeyDown={(e) => e.key === "Enter" && submitReply(a.id)}
                    placeholder="Reply…"
                    className="min-w-0 flex-1 rounded border border-surface-800 bg-surface-950 px-2 py-1 text-[11px] text-surface-200 placeholder:text-surface-600 focus:border-brand-600 focus:outline-none"
                  />
                  <button
                    onClick={() => submitReply(a.id)}
                    aria-label="Send reply"
                    className="rounded p-1 text-surface-500 hover:bg-surface-800 hover:text-brand-400"
                  >
                    <Send className="h-3 w-3" aria-hidden="true" />
                  </button>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>

      <div className="flex items-center gap-1.5 border-t border-surface-800 px-3 py-2">
        <input
          value={draft}
          onChange={(e) => setDraft(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && submitComment()}
          placeholder="Add a comment…"
          className="min-w-0 flex-1 rounded border border-surface-800 bg-surface-950 px-2 py-1 text-xs text-surface-200 placeholder:text-surface-600 focus:border-brand-600 focus:outline-none"
        />
        <button
          onClick={submitComment}
          aria-label="Add comment"
          className="rounded bg-brand-600 p-1.5 text-white transition-colors hover:bg-brand-500"
        >
          <Send className="h-3 w-3" aria-hidden="true" />
        </button>
      </div>
    </div>
  );
}
