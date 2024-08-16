<template>

    <h1>Informacion Paciente <span @click="showModalThird(record.third_patient_full)"
            v-if="record.third_patient_full?.type_document !== 'AS'">🖊️</span></h1>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-4" v-if="record.third_patient_full?.type_document === 'AS'">
        <div>
            <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
            {{ record.third_patient_full?.nit }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Nombre: </label>
            {{ record.third_patient_full?.name }} {{ record.third_patient_full?.second_name }} {{
                record.third_patient_full?.last_name }} {{ record.third_patient_full?.second_last_name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Tercero: </label>
            <SelectThird :placeholder="'Tercero'" :third-type="'P'" v-model="record.third_patient_full"
                @change="saveItem(record.id, 'third_patient', record.third_patient_full?.id)" />
        </div>
    </div>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-4" v-if="record.third_patient_full?.type_document !== 'AS'">
        <div>
            <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
            {{ record.third_patient_full?.nit }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Nombre: </label>
            {{ record.third_patient_full?.name }} {{ record.third_patient_full?.second_name }} {{
                record.third_patient_full?.last_name }} {{ record.third_patient_full?.second_last_name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
            {{ record.third_patient_full?.city_birth_full?.name }} - {{ record.third_patient_full?.date_birth }} ({{
                record.third_patient_full?.year_old }} años)
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Telefono:</label>
            {{ record.third_patient_full?.phone }}

        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Etnia: </label>
            {{ record.third_patient_full?.etnia_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Tipo de Sangre</label>
            {{ record.third_patient_full?.blood_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Sexo: </label>
            {{ record.third_patient_full?.sex_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Zona: </label>
            {{ record.third_patient_full?.zone_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Ocupacion: </label>
            {{ record.third_patient_full?.occupation_full?.name }}
        </div>

    </div>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-2 mt-4" v-if="record.third_patient_full?.type_document !== 'AS'">
        <div>
            <label class="block text-sm font-medium text-gray-700">Direccion:</label>
            {{ record.third_patient_full?.address }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Email:</label>
            {{ record.third_patient_full?.email }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Edicion Tercero:  <span @click="showModalThird('')">➕</span></label>


            <SelectThird :placeholder="'Tercero'" :third-type="'P'" v-model="record.third_patient_full"
                @change="saveItem(record.id, 'third_patient', record.third_patient_full.id)" />

        </div>

    </div>
    <div v-if="record.third_patient_full?.type_document !== 'AS'" class="mt-3">
        <h1>Antecedentes</h1>
        <div class="grid grid-cols-1  md:grid-cols-2 m-4">
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Alergias: {{ record.third_patient_full?.allergies }}. {{
                    newRecordAllergies
                }}</label>
                <UTextarea v-model="newRecordAllergies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Patologias: {{ record.third_patient_full?.pathologies }}.
                    {{ newRecordPathologies
                    }}</label>
                <UTextarea v-model="newRecordPathologies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Medicacion:{{ record.third_patient_full?.medications }}. {{
                    newRecordMedications }}
                </label>
                <UTextarea v-model="newRecordMedications" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium text-gray-700">Liquidos y Alimentos: {{
                    record.third_patient_full?.liquids_foods }}.
                    {{ newRecordLiquidsFoods }}</label>
                <UTextarea v-model="newRecordLiquidsFoods" variant="outline" />
            </div>

        </div>
        <div class="m-2 g-4">
            <UButton class="mt-2" variant="soft" block @click="saveHistory">Guardar</UButton>

        </div>

    </div>
    <ModalEditThird :third="thirdSelectedThird" :typeT="'P'" v-model="isThird" />

</template>

<script lang="ts" setup>

const isThird = ref(false)
const thirdSelectedThird = ref<any>({})
const newRecordAllergies = ref('')
const newRecordPathologies = ref('')
const newRecordMedications = ref('')
const newRecordLiquidsFoods = ref('')


const props = defineProps({
    calendarEvent: Object,
})

const record = ref<any>({})

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    record.value = response   
}

onMounted(() => {
    console.log('onMountedce2', props.calendarEvent)
    record.value = props.calendarEvent
    fetchRecord(props.calendarEvent?.id)
})

await record.value;

const showModalThird = (value: any) => {
    thirdSelectedThird.value = value
    isThird.value = true
}



const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });


};

const saveHistory = async () => {
    try {
        const response = await $fetch(`api/thirds/${record.value.third_patient_full.id}`, {
            method: 'PATCH',
            body: JSON.stringify({
                allergies: record?.value.third_patient_full?.allergies + '. ' + newRecordAllergies?.value,
                pathologies: record?.value.third_patient_full?.pathologies + '. ' + newRecordPathologies?.value,
                medications: record?.value.third_patient_full?.medications + '. ' + newRecordMedications?.value,
                liquids_foods: record?.value.third_patient_full?.liquids_foods + '. ' + newRecordLiquidsFoods?.value
            })
        });
        fetchRecord(record.value.id);
        if (response) {
            newRecordAllergies.value = '';
            newRecordPathologies.value = '';
            newRecordMedications.value = '';
            newRecordLiquidsFoods.value = '';
        }
    } catch (error: any) {
        const errorMessage = error.message || 'Error desconocido';
    }
};

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

</script>

<style scoped>
p {
    font-size: 8px;
}
</style>
