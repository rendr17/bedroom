export const SITE = {
  name: "Rendi's Portfolio Adventure",
  author: "Rendi",
  role: "Software Developer",
  tagline: "Same Human. New Adventures.",
  description:
    "Personal portfolio of Rendi, a software developer — presented as a retro bedroom adventure inspired by early-2000s PC culture.",
} as const;

export const NAV_LINKS = [
  { href: "/about", label: "About" },
  { href: "/projects", label: "Projects" },
  { href: "/experience", label: "Experience" },
  { href: "/skills", label: "Skills" },
  { href: "/contact", label: "Contact" },
] as const;
