<template>
    <div class = "m-4">
        <FullCalendar :options="calendarOptions" />
    </div>
</template>
<script setup>

import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";

const originalScheduleds = ref([])

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
    events: [{ id: 1, title: "event 1", date: "2024-07-01"}],
    editable: true,
    eventClick: (info) => {
        console.log("Event Calendar", info.event.id)
    },
    eventDidMount: async (info) => {
        //await getSchedules(),
        console.log("EventDidMount", info)
    },
    eventDrop: (info) => {
        console.log("EventDrop", info)
    },
    eventChange: (info) => {
        console.log("EventChange", info.dateStr)
    }
}

onMounted(async () => {
    await getSchedules()
})

</script>
