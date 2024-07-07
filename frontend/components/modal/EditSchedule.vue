<template>
    <ModalGlobalSchedule :calendar-event="calendarEvent" >
        <!-- Por si voy a poner en el sleect lo de agregar observaciones -->
        <PanelEditSchedule :calendar-event="calendarEvent" ></PanelEditSchedule>
    </ModalGlobalSchedule>
</template>

<script setup lang="ts">



const props = defineProps({
    calendarEvent: Object
})
</script>
