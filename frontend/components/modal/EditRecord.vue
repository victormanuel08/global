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
import { PanelBasic, PanelSystems, PanelGeneral, PanelThird, PanelPregnancy, PanelEvolution, PanelHistory, PanelRecords } from "#components";

const props = defineProps({
    calendarEvent: Object,
})

const creationPanels = {
    'Basic': markRaw({
        component: PanelBasic,
        title: 'Basic',
    }),
    'Third': { component: PanelThird },
    'Systems': markRaw({
        component: PanelSystems,
        title: 'Sistemas',
    }),
    'General': { component: PanelGeneral },
    'History': { component: PanelHistory },
    'Records': { component: PanelRecords},
    'Pregnancy': { component: PanelPregnancy },
    'Evolution': { component: PanelEvolution },
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
    label: 'Datos Consulta',
    icon: 'i-heroicons-information-circle',
    panel: 'Basic',
},
{
    label: 'Revision Sistemas',
    icon: 'i-heroicons-information-circle',
    panel: 'Systems',
}, {
    label: 'Examen General',
    icon: 'i-heroicons-information-circle',
    panel: 'General',
},
]

onMounted(() => {
    if (props.calendarEvent?.patient.sex === "F") {       
        items.splice(1, 0, {
            label: 'Maternidad',
            icon: 'i-heroicons-information-circle',
            panel: 'Pregnancy',
        });
    }
    if (props.calendarEvent?.medic.speciality_full.code === "012") {       
        items.push({
            label: 'Evolucion',
            icon: 'i-heroicons-information-circle',
            panel: 'Evolution',
        });
    }     
});

function onChange(index: any) {
    //alert(`${item.panel}`)    
    const item = items[index]
    creationPanelSelected.value = creationPanels[item.panel]
}

</script>
<style scoped>
.modal {
    max-width: 800px;
}
</style>
