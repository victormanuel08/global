<template>
    <UCard class="m-6">
        <div class="tabs-container">
            <div v-for="(item, index) in items" :key="index" :class="['tab-item', { active: isActive(item) }]"
                @click="onChange(index)">
                <Icon :name="item.icon" style="font-size: 1.5em;" class="w-4 h-4 flex-shrink-0" />
                <span>{{ item.label }}</span>
            </div>
        </div>
        <div class="p-4">
            <component :is="creationPanelSelected.component" :calendar-event="props.calendarEvent" />
        </div>
    </UCard>
</template>



<script setup lang="ts">
import { PanelReports, PanelBasic, PanelThird, PanelPregnancy, PanelDocuments, PanelObjects, PanelRecords, PanelInjuries } from "#components";
const props = defineProps({
    calendarEvent: Object,
})
onMounted(() => {
    console.log('onMountedce', props.calendarEvent)
    creationPanelSelected.value = creationPanels['Third']

});
const isActive = (item: any) => {
    return item.panel === creationPanelSelected.value;
};
const creationPanels = {
    'Third': { component: PanelThird, title: 'Third' },

    'Records': { component: PanelRecords, title: 'Records' },
    'Basic': markRaw({
        component: PanelBasic,
        title: 'Basic'
    }),

    'Pregnancy': { component: PanelPregnancy, title: 'Pregnancy' },
    'Injuries': { component: PanelInjuries, title: 'Injuries' },
    'Objects': { component: PanelObjects, title: 'Objects' },
    'Documents': { component: PanelDocuments, title: 'Documents' },
    'Reports': { component: PanelReports, title: 'Reports' },
}
const creationPanelSelected = ref(creationPanels['Third'])
const items = [{
    label: 'Datos Paciente',
    icon: 'uil:user',
    panel: 'Third',
},

{
    label: 'Historia Medica',
    icon: 'uil:file-medical',
    panel: 'Records',
},
{
    label: 'Evento',
    icon: 'uil:exclamation-triangle',
    panel: 'Basic',
},
{
    label: 'Clinica',
    icon: 'uil:file-medical',
    panel: 'Injuries',
},
{
    label: 'Objetos',
    icon: 'uil:briefcase',
    panel: 'Objects',
},
{
    label: 'Documentos',
    icon: 'uil:document',
    panel: 'Documents',
},
{
    label: 'Reportes',
    icon: 'uil:document',
    panel: 'Reports',
},
]

function onChange(index: any) {
    const item = items[index]
    creationPanelSelected.value = creationPanels[item.panel]
    console.log('onChange', creationPanelSelected.value.title)
}
</script>
<style scoped>
.tabs-container {
    display: flex;
    justify-content: center;
    border-bottom: 2px solid #e0e0e0;
}

.tab-item {
    padding: 16px 24px;
    cursor: pointer;
    font-size: 16px;
    color: #757575;
    transition: color 0.3s, background-color 0.3s, box-shadow 0.3s;
    text-align: center;
    border-radius: 20px;
    margin: 0 8px;
}

.tab-item.active {
    color: #6200ea;
    background-color: #e0e0e0;
    box-shadow: 0 4px 8px rgba(0, 0, 255, 0.2);
    /* Sombreado azul claro */
}

.tab-item:hover {
    color: #6200ea;
}
</style>
