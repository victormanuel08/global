<template>

    <UModal v-model="isOpen">
       
    </UModal>
</template>

<script setup lang="ts">
import { PanelStore } from "#components";
const isOpen = defineModel<boolean>({ default: false })
const mode = ref('slot' as 'slot' | 'creating')
const props = defineProps({
    calendarEvent: Object,
})

let dropdownItemsLoaded = false

watch(() => props.calendarEvent, (value: any) => {
    if (value && !dropdownItemsLoaded) {
        dropdownCreateItems.push([           
            {
                label: 'Imprimir',
                icon: "i-heroicons-printer",
                click: () => {
                    console.log("Imprimir")
                }
            },  

            ])
                dropdownItemsLoaded = true
            }
})

const creationPanels = {   
    'store': { component: PanelStore, title: 'Bodega' }, // 'Store  
}

const creationPanelSelected = ref(creationPanels['store'])

const manageClick = (panel: keyof typeof creationPanels) => {
    creationPanelSelected.value = creationPanels[panel]
    mode.value = 'creating'
}

const dropdownCreateItems = [
    [
    {
        label: 'Bodega',
        icon: "i-heroicons-clipboard-document",
        click: () => manageClick('store')
    }
    ],
   
]
</script>