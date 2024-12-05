<template>
    <div class="max-w-5xl mx-auto">
        <UCard class="my-2">
            <template #header>
                <div class="flex justify-between items-center">
                    <h2 class="font-bold">Medicamentos</h2>
                    <div class="flex gap-3 my-3">
                        <UButton style="width: 80px; white-space: normal; text-align: right;" class="rounded-full"
                            variant="soft" @click="downloadReport">
                            Descargar
                        </UButton>
                        <UButton style="width: 100px; white-space: normal; text-align: right;" class="rounded-full"
                            variant="soft" @click="sendEmail">
                            Enviar Email
                        </UButton>
                        <UInput v-model="search" placeholder="Buscar" />
                        <UPagination v-model="pagination.page" :page-count="pagination.pageSize"
                            :total="pagination.resultsCount" />
                    </div>
                </div>
            </template>

            <!-- Mensaje cuando no hay datos -->
            <div class="flex justify-center items-center">
                <h3 v-if="records.length === 0">No hay Medicamentos</h3>
            </div>

            <!-- Tabla de medicamentos -->
            <div style="overflow: auto;">
                <table class="table-auto w-full permission-table">
                    <thead>
                        <tr>
                            <th :class="ui.th">Medicamento</th>
                            <th :class="ui.th">Cantidad</th>
                            <th :class="ui.th">Dosis</th>
                            <th :class="ui.th">Vía de Administración</th>
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
                                <label>{{ record.dose }}</label>
                            </td>
                            <td :class="ui.td">
                                <label>{{ record.route }}</label>
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
                                <UInput v-model="newMedicament.dose" placeholder="Dosis" class="border rounded p-1" />
                            </td>
                            <td :class="ui.td">
                                <UInput v-model="newMedicament.route" placeholder="Vía de Administración"
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
    dose: string;
    route: string;
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
    dose: '',
    route: '',
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
    if (confirm('¿Estás seguro de eliminar este Medicamento?')) {
        try {
            await $fetch(`api/medicaments/${id}/`, { method: 'DELETE' });
            toast.add({ title: 'Medicamento eliminado correctamente.' });
            refresh();
        } catch (error) {
            console.error('Error al eliminar:', error);
            toast.add({ title: 'Error al eliminar el Medicamento.' });
        }
    }
};

// Función para crear un nuevo medicamento
const createRecord = async () => {
    if (!newMedicament.value.service || !newMedicament.value.quantity || !newMedicament.value.dose || !newMedicament.value.route) {
        toast.add({ title: 'Por favor, completa todos los campos antes de guardar.' });
        return;
    }

    if (confirm('¿Estás seguro de agregar este Medicamento?')) {
        try {
            await $fetch('/api/medicaments/', {
                method: 'POST',
                body: {
                    record: props.calendarEvent?.id,
                    service: newMedicament.value.service,  // Se envía el ID aquí
                    quantity: parseInt(newMedicament.value.quantity.toString()),
                    dose: newMedicament.value.dose,
                    route: newMedicament.value.route,
                },
            });
            toast.add({ title: 'Medicamento creado correctamente.' });
            refresh();
            resetForm();
        } catch (error) {
            console.error('Error al crear:', error);
            toast.add({ title: 'Error al crear el Medicamento.' });
        }
    }
};

// Función para resetear el formulario
const resetForm = () => {
    newMedicament.value = {
        record: props.calendarEvent?.id || 0,
        service: 0, // Almacenará directamente el ID
        quantity: 0,
        dose: '',
        route: '',
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
const downloadReport = async () => {
  try {
    const response = await fetch("api/api/printpdf/medicamentos/" + props.calendarEvent?.id, {
      method: 'GET',
      headers: {
        'Accept': 'application/pdf', // Asegúrate de aceptar el tipo de contenido correcto
      },
    });

    if (!response.ok) {
      // Leer el mensaje de error devuelto por el backend
      const errorText = await response.text();
      console.error('Error al descargar el archivo:', errorText);

      // Mostrar el mensaje de error en el toast
      toast.add({ title: `Error al descargar: ${errorText}` });
      return;
    }

    const blob = await response.blob();
    const filename = 'Formula ' + props.calendarEvent?.id + '.pdf';

    // Crear un enlace para descargar el archivo
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = filename;
    link.click();

    // Revocar la URL del objeto después de un tiempo
    setTimeout(() => {
      window.URL.revokeObjectURL(link.href);
    }, 250);

    toast.add({ title: 'Archivo descargado correctamente.' });
  } catch (error) {
    console.error('Error en la descarga:', error);
    toast.add({ title: 'Ocurrió un error al intentar descargar el archivo.' });
  }
};


const sendEmail = async () => {
  try {
    // Verifica que el registro tenga un ID válido
    if (!props.calendarEvent || !props.calendarEvent?.id) {
      toast.add({ title: 'No se encontró un registro válido para enviar el correo.' });
      return;
    }

    // Crea el objeto FormData con los datos necesarios
    const formData = new FormData();
    formData.append('id', props.calendarEvent.id); // ID del registro
    formData.append('type', 'medicamentos'); // Tipo de template, aquí es 'medicamentos'
    formData.append('asunto', "Formula Medica"); // Asunto del correo
    formData.append('mensaje', "messaje.value"); // Mensaje personalizado
    formData.append('destinatario', 'rinconvargasvictormanuel@gmail.com'); // Destinatario predeterminado o dinámico

    // Realiza la solicitud al endpoint del backend
    const response = await fetch('/api/sendemail/', {
      method: 'POST',
      body: formData,
    });
    const text = await response.text();
    // Maneja la respuesta del servidor
    if (!response.ok) {
      // Leer el mensaje de error devuelto por el backend
      
      console.error( text);

      // Mostrar el mensaje de error en el toast
      toast.add({ title: ` ${text}` });
      return;
    }else{
        toast.add({ title: ` ${text}` });
    }
   
  } catch (error) {
    console.error('Error en la solicitud:', error);
    //toast.add({ title: 'Ocurrió un error al enviar el correo. Revisa la consola para más detalles.' });
  }
};


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
