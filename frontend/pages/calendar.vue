<template>
    <div class = "m-4">
        <FullCalendar :options="calendarOptions" />
    </div>


</template>
<script setup>

import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
import esLocale from '@fullcalendar/core/locales/es';


const originalScheduleds = ref([])

const modalOpen = ref({
    createSchedule: false,
    editSchedule: false
})

const modalClosedHandler = (value) => {
    if (!value) { // Si el valor es false, significa que la modal se ha cerrado
        updateScheduleHandler();
    }
}

const updateScheduleHandler = async () => {
    getSchedules()
}

const getSchedules = async () => {
    const response = await $fetch('/api/scheduleds/')
    console.log("Response", response.results)
    originalScheduleds.value = response.results
    calendarOptions.events = response.results.map((item) => ({       
        id: item.id,
        title: item.third_patient,
        date: item.date,
        display: 'block',
        backgroundColor: item.confirmed === '0' ? 'red' : 'green'
    }))
    console.log("Scheduleds", calendarOptions.events)    
}

const calendarOptions = {
    plugins: [dayGridPlugin, interactionPlugin],
    initialView: "dayGridMonth",
    locale: esLocale,
    events: [{ id: 1, title: "event 1", date: "2024-07-01", time: "10:00:00"}],
    editable: true,
    eventClick: (info) => {
        console.log("Event Calendar", info.event.id)
        modalOpen.value.editSchedule = true
    },
    dateClick: (info) => {
        console.log("Date Calendar", info.dateStr)
        modalOpen.value.createSchedule = true
    }
}

onMounted(async () => {
    await  getSchedules()
})

</script>
