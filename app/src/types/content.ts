export interface Profile {
  name: string;
  role: string;
  tagline: string;
  bio: string;
  focus: string[];
  interests: string[];
  currentFocus: string;
}

export interface SocialLink {
  kind: "email" | "github" | "linkedin" | "cv";
  label: string;
  href: string | null;
}

export interface ExperienceEntry {
  role: string;
  organization: string;
  period: string;
  location?: string;
  summary?: string;
  responsibilities: string[];
  highlights: string[];
}
