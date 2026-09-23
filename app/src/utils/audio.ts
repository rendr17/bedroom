import { storage, STORAGE_KEYS } from "./storage";

export type CueName = "click" | "open" | "startup" | "success";

const elements = new Map<CueName, HTMLAudioElement>();

export function isSoundEnabled(): boolean {
  return storage.get(STORAGE_KEYS.soundEnabled) === "1";
}

export function setSoundEnabled(on: boolean): void {
  storage.set(STORAGE_KEYS.soundEnabled, on ? "1" : "0");
}

export function playCue(name: CueName): void {
  if (!isSoundEnabled()) return;
  try {
    let el = elements.get(name);
    if (!el) {
      el = new Audio(`/assets/audio/${name}.wav`);
      el.volume = 0.45;
      elements.set(name, el);
    }
    el.currentTime = 0;
    void el.play().catch(() => {
      /* autoplay blocked — silent no-op, audio never blocks interaction */
    });
  } catch {
    /* audio unavailable — non-fatal */
  }
}
