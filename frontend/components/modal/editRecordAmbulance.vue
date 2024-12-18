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
                    <Icon :name="item.icon" class="w-4 h-4 flex-shrink-0" />
                    <span>{{ item.label }}</span>
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
    PanelReports,
    PanelBasic,
    PanelThird,
    PanelPregnancy,
    PanelDocuments,
    PanelObjects,
    PanelRecords,
    PanelInjuries,
    PanelConsumables,
} from "#components";

const props = defineProps({
    calendarEvent: Object,
});

onMounted(() => {
    //console.log("onMountedce", props.calendarEvent);
    creationPanelSelected.value = creationPanels["Third"];
    selectedPanel.value = "Third"; // Inicializamos con el panel actual
});

// Configuración de paneles y su contenido
const creationPanels = {
    Third: { component: PanelThird, title: "Third" },
    Records: { component: PanelRecords, title: "Records" },
    Basic: { component: PanelBasic, title: "Basic" },
    Pregnancy: { component: PanelPregnancy, title: "Pregnancy" },
    Injuries: { component: PanelInjuries, title: "Injuries" },
    Objects: { component: PanelObjects, title: "Objects" },
    Consumables: { component: PanelConsumables, title: "Consumables" },
    Documents: { component: PanelDocuments, title: "Documents" },
    Reports: { component: PanelReports, title: "Reports" },
};

const items = [
    { label: "Datos Paciente", icon: "uil:user", panel: "Third" },
    { label: "Historia Medica", icon: "uil:file-medical", panel: "Records" },
    { label: "Evento", icon: "uil:exclamation-triangle", panel: "Basic" },
    { label: "Clinica", icon: "uil:file-medical", panel: "Injuries" },
    { label: "Objetos", icon: "uil:briefcase", panel: "Objects" },
    { label: "Documentos", icon: "uil:document", panel: "Documents" },
    { label: "Consumibles", icon: "uil:document", panel: "Consumables" },
    { label: "Reportes", icon: "uil:document", panel: "Reports" },
];

const creationPanelSelected = ref(creationPanels["Third"]);
const selectedPanel = ref("Third");

function onChange(index: number) {
    const item = items[index];
    creationPanelSelected.value = creationPanels[item.panel];
    selectedPanel.value = item.panel;
    //console.log("onChange", creationPanelSelected.value.title);
}

function onChangeDropdown() {
    const panel = items.find((item) => item.panel === selectedPanel.value);
    if (panel) {
        creationPanelSelected.value = creationPanels[panel.panel];
        //console.log("onChangeDropdown", creationPanelSelected.value.title);
    }
}

const isActive = (item: any) => {
    return item.panel === creationPanelSelected.value;
};
</script>

<style scoped>
/* Estilo de las pestañas */
.tabs-container {
    display: flex;
    justify-content: flex-start;
    border-bottom: 2px solid #e0e0e0;
    padding: 0 8px;
}

.tab-item {
    padding: 12px 16px;
    cursor: pointer;
    font-size: 14px;
    color: #757575;
    text-align: center;
    border-radius: 20px;
    margin: 0 8px;
    transition: color 0.3s, background-color 0.3s, box-shadow 0.3s;
}

.tab-item.active {
    color: blue;
    background-color: #e0e0e0;
    box-shadow: 0 4px 8px rgba(0, 0, 255, 0.2);
}

.tab-item:hover {
    color: blue
}

/* Estilo para el select */
select {
    padding: 10px;
    border-radius: 8px;
    background-color: #f9f9f9;
    font-size: 16px;
    color: #333;
    border: 1px solid #ccc;
    transition: all 0.3s ease;
    appearance: none; /* Eliminar estilo por defecto de los navegadores */
}

select:focus {
    border-color: blue;
    outline: none;
}

/* Estilo de los iconos */
select::-ms-expand {
    display: none;
}

@media (max-width: 768px) {
    .tabs-container {
        display: none; /* Ocultar las pestañas tradicionales */
    }
}
</style>
