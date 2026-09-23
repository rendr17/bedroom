import type { Hotspot } from "@/types/hotspot";

export const hotspots: Hotspot[] = [
  {
    id: "about",
    label: "About Me",
    href: "/about",
    desktop: { x: 23, y: 20 },
    mobileOrder: 2,
  },
  {
    id: "projects",
    label: "Explore Projects",
    href: "/projects",
    desktop: { x: 47, y: 55 },
    mobileOrder: 1,
  },
  {
    id: "experience",
    label: "Experience",
    href: "/experience",
    desktop: { x: 85, y: 70 },
    mobileOrder: 3,
  },
  {
    id: "skills",
    label: "Skills",
    href: "/skills",
    desktop: { x: 16, y: 42 },
    mobileOrder: 4,
  },
  {
    id: "contact",
    label: "Contact",
    href: "/contact",
    desktop: { x: 82, y: 26 },
    mobileOrder: 5,
  },
  {
    id: "extras",
    label: "Extras",
    href: "/extras",
    desktop: { x: 61, y: 89 },
    mobileOrder: 6,
    optional: true,
    icon: "/assets/props/gamepad.png",
  },
];
