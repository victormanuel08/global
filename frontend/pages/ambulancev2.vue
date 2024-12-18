<template>
  <!-- Renderiza el modal si isAmbulance es verdadero -->
  <ModalEditRecordAmbulance :calendarEvent="recordObject" v-if="isAmbulance" />
</template>

<script lang="ts" setup>
import Swal from 'sweetalert2'; // Importa SweetAlert2

// Usamos el almacenamiento del usuario
const authUserStorage = useAuthUserStorage();
const isAmbulance = ref(false);
const recordObject = ref<any>(null);

// Función para crear un nuevo reporte
const create = async (value: any) => {
  try {
    const response = await $fetch('api/records/', {
      method: 'POST',
      body: {
        third_patient: value,
        third_medic: authUserStorage?.value?.third?.id,
        vehicle: authUserStorage?.value?.third?.vehicle,
        third_driver: authUserStorage?.value?.third?.vehicle_full?.id,
      },
    });
   

    // Guardar el ID del último registro en el almacenamiento
    authUserStorage.value.lastRecord = response.id; // Guardamos el ID o la referencia del último registro

    // Actualizamos el objeto recordObject con el nuevo registro
    recordObject.value = response;
  
  } catch (error) {
   
  }
};

// Obtener el último registro guardado en el almacenamiento
const fetchLastRecord = () => {
  return authUserStorage.value.lastRecord || null; // Regresamos el último ID guardado, si existe
};

// Lógica al montar el componente
onMounted(async () => {
 

  // Verificamos si hay un último registro guardado en el almacenamiento
  const lastRecordId = fetchLastRecord();

  // Si ya existe un registro guardado
  if (lastRecordId) {
    Swal.fire({
      title: '¿Qué deseas hacer?',
      text: 'Parece que tienes un registro abierto. ¿Quieres retomarlo o crear uno nuevo?',
      icon: 'question',
      showCancelButton: true,
      confirmButtonText: 'Nuevo Registro',
      cancelButtonText: 'Retomar Registro',
    }).then((result) => {
      if (result.isConfirmed) {
        // Crear un nuevo registro
        create(2); // Cambia el valor según lo que necesites
        isAmbulance.value = true;
      } else if (result.dismiss === Swal.DismissReason.cancel) {
        // Aquí retomas el último registro guardado
        // Suponemos que la API para obtener un registro con el ID es algo como 'api/records/:id'
        $fetch(`api/records/${lastRecordId}`).then((response) => {
          recordObject.value = response;
          isAmbulance.value = true;
        });
      }
    });
  } else {

    create(2); // Cambia el valor según lo que necesites
    isAmbulance.value = true;
  }
});
</script>

<style></style>
