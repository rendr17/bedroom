export const STORAGE_KEYS = {
  introSeen: "portfolio:introSeen",
  visitedSections: "portfolio:visitedSections",
  soundEnabled: "portfolio:soundEnabled",
  reducedEffects: "portfolio:reducedEffects",
} as const;

export const storage = {
  get(key: string): string | null {
    try {
      return localStorage.getItem(key);
    } catch {
      return null;
    }
  },
  set(key: string, value: string): void {
    try {
      localStorage.setItem(key, value);
    } catch {
      // storage blocked/full — non-fatal
    }
  },
  remove(key: string): void {
    try {
      localStorage.removeItem(key);
    } catch {
      // storage blocked — non-fatal
    }
  },
};
