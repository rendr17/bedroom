import { getCollection } from "astro:content";

export async function getSortedProjects() {
  const entries = await getCollection("projects");
  return entries
    .slice()
    .sort(
      (a, b) =>
        (a.data.sortOrder ?? Number.MAX_SAFE_INTEGER) -
          (b.data.sortOrder ?? Number.MAX_SAFE_INTEGER) ||
        a.data.title.localeCompare(b.data.title),
    );
}
