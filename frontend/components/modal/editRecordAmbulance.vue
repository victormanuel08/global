<template>
    <UCard class="m-6">
        <div class="flex flex-cols-2 gap-4 md:grid-cols-2 m-2">
            <UTabs :items="items" class="w-full" @change="onChange">
                <template #default="{ item, index }">
                    <div :class="isActive(item) ? 'active-tab' : 'inactive-tab'">
                        
                        <span v-if="creationPanelSelected.title === item.panel" style="color: blue; font-size: 16px;">
                            <Icon :name="item.icon" style="color: blue; font-size: 1em;" class="w-4 h-4 flex-shrink-0" />
                            {{ item.label }}
                        </span>
                        <span v-else>
                            <Icon :name="item.icon" style="color: blue; font-size: 2em;" class="w-4 h-4 flex-shrink-0" />
                        </span>
                        
                    </div>
                </template>
            </UTabs>
        </div>
        <div class="p-4">
            <component :is="creationPanelSelected.component" :calendar-event="props.calendarEvent" />
        </div>
    </UCard>
</template>
<script setup lang="ts">
import { PanelReports, PanelBasic, PanelThird, PanelPregnancy, PanelDocuments,  PanelObjects,  PanelRecords, PanelInjuries } from "#components";
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
    label: 'Datos Evento',
    icon: 'uil:exclamation-triangle',
    panel: 'Basic',
},
{
    label: 'Lesiones',
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

</style>
