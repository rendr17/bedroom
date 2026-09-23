export const SITE = {
  name: "Rendi's Portfolio Adventure",
  author: "Rendi",
  role: "Software Developer",
  tagline: "Same Human. New Adventures.",
  description:
    "Personal portfolio of Rendi, a software developer — presented as a retro bedroom adventure inspired by early-2000s PC culture.",
} as const;

export const NAV_LINKS = [
  { href: "/about", label: "About", icon: "/assets/icons/nav/about.png" },
  {
    href: "/projects",
    label: "Projects",
    icon: "/assets/icons/nav/projects.png",
  },
  {
    href: "/experience",
    label: "Experience",
    icon: "/assets/icons/nav/experience.png",
  },
  { href: "/skills", label: "Skills", icon: "/assets/icons/nav/skills.png" },
  { href: "/contact", label: "Contact", icon: "/assets/icons/nav/contact.png" },
] as const;
