<template>
    <div>
        <h1>Antecedentes</h1>
        <div class="grid grid-cols-1  md:grid-cols-2 m-4">
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Alergias: {{ record.allergies }}. {{ newRecordAllergies
                    }}</label>
                <UTextarea v-model="newRecordAllergies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Patologias: {{ record.pathologies }}. {{ newRecordPathologies
                    }}</label>
                <UTextarea v-model="newRecordPathologies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Medicacion:{{ record.medications }}. {{ newRecordMedications }}
                </label>
                <UTextarea v-model="newRecordMedications" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium text-gray-700">Liquidos y Alimentos: {{ record.liquids_foods }}.
                    {{ newRecordLiquids_foods }}</label>
                <UTextarea v-model="newRecordLiquids_foods" variant="outline" />
            </div>

        </div>
        <div class="m-2 g-4">
            <UButton class="mt-2" variant="soft" block @click="saveHistory">Guardar</UButton>

        </div>

    </div>

</template>

<script lang="ts" setup>

const toast = useToast()


const modelValue = defineProps({
    calendarEvent: Object,
})

const record = ref<any>({})
const newRecordAllergies = ref('')
const newRecordPathologies = ref('')
const newRecordMedications = ref('')
const newRecordLiquids_foods = ref('')

onMounted(() => {
    if (modelValue.calendarEvent?.patient) {
        record.value = modelValue.calendarEvent?.patient

    } else {
        record.value = modelValue.calendarEvent

    }
})


const saveHistory = async () => {

    try {
        const response = await $fetch(`api/thirds/${record.value.id}`, {
            method: 'PATCH',
            body: JSON.stringify({
                allergies: record?.value.allergies + '. ' + newRecordAllergies?.value,
                pathologies: record?.value.pathologies + '. ' + newRecordPathologies?.value,
                medications: record?.value.medications + '. ' + newRecordMedications?.value,
                liquids_foods: record?.value.liquids_foods + '. ' + newRecordLiquids_foods?.value
            })
        });

        if (response) {
            // Éxito: limpiar los campos
            newRecordAllergies.value = '';
            newRecordPathologies.value = '';
            newRecordMedications.value = '';
            newRecordLiquids_foods.value = '';
        }
        if (modelValue.calendarEvent?.patient) {
            record.value = modelValue.calendarEvent?.patient

        } else {
            record.value = modelValue.calendarEvent

        }
    } catch (error: any) {
        // Error: capturar el mensaje y mostrarlo en un "toast"
        const errorMessage = error.message || 'Error desconocido';


    }
};

</script>
<style></style>