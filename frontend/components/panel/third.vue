<template>
    <div>
        <h1>Informacion Paciente</h1>
        <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
            <div>
                <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
                {{ record.nit }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Nombre: </label>
                {{ record.name }} {{ record.second_name }} {{ record.last_name }} {{ record.second_last_name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
                {{ record.city_birth_full?.name }} - {{ record.date_birth }} ({{ record.year_old }} años)
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Telefono:</label>
                {{ record.phone }}

            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Etnia: </label>
                {{ record.etnia_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Tipo de Sangre</label>
                {{ record.blood_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Sexo: </label>
                {{ record.sex_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Zona: </label>
                {{ record.zone_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Ocupacion: </label>
                {{ record.occupation_full?.name }}
            </div>

        </div>
        <div class="grid grid-cols-3 gap-4 md:grid-cols-3 mt-4">
            <div>
                <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                {{ record.address }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Email:</label>
                {{ record.email }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Edicion Tercero:</label>
                {{ record.eps_full?.name }}
                <span @click="showModalThird(record)" >🖊️</span>
            </div>
        </div>

    </div>
    <ModalEditThird  :third="thirdSelected"   :typeT="'P'" @close="handleModalClose" v-model="isThird" />
</template>

<script lang="ts" setup>

const isThird = ref(false)
const thirdSelected = ref<any>({})  

const showModalThird = (value: any) => {
    thirdSelected.value = value
    console.log('showModalThird',thirdSelected)    
    isThird.value = true
}

const modelValue = defineProps({
    calendarEvent: Object,
})
const record = ref<any>({})
onMounted(() => {
    if (modelValue.calendarEvent?.patient) {
        record.value = modelValue.calendarEvent?.patient
        console.log('CALENDARIO', record.value)
    } else {
        record.value = modelValue.calendarEvent
        console.log('THIRD', record.value)
    }
    if (record.value.record) {
        console.log('RECORD RECORD',record.value)
        console.log('EXISTE RECORD')
    } else {
        createRecord()
        console.log('CREAR RECORD')
    }
})

const createRecord = async () => {
    const response = await $fetch('api/records/', {
        method: 'POST',
        body: {
            third_patient: record.value?.id,
            third_medic: record.value?.id, //deberia cargarlo del user       
        },
    })
    console.log('RESPONSE', response.id)
    record.value.record = response

    console.log('RECORDRESPONSE', record.value)
}

</script>
<style></style>