// @ts-check
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

// https://astro.build/config
export default defineConfig({
    site: "https://guyjuniorcalvet.github.io",
    base: "/Mon_Portfolio",
  vite: {
    plugins: [tailwindcss()],
  },
});
