"use client";

import { FormEvent, useEffect, useState } from "react";
import { createProject, fetchProjects, Project } from "../lib/api";

export default function HomePage() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [form, setForm] = useState({ title: "", topic: "", audience: "", draft: "" });

  useEffect(() => {
    fetchProjects()
      .then((data) => setProjects(data))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    setSaving(true);
    setError(null);
    try {
      const project = await createProject({
        title: form.title,
        topic: form.topic,
        audience: form.audience || undefined,
        draft: form.draft || undefined,
      });
      setProjects((prev) => [project, ...prev]);
      setForm({ title: "", topic: "", audience: "", draft: "" });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setSaving(false);
    }
  }

  return (
    <main>
      <header>
        <h1>Blog Post Helper</h1>
        <p>Track story ideas, store sources, and extract claims from drafts.</p>
      </header>

      <section className="card" style={{ marginBottom: "2rem" }}>
        <h2>New project</h2>
        <form className="grid" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="title">Project title</label>
            <input
              id="title"
              value={form.title}
              onChange={(event) => setForm({ ...form, title: event.target.value })}
              required
            />
          </div>
          <div>
            <label htmlFor="topic">Topic</label>
            <input
              id="topic"
              value={form.topic}
              onChange={(event) => setForm({ ...form, topic: event.target.value })}
              required
            />
          </div>
          <div>
            <label htmlFor="audience">Audience (optional)</label>
            <input
              id="audience"
              value={form.audience}
              onChange={(event) => setForm({ ...form, audience: event.target.value })}
            />
          </div>
          <div>
            <label htmlFor="draft">Draft</label>
            <textarea
              id="draft"
              rows={5}
              value={form.draft}
              onChange={(event) => setForm({ ...form, draft: event.target.value })}
            />
          </div>
          <button type="submit" disabled={saving}>
            {saving ? "Saving..." : "Create project"}
          </button>
        </form>
        {error ? <p style={{ color: "#b91c1c" }}>{error}</p> : null}
      </section>

      <section className="card">
        <h2>Projects</h2>
        {loading ? <p>Loading projects...</p> : null}
        {!loading && projects.length === 0 ? (
          <p>
            No projects yet. Create one above to start tracking sources and claims.
          </p>
        ) : (
          <ul>
            {projects.map((project) => (
              <li key={project.id}>
                <strong>{project.title}</strong>
                <div>{project.topic}</div>
                <small>
                  {project.audience ? `Audience: ${project.audience} • ` : ""}
                  Created {new Date(project.created_at).toLocaleString()}
                </small>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  );
}
