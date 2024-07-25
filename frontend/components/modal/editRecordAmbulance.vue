<template>
    <UCard class="m-6">
        <div class="flex flex-cols-2 gap-4 md:grid-cols-2 m-2">
            <UTabs :items="items" class="w-full" @change="onChange">
                <template #default="{ item, index }">
                    <div class="flex items-center gap-2 relative truncate">
                        <UIcon :name="item.icon" class="w-4 h-4 flex-shrink-0" />
                        <span class="truncate">{{ index + 1 }}. {{ item.label }}</span>
                    </div>
                </template>
            </UTabs>
        </div>

        <div class="p-4">
            <component :is="creationPanelSelected.component" :calendar-event="$props.calendarEvent" />
        </div>
    </UCard>
</template>
<script setup lang="ts">
import { PanelBasic, PanelSystems, PanelGeneral, PanelThird, PanelPregnancy, PanelEvolution, PanelDocuments, PanelHistory, PanelObjects, PanelProcedures, PanelRecords, PanelInjuries } from "#components";

const props = defineProps({
    calendarEvent: Object,
})

const creationPanels = {
    'Third': { component: PanelThird },
    'History': { component: PanelHistory },
    'Records': { component: PanelRecords },
    'Basic': markRaw({
        component: PanelBasic,
        title: 'Basic',
    }),   
    'Procedures': markRaw({
        component: PanelProcedures,
        title: 'Systems',
    }), 
    'Pregnancy': { component: PanelPregnancy },
    'Objects': { component: PanelObjects },
    'Documents': { component: PanelDocuments },
}

const creationPanelSelected = ref(creationPanels['Third'])

const items = [{
    label: 'Datos Paciente',
    icon: 'i-heroicons-information-circle',
    panel: 'Third',
},
{
    label: 'Antecedentes',
    icon: 'i-heroicons-information-circle',
    panel: 'History',
},
{
    label: 'Historia Medica',
    icon: 'i-heroicons-information-circle',
    panel: 'Records',
},
{
    label: 'Datos Evento',
    icon: 'i-heroicons-information-circle',
    panel: 'Basic',
},
{
    label: 'Lesiones',
    icon: 'i-heroicons-information-circle',
    panel: 'Injuries',
},
{
    label: 'Procedimientos',
    icon: 'i-heroicons-information-circle',
    panel: 'Procedures',
}, 
{
    label: 'Objetos',
    icon: 'i-heroicons-information-circle',
    panel: 'Objects',
},
{
    label: 'Documentos',
    icon: 'i-heroicons-information-circle',
    panel: 'Documents',
},
]

onMounted(() => {
    console.log("modalambulanciaqqqq", props.calendarEvent?.sex)
    if (props.calendarEvent?.sex === "F") {       
        items.splice(1, 0, {
            label: 'Maternidad',
            icon: 'i-heroicons-information-circle',
            panel: 'Pregnancy',
        });
    }    
});

function onChange(index: any) {    
    const item = items[index]
    creationPanelSelected.value = creationPanels[item.panel]
}

</script>
<style scoped>
</style>
