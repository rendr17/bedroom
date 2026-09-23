import type { Hotspot } from "@/types/hotspot";

export const hotspots: Hotspot[] = [
  {
    id: "about",
    label: "About Me",
    href: "/about",
    desktop: { x: 24, y: 38 },
    mobileOrder: 2,
  },
  {
    id: "projects",
    label: "Explore Projects",
    href: "/projects",
    desktop: { x: 48, y: 42 },
    mobileOrder: 1,
  },
  {
    id: "experience",
    label: "Experience",
    href: "/experience",
    desktop: { x: 79, y: 24 },
    mobileOrder: 3,
  },
  {
    id: "skills",
    label: "Skills",
    href: "/skills",
    desktop: { x: 78, y: 52 },
    mobileOrder: 4,
  },
  {
    id: "contact",
    label: "Contact",
    href: "/contact",
    desktop: { x: 89, y: 63 },
    mobileOrder: 5,
  },
  {
    id: "extras",
    label: "Extras",
    href: "/extras",
    desktop: { x: 12, y: 72 },
    mobileOrder: 6,
    optional: true,
  },
];
