<template>
    <div class = "m-4">
        <FullCalendar :options="calendarOptions" />
    </div>
</template>
<script setup>
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";

onMounted(async () => {
    await getSchedules();
})


const getSchedules = async () => {
    const response = await $fetch('/api/scheduleds/');
    console.log('Original Schedules', response.results);
    const calendarOptions = {
        plugins: [dayGridPlugin, interactionPlugin],
        initialView: "dayGridMonth",
        events: response.results.map((scheduled) => ({
            id: scheduled.id,
            title: scheduled.third_patient_full.name,
            date: scheduled.date,
            
        })),
    };
console.log('Calendar Options', calendarOptions);
}


</script>
