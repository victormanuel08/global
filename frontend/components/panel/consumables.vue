
<template>
    <div class="max-w-5xl mx-auto">
        <UCard class="my-2">
            <template #header>
                <div class="flex justify-between items-center">
                    <h2 class="font-bold">Insumos</h2>
                    <div class="flex gap-3 my-3">            
                        <UInput v-model="search" placeholder="Buscar" />
                        <UPagination v-model="pagination.page" :page-count="pagination.pageSize"
                            :total="pagination.resultsCount" />
                    </div>
                </div>
            </template>

            <!-- Mensaje cuando no hay datos -->
            <div class="flex justify-center items-center">
                <h3 v-if="records.length === 0">No hay Insumos</h3>
            </div>

            <!-- Tabla de medicamentos -->
            <div style="overflow: auto;">
                <table class="table-auto w-full permission-table">
                    <thead>
                        <tr>
                            <th :class="ui.th">Insumo</th>
                            <th :class="ui.th">Cantidad</th>                            
                            <th :class="ui.th">Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Medicamentos existentes -->
                        <tr v-for="(record, index) in records" :key="record.id">
                            <td :class="ui.td">
                                <label>{{ record.service_full.description }}</label>
                            </td>
                            <td :class="ui.td">
                                <label>{{ record.quantity }}</label>
                            </td>
               
                            <td :class="ui.td">
                                <span @click="deleteRecord(record.id)" :class="ui.span">🗑️</span>
                            </td>
                        </tr>

                        <!-- Formulario para agregar medicamento -->
                        <tr>
                            <td :class="ui.td">
                                <SelectServices class="border rounded p-1 w-72" v-model="service_full"
                                    :specialities="speciality" />
                            </td>
                            <td :class="ui.td">
                                <UInput v-model="newMedicament.quantity" placeholder="Cantidad"
                                    class="border rounded p-1" />
                            </td>
           
                            <td :class="ui.td">
                                <span @click="createRecord" :class="ui.span">💾</span>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </UCard>
    </div>
</template>

<script setup lang="ts">
// Tipos
interface Medicament {
    record: any;
    service: any;
    quantity: number;

}
const props = defineProps({
    calendarEvent: Object,
})

const speciality = ref<any>({})
const service_full = ref<any>({})

// Cargar especialidades
const loadSpeciality = async () => {
    const response = await $fetch<any>('api/specialities/', {
        query: {
            code: '31'
        }
    });
    speciality.value = response.results[0];
}

// Variables reactivas
const newMedicament = ref<Medicament>({
    record: 0,
    service: 0,
    quantity: 0,

});
const toast = useToast(); // Para notificaciones

// Hook de paginación
const {
    data: records,
    pagination,
    search,
    refresh
} = usePaginatedFetch<any>('/api/medicaments/?record=' + (props.calendarEvent?.id ?? ''),);

// Función para eliminar un medicamento
const deleteRecord = async (id: number) => {
    if (confirm('¿Estás seguro de eliminar este Insumo?')) {
        try {
            await $fetch(`api/medicaments/${id}/`, { method: 'DELETE' });
            toast.add({ title: 'Insumo eliminado correctamente.' });
            refresh();
        } catch (error) {
            console.error('Error al eliminar:', error);
            toast.add({ title: 'Error al eliminar el Insumo.' });
        }
    }
};

// Función para crear un nuevo medicamento
const createRecord = async () => {
    if (!newMedicament.value.service || !newMedicament.value.quantity ) {
        toast.add({ title: 'Por favor, completa todos los campos antes de guardar.' });
        return;
    }

    if (confirm('¿Estás seguro de agregar este Insumo?')) {
        try {
            await $fetch('/api/medicaments/', {
                method: 'POST',
                body: {
                    record: props.calendarEvent?.id,
                    service: newMedicament.value.service,  // Se envía el ID aquí
                    quantity: parseInt(newMedicament.value.quantity.toString()),

                },
            });
            toast.add({ title: 'Insumo creado correctamente.' });
            refresh();
            resetForm();
        } catch (error) {
            console.error('Error al crear:', error);
            toast.add({ title: 'Error al crear el Insumo.' });
        }
    }
};

// Función para resetear el formulario
const resetForm = () => {
    newMedicament.value = {
        record: props.calendarEvent?.id || 0,
        service: 0, // Almacenará directamente el ID
        quantity: 0,

    };
};

// Observa los cambios en `service_full` y asigna el ID correspondiente
watch(
    () => service_full.value,
    (newValue) => {
        if (newValue && newValue.id) {
            newMedicament.value.service = newValue.id;  // Asigna solo el ID
        }
    }
);

// Estilos
const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    span: 'cursor-pointer',
};

// Inicialización
onMounted(() => {
    loadSpeciality();
    refresh();
});
</script>




<style scoped>
.table-auto {
    width: 100%;
    border-collapse: collapse;
}

.permission-table th,
.permission-table td {
    text-align: center;
}
</style>
