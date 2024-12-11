<template>
    <div>
        <h1>Antecedentes</h1>
        <div class="grid grid-cols-1  md:grid-cols-2 m-4">
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">
                    Alergias: {{ record.allergies }}. {{ newRecordAllergies }}
                </label>
                <UTextarea v-model="newRecordAllergies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">
                    Patologías: {{ record.pathologies }}. {{ newRecordPathologies }}
                </label>
                <UTextarea v-model="newRecordPathologies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">
                    Medicación: {{ record.medications }}. {{ newRecordMedications }}
                </label>
                <UTextarea v-model="newRecordMedications" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium text-gray-700">
                    Líquidos y Alimentos: {{ record.liquids_foods }}. {{ newRecordLiquids_foods }}
                </label>
                <UTextarea v-model="newRecordLiquids_foods" variant="outline" />
            </div>
        </div>
        <div class="m-2 g-4">
            <UButton class="mt-2" variant="soft" block @click="saveHistory">Guardar</UButton>
        </div>
    </div>
</template>

<script lang="ts" setup>
const toast = useToast();

const modelValue = defineProps({
    calendarEvent: Object,
});

const record = ref<any>({});
const newRecordAllergies = ref('Niega alergias');
const newRecordPathologies = ref('Niega patologías');
const newRecordMedications = ref('Niega medicación');
const newRecordLiquids_foods = ref('Niega líquidos y alimentos');

onMounted(() => {
    record.value = modelValue.calendarEvent?.patient || modelValue.calendarEvent || {};
});

const saveHistory = async () => {
    const body: Record<string, string> = {};

    // Incluir los valores solo si han sido modificados
    if (newRecordAllergies.value !== 'Niega alergias') {
        body.allergies = `${record.value.allergies || ''}. ${newRecordAllergies.value}`.trim();
    }
    if (newRecordPathologies.value !== 'Niega patologías') {
        body.pathologies = `${record.value.pathologies || ''}. ${newRecordPathologies.value}`.trim();
    }
    if (newRecordMedications.value !== 'Niega medicación') {
        body.medications = `${record.value.medications || ''}. ${newRecordMedications.value}`.trim();
    }
    if (newRecordLiquids_foods.value !== 'Niega líquidos y alimentos') {
        body.liquids_foods = `${record.value.liquids_foods || ''}. ${newRecordLiquids_foods.value}`.trim();
    }

    // Si no hay cambios, informar al usuario y detener la operación
    if (Object.keys(body).length === 0) {
        toast.add({ title: 'No hay cambios para guardar.', severity: 'info' });
        return;
    }

    try {
        const response = await $fetch(`api/thirds/${record.value.id}`, {
            method: 'PATCH',
            body: JSON.stringify(body),
        });

        if (response) {
            toast.add({ title: 'Historial guardado con éxito.', severity: 'success' });

            // Limpiar solo los campos modificados
            if (body.allergies) newRecordAllergies.value = 'Niega alergias';
            if (body.pathologies) newRecordPathologies.value = 'Niega patologías';
            if (body.medications) newRecordMedications.value = 'Niega medicación';
            if (body.liquids_foods) newRecordLiquids_foods.value = 'Niega líquidos y alimentos';

            // Actualizar el registro local
            record.value = { ...record.value, ...body };
        }
    } catch (error: any) {
        toast.add({ title: error.message || 'Error al guardar el historial.', severity: 'error' });
    }
};
</script>
