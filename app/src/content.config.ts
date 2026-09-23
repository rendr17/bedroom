import { defineCollection, z } from "astro:content";
import { file, glob } from "astro/loaders";

const projects = defineCollection({
  loader: glob({ pattern: "*.json", base: "./src/content/projects" }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    category: z.string(),
    role: z.string(),
    status: z.string(),
    featured: z.boolean().default(false),
    sortOrder: z.number().optional(),
    year: z.string().optional(),
    shortDescription: z.string(),
    longDescription: z.string().optional(),
    problem: z.string().optional(),
    solution: z.string().optional(),
    responsibilities: z.array(z.string()).default([]),
    features: z.array(z.string()).default([]),
    technology: z.array(z.string()).default([]),
    impact: z.array(z.string()).default([]),
    screenshots: z
      .array(z.object({ src: z.string(), alt: z.string() }))
      .default([]),
    links: z
      .array(z.object({ label: z.string(), href: z.string() }))
      .default([]),
    accent: z.string().optional(),
  }),
});

const skills = defineCollection({
  loader: file("src/data/skills.json"),
  schema: z.object({
    name: z.string(),
    items: z
      .array(z.object({ name: z.string(), context: z.string().optional() }))
      .default([]),
  }),
});

export const collections = { projects, skills };
