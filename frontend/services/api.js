export function extractRepository(input) {
  const value = input.trim();

  if (!value) {
    throw new Error("Please enter a GitHub repository URL.");
  }

  let cleaned = value
    .replace(/^https?:\/\//, "")
    .replace(/^www\./, "")
    .replace(/\.git$/, "")
    .replace(/\/$/, "");

  if (cleaned.startsWith("github.com/")) {
    cleaned = cleaned.substring("github.com/".length);
  }

  const parts = cleaned.split("/");

  if (parts.length < 2) {
    throw new Error("Repository URL is incomplete.");
  }

  const owner = parts[0];
  const repo = parts[1];

  return { owner, repo };
}