export interface ExperienceEntry {
  role: string;
  organization: string;
  period: string;
  location?: string;
  summary?: string;
  responsibilities: string[];
  highlights: string[];
}

export const experience: ExperienceEntry[] = [];
