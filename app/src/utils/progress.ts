import { storage, STORAGE_KEYS } from "./storage";

export const QUEST_SECTIONS = [
  "about",
  "projects",
  "experience",
  "skills",
  "contact",
] as const;

export type QuestSection = (typeof QUEST_SECTIONS)[number];

export function sectionFromPath(pathname: string): QuestSection | null {
  const seg = pathname.split("/").filter(Boolean)[0];
  return (QUEST_SECTIONS as readonly string[]).includes(seg)
    ? (seg as QuestSection)
    : null;
}

export function getVisited(): QuestSection[] {
  try {
    const raw = storage.get(STORAGE_KEYS.visitedSections);
    if (!raw) return [];
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    return parsed.filter(
      (v): v is QuestSection =>
        typeof v === "string" &&
        (QUEST_SECTIONS as readonly string[]).includes(v),
    );
  } catch {
    return [];
  }
}

export function markVisited(id: QuestSection): void {
  const visited = getVisited();
  if (!visited.includes(id)) {
    visited.push(id);
    storage.set(STORAGE_KEYS.visitedSections, JSON.stringify(visited));
  }
}
