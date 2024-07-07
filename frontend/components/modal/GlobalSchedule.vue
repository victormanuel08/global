<template>
    <UModal v-model="isOpen">
        <UCard>
            <template #header>
                <div class="grid grid-cols-3 gap-4">

                    <div>
                        <UButton @click="mode = 'slot'" v-if="mode === 'creating'">Volver</UButton>
                    </div>
                    <div class='justify-center'>
                        <label>Agendamiento </label>
                    </div>
                    <div class="flex justify-end gap-4">
                        <UDropdown :items="dropdownCreateItems" :popper="{ placement: 'bottom-start' }">
                            <UButton color="white" label="Acciones" trailing-icon="i-heroicons-chevron-down-20-solid" />
                        </UDropdown>
                    </div>
                </div>
            </template>
            <div v-if="mode === 'creating'">
                <h4>{{ creationPanelSelected.title }}</h4>
                <component @update:modalShow="isOpen = $event" :is="creationPanelSelected.component" :calendar-event="calendarEvent" />
            </div>
            <div v-if="mode === 'slot'">
                <slot></slot>
            </div>
        </UCard>
    </UModal>
</template>

<script setup lang="ts">
import {PanelStore} from "#components";
const isOpen = defineModel<boolean>({ default: false })
const mode = ref('slot' as 'slot' | 'creating')
const props = defineProps({
    calendarEvent: Object,

})

let dropdownItemsLoaded = false

watch(() => props.calendarEvent, (value) => {
    if (value && !dropdownItemsLoaded) {
        dropdownCreateItems.push([
  

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