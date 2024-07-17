<template>
    <div>
        <h1>Informacion Paciente</h1>
        <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
            <div>
                <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
                {{ record.nit }}
                <label class="block text-sm font-medium text-gray-700">Sexo: {{ record.sex }}</label>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Nombre: </label>   
                {{ record.name }} {{ record.second_name }} {{ record.last_name }} {{ record.second_last_name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
                {{ record.city_birth }} - {{ record.date_birth }} ({{ record.year_old }} años)
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Telefono:</label>
                {{ record.phone }}
               
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Etnia: </label>   
                {{ record.ethnicity }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Tipo de Sangre</label>
                {{ record.blood_type }} 
            </div>
        </div>
        <div class="flex flex-cols-2 gap-1 md:grid-cols-2">
            <div>
                <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                {{ record.address }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Email:</label>
                {{ record.email }}
            </div>
        </div>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-1">


        </div>
    </div>
</template>

<script lang="ts" setup>

const modelValue = defineProps({
    calendarEvent: Object,    
})  
const record = ref<any>({})
onMounted(() => {
    record.value = modelValue.calendarEvent?.patient    
})  

</script>
<style></style>