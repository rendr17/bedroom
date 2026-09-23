export type HotspotId =
  "about" | "projects" | "experience" | "skills" | "contact" | "extras";

export interface Hotspot {
  id: HotspotId;
  label: string;
  quest?: string;
  href: string;
  desktop: { x: number; y: number };
  mobileOrder: number;
  optional?: boolean;
  icon?: string;
}
