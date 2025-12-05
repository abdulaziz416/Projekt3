<script setup>
import { ref, onMounted } from "vue";
import {
  getResolutions,
  createResolution,
  deleteResolution,
} from "./api";

const resolutions = ref([]);
const newText = ref("");
const loading = ref(false);
const error = ref("");

async function loadResolutions() {
  loading.value = true;
  error.value = "";
  try {
    resolutions.value = await getResolutions();
  } catch (e) {
    error.value =
      e?.message || "Något gick fel när nyårslöften skulle hämtas.";
  } finally {
    loading.value = false;
  }
}

async function addResolution() {
  if (!newText.value.trim()) return;

  try {
    const created = await createResolution(newText.value.trim());
    resolutions.value.push(created);
    newText.value = "";
  } catch (e) {
    error.value =
      e?.message || "Kunde inte skapa nyårslöftet.";
  }
}

async function removeResolution(id) {
  try {
    await deleteResolution(id);
    resolutions.value = resolutions.value.filter((r) => r.id !== id);
  } catch (e) {
    error.value =
      e?.message || "Kunde inte ta bort nyårslöftet.";
  }
}

onMounted(loadResolutions);
</script>

<template>
  <main
    style="
      max-width: 600px;
      margin: 2rem auto;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    "
  >
    <h1>Nyårslöften 🎉</h1>

    <section style="margin-bottom: 1.5rem;">
      <h2>Lägg till nytt löfte</h2>
      <form
        @submit.prevent="addResolution"
        style="display: flex; gap: 0.5rem; margin-top: 0.5rem;"
      >
        <input
          v-model="newText"
          type="text"
          placeholder="Skriv ett nyårslöfte..."
          style="flex: 1; padding: 0.5rem;"
        />
        <button type="submit">Spara</button>
      </form>
    </section>

    <section>
      <h2>Dina löften</h2>
      <p v-if="loading">Laddar...</p>
      <p v-if="error" style="color: red;">{{ error }}</p>
      <p v-if="!loading && resolutions.length === 0">
        Inga löften än. Börja med ett! 🎇
      </p>

      <ul v-else style="list-style: none; padding-left: 0;">
        <li
          v-for="resolution in resolutions"
          :key="resolution.id"
          style="
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.4rem;
            padding: 0.4rem 0;
            border-bottom: 1px solid #444;
          "
        >
          <span>{{ resolution.text }}</span>
          <button @click="removeResolution(resolution.id)">
            Ta bort
          </button>
        </li>
      </ul>
    </section>
  </main>
</template>