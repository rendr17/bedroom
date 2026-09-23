export interface Profile {
  name: string;
  role: string;
  tagline: string;
  bio: string;
  focus: string[];
  interests: string[];
  currentFocus: string;
}

export const profile: Profile = {
  name: "Rendi",
  role: "Software Developer",
  tagline: "Same Human. New Adventures.",
  bio: "I build practical web applications, internal systems, integrations, and digital products.",
  focus: [
    "Full-stack web development",
    "AI integration",
    "Internal systems & operations",
    "Product experiments",
  ],
  interests: [
    "Practical products",
    "Systems & automation",
    "Games & web experiments",
  ],
  currentFocus: "AI integration",
};
