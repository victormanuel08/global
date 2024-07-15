<template>
    <UModal class="modal">
        <div class="p-4">
            <component :is="creationPanels.Third.component" :calendar-event="$props.calendarEvent" />
        </div>
        <UTabs :items="items" class="w-full">
            <template #default="{ item, index, selected }">
            <div class="flex items-center gap-2 relative truncate">
                <UIcon :name="item.icon" class="w-4 h-4 flex-shrink-0" />
                <span class="truncate">{{ index + 1 }}. {{ item.label }}</span>
                <span v-if="selected" class="absolute -right-4 w-2 h-2 rounded-full bg-primary-500 dark:bg-primary-400" />
            </div>            
            </template>            
        </UTabs>
        <div class="p-4">
            <component :is="creationPanelSelected.component" :calendar-event="$props.calendarEvent" />
        </div>
    </UModal >
</template>
<script setup lang="ts">
import { PanelBasic, PanelSistems, PanelGeneral, PanelThird} from "#components";

const props = defineProps({
    calendarEvent: Object,    
})

const manageClick = (panel: keyof typeof creationPanels) => {
    creationPanelSelected.value = creationPanels[panel]  
    console.log(creationPanelSelected.value)  
}

const creationPanels = {
    'Basic': { component: PanelBasic},
    'Third': { component: PanelThird},
    'Sistems': { component: PanelSistems},
    'General': { component: PanelGeneral},
}

const creationPanelSelected = ref(creationPanels['Basic'])

const items = [{
  label: 'Datos Basicos',
  icon: 'i-heroicons-information-circle',
  click: () => manageClick('Basic')
},
{
  label: 'Revision Sistemas',
  icon: 'i-heroicons-information-circle',
  click: () => manageClick('Sistems')
},{
  label: 'Examen General',
  icon: 'i-heroicons-information-circle',
  click: () => manageClick('General')
}
]

</script>
<style scoped>
.modal{  
  width: 1000%; 
  max-width: 120000px;   
}
</style>
