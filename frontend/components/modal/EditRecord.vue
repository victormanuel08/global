<template>
  <UCard class="m-6">
    <!-- Menú adaptable -->
    <div class="mb-4">
      <!-- Dropdown para móviles -->
      <div class="block md:hidden">
        <select
          v-model="selectedPanel"
          class="w-full border border-gray-300 rounded-lg shadow-sm py-2 px-4 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 appearance-none"
          @change="onChangeDropdown"
        >
          <option v-for="(item, index) in items" :key="index" :value="item.panel">
            {{ item.label }}
          </option>
        </select>
      </div>

      <!-- Pestañas para pantallas grandes -->
      <div class="hidden md:flex tabs-container">
        <div
          v-for="(item, index) in items"
          :key="index"
          :class="['tab-item', { active: isActive(item) }]"
          @click="onChange(index)"
        >
          <Icon :name="item.icon" class="tab-icon" />
          <span :class="{ 'active-tab': isActive(item) }">{{ item.label }}</span>
        </div>
      </div>
    </div>

    <!-- Panel de contenido -->
    <div class="p-4">
      <component :is="creationPanelSelected.component" :calendar-event="props.calendarEvent" />
    </div>
  </UCard>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import {
  PanelBasicRecord,
  PanelThird,
  PanelPregnancy,
  PanelProcedures,
  PanelGeneral,
  PanelRecords,
  PanelSystems,
  PanelMedicaments,
} from "#components";

const props = defineProps({
  calendarEvent: Object,
});

onMounted(() => {
  creationPanelSelected.value = creationPanels["Third"];
  selectedPanel.value = "Third"; // Inicializar con el primer panel
});

// Configuración de paneles y su contenido
const creationPanels = {
  Third: { component: PanelThird, title: "Datos Paciente" },
  Records: { component: PanelRecords, title: "Historia Médica" },
  BasicRecord: { component: PanelBasicRecord, title: "Datos Consulta" },
  Pregnancy: { component: PanelPregnancy, title: "Maternidad" },
  Systems: { component: PanelSystems, title: "Sistemas de Revisión" },
  General: { component: PanelGeneral, title: "Exámenes Generales" },
  Procedures: { component: PanelProcedures, title: "Procedimientos" },
  Medicaments: { component: PanelMedicaments, title: "Medicamentos" },
};

const items = [
  { label: "Datos Paciente", icon: "uil:user", panel: "Third" },
  { label: "Historia Médica", icon: "uil:file-medical", panel: "Records" },
  { label: "Datos Consulta", icon: "uil:clipboard", panel: "BasicRecord" },
  { label: "Sistemas de Revisión", icon: "uil:medkit", panel: "Systems" },
  { label: "Exámenes Generales", icon: "uil:briefcase", panel: "General" },
  { label: "Procedimientos", icon: "uil:document", panel: "Procedures" },
  { label: "Medicamentos", icon: "uil:report", panel: "Medicaments" },
];

const creationPanelSelected = ref(creationPanels["Third"]);
const selectedPanel = ref("Third");

function onChange(index: number) {
  const item = items[index];
  creationPanelSelected.value = creationPanels[item.panel];
  selectedPanel.value = item.panel;
}

function onChangeDropdown() {
  const panel = items.find((item) => item.panel === selectedPanel.value);
  if (panel) {
    creationPanelSelected.value = creationPanels[panel.panel];
  }
}

function isActive(item: any) {
  return item.panel === creationPanelSelected.value;
}
</script>

<style scoped>
/* Contenedor de pestañas */
.tabs-container {
  display: flex;
  justify-content: flex-start;
  border-bottom: 2px solid #e0e0e0;
  flex-wrap: wrap;
  gap: 10px;
}

/* Estilo de cada pestaña */
.tab-item {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  cursor: pointer;
  font-size: 14px;
  color: #757575;
  text-align: center;
  border-radius: 12px;
  margin: 0 8px;
  transition: all 0.3s ease-in-out;
  gap: 8px;
}

.tab-item.active {
  color: white;
  background-color: #6200ea;
  box-shadow: 0 4px 8px rgba(0, 0, 255, 0.2);
}

.tab-item:hover {
  color: #6200ea;
  background-color: #f0f0f0;
  transform: scale(1.05);
}

.tab-icon {
  font-size: 1.5em;
}

.active-tab {
  font-weight: bold;
  text-transform: uppercase;
}

/* Estilo para el dropdown */
select {
  padding: 10px;
  border-radius: 8px;
  background-color: #f9f9f9;
  font-size: 16px;
  color: #333;
  border: 1px solid #ccc;
  transition: all 0.3s ease;
  appearance: none;
}

select:focus {
  border-color: #6200ea;
  outline: none;
}

select::-ms-expand {
  display: none;
}

/* Responsividad */
@media (max-width: 640px) {
  .tabs-container {
    display: none; /* Ocultar las pestañas en móviles */
  }
}

@media (min-width: 641px) {
  select {
    display: none; /* Ocultar el dropdown en pantallas grandes */
  }
}
</style>

