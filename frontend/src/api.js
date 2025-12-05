const API_BASE_URL = "http://localhost:8000";

export async function getResolutions() {
  const res = await fetch(`${API_BASE_URL}/resolutions`);
  if (!res.ok) {
    throw new Error("Kunde inte hämta nyårslöften");
  }
  return res.json();
}

export async function createResolution(text) {
  const res = await fetch(`${API_BASE_URL}/resolutions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  if (!res.ok) {
    throw new Error("Kunde inte skapa nyårslöfte");
  }
  return res.json();
}

export async function deleteResolution(id) {
  const res = await fetch(`${API_BASE_URL}/resolutions/${id}`, {
    method: "DELETE",
  });
  if (!res.ok) {
    throw new Error("Kunde inte ta bort nyårslöfte");
  }
  return res.json();
}