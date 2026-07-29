import { cp, mkdir, readdir, rm } from "node:fs/promises";
import { extname, join } from "node:path";

const root = process.cwd();
const output = join(root, "public");
const copiedExtensions = new Set([".html", ".css", ".js", ".txt", ".xml", ".png"]);
const copiedDirectories = ["assets", "uploads", "altr-brand-assets"];
const excludedFiles = new Set([
  "claude-tutorials-page.png",
  "impact-scrolled.png",
  "impact-studies-preview.png",
  "impact-studies-v2.png",
  "impact-studies-v3.png",
  "tutorials-filter-mcp.png",
  "tutorials-page-preview.png",
  "tutorials-v2-preview.png",
]);

await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });

for (const entry of await readdir(root, { withFileTypes: true })) {
  if (!entry.isFile()) continue;
  if (!copiedExtensions.has(extname(entry.name))) continue;
  if (excludedFiles.has(entry.name)) continue;
  await cp(join(root, entry.name), join(output, entry.name));
}

for (const directory of copiedDirectories) {
  await cp(join(root, directory), join(output, directory), { recursive: true });
}
