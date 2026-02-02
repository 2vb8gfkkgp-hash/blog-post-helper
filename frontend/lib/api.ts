const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export type Project = {
  id: number;
  title: string;
  topic: string;
  audience?: string | null;
  deadline?: string | null;
  draft?: string | null;
  created_at: string;
};

export async function fetchProjects(): Promise<Project[]> {
  const res = await fetch(`${API_BASE}/projects`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error("Failed to load projects");
  }
  return res.json();
}

export async function createProject(payload: {
  title: string;
  topic: string;
  audience?: string;
  draft?: string;
}): Promise<Project> {
  const res = await fetch(`${API_BASE}/projects`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    throw new Error("Failed to create project");
  }
  return res.json();
}
