<template>
    <div>
        <h1>Datos Basicos</h1>
        <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
            <div>
                <label class="block text-sm font-medium text-gray-700">Fecha:</label>
                {{ formatDateYYYYMMDD(record.date_time) }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Hora: </label>   
                {{ formatDateHHMMSS(record.date_time) }}             
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
                <UInput v-model="modelValue.email" label="Email" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Direccion</label>
                <UInput v-model="modelValue.phone" label="Telefono" />
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>

const modelValue = defineProps({
    calendarEvent: Object,    
})  
const record = ref({})
onMounted(() => {
   retrieveFromApi(modelValue.calendarEvent?.record)   
})  
const retrieveFromApi = async (q: any) => {
    const response = await $fetch<any>("api/records/"+q)
    console.log("Record", record)   
    record.value = response    
}
</script>
<style></style>