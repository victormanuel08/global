<template>
    <UCard class="m-6">
        <div class="flex flex-cols-2 gap-4 md:grid-cols-2 m-2">
            <UTabs :items="items" class="w-full" @change="onChange">
                <template #default="{ item, index }">
                    <div >                        
                        <Icon :name="item.icon" style="color: blue; font-size: 1.5em;"  />
                        <span 
                             style="color: blue;">
                              {{ item.label }}
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
import { PanelReports, PanelBasicRecord,  PanelThird, PanelPregnancy,  PanelProcedures, PanelRecords,PanelEvolution,PanelGeneral,PanelSystems } from "#components";
const props = defineProps({
    calendarEvent: Object,
})
onMounted(() => { 
    console.log('onMountedce', props.calendarEvent)
    

    if (props.calendarEvent?.third_medic_full.speciality_full.code === "012") {       
        items.push({
            label: 'Evolucion',
            icon: 'i-heroicons-information-circle',
            panel: 'Evolution',
        });
    }     
    creationPanelSelected.value = creationPanels['Third']
});
const isActive = (item:any) => { 
  return item.panel === creationPanelSelected.value;
};
const creationPanels = {
    'Basic': markRaw({
        component: PanelBasicRecord,
        title: 'Basic',
    }),
    'Third': { component: PanelThird, title: 'Datos Paciente' },
    'Records': { component: PanelRecords, title: 'Records' },
    'Systems': markRaw({
        component: PanelSystems,
        title: 'Sistemas',
    }),
    'General': { component: PanelGeneral,title: 'General' },
 
    'Pregnancy': { component: PanelPregnancy, title: 'Maternidad' },
    'Evolution': { component: PanelEvolution, title: 'Evolucion' },   
    'Procedures': markRaw({
        component: PanelProcedures,
        title: 'Procedures',
    }),     
    'Reports': { component: PanelReports, title: 'Reports' },
}
const creationPanelSelected = ref(creationPanels['Third'])
const items = [
{
    label: 'Datos Paciente',
    icon: 'i-heroicons-information-circle',
    panel: 'Third',
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

{
    label: 'Procedimientos',
    icon: 'uil:surgical-mask',
    panel: 'Procedures',
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
.active-tab {
  font-size: 16px;
}
.inactive-tab {
  font-size: 16px;
}
.text-md {
  font-size: 16px;
}
</style>

