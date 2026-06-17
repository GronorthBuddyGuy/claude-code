"use client";

import { useState } from "react";
import { ChevronRight, File, Folder, FolderOpen } from "lucide-react";
import type { FileNode } from "@/lib/types";
import { cn } from "@/lib/utils";

function FileTreeNode({ node, depth }: { node: FileNode; depth: number }) {
  const [open, setOpen] = useState(false);
  const isDir = node.type === "directory";

  return (
    <li>
      <button
        onClick={() => isDir && setOpen((v) => !v)}
        className="flex w-full items-center gap-1.5 rounded-md px-2 py-1 text-left text-xs text-surface-400 transition-colors hover:bg-surface-800/60 hover:text-surface-200"
        style={{ paddingLeft: `${depth * 12 + 8}px` }}
      >
        {isDir ? (
          <>
            <ChevronRight
              className={cn("h-3 w-3 flex-shrink-0 transition-transform", open && "rotate-90")}
              aria-hidden="true"
            />
            {open ? (
              <FolderOpen className="h-3.5 w-3.5 flex-shrink-0 text-brand-400" aria-hidden="true" />
            ) : (
              <Folder className="h-3.5 w-3.5 flex-shrink-0 text-brand-400" aria-hidden="true" />
            )}
          </>
        ) : (
          <File className="ml-4 h-3.5 w-3.5 flex-shrink-0 text-surface-500" aria-hidden="true" />
        )}
        <span className="min-w-0 flex-1 truncate">{node.name}</span>
        {node.gitStatus && (
          <span className="flex-shrink-0 text-[10px] font-medium text-amber-400">
            {node.gitStatus}
          </span>
        )}
      </button>
      {isDir && open && node.children && node.children.length > 0 && (
        <ul>
          {node.children.map((child) => (
            <FileTreeNode key={child.path} node={child} depth={depth + 1} />
          ))}
        </ul>
      )}
    </li>
  );
}

export function FileExplorer() {
  const [tree] = useState<FileNode[]>([]);

  return (
    <div className="flex min-h-0 flex-1 flex-col">
      <div className="px-3 py-2 text-[10px] font-semibold uppercase tracking-wide text-surface-500">
        Files
      </div>
      <div className="flex-1 overflow-y-auto px-1 pb-2">
        {tree.length === 0 ? (
          <p className="px-3 py-6 text-center text-xs text-surface-500">
            No workspace connected.
          </p>
        ) : (
          <ul>
            {tree.map((node) => (
              <FileTreeNode key={node.path} node={node} depth={0} />
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
