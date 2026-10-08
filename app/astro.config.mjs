import process from "node:process";
import { defineConfig } from "astro/config";

const site = process.env.PUBLIC_SITE_URL;

export default defineConfig(site ? { site } : {});
