import type { Hotspot } from "@/types/hotspot";

export const hotspots: Hotspot[] = [
  {
    id: "about",
    label: "About Me",
    quest: "Learn about Rendi",
    href: "/about",
    desktop: { x: 26, y: 36 },
    mobileOrder: 2,
  },
  {
    id: "projects",
    label: "Projects",
    quest: "Check out the projects",
    href: "/projects",
    desktop: { x: 51, y: 44 },
    mobileOrder: 1,
  },
  {
    id: "experience",
    label: "Experience",
    quest: "Review experience",
    href: "/experience",
    desktop: { x: 71, y: 30 },
    mobileOrder: 3,
  },
  {
    id: "skills",
    label: "Skills",
    quest: "Sharpen your skills",
    href: "/skills",
    desktop: { x: 80, y: 47 },
    mobileOrder: 4,
  },
  {
    id: "contact",
    label: "Contact",
    quest: "Get in touch",
    href: "/contact",
    desktop: { x: 93, y: 57 },
    mobileOrder: 5,
  },
  {
    id: "extras",
    label: "Extras",
    href: "/extras",
    desktop: { x: 6, y: 72 },
    mobileOrder: 6,
    optional: true,
    icon: "/assets/props/gamepad.png",
  },
];
