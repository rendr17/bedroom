export interface SocialLink {
  kind: "email" | "github" | "linkedin" | "cv";
  label: string;
  href: string | null;
}

export const socials: SocialLink[] = [
  { kind: "email", label: "Email", href: null },
  { kind: "github", label: "GitHub", href: null },
  { kind: "linkedin", label: "LinkedIn", href: null },
  { kind: "cv", label: "CV", href: null },
];
