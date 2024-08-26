<template>
  <div>
   
    <div class="flex flex-row-1 gap-4 justify-center">

      <div >
        <UButton 
          style="width: 80px; 
          white-space: normal; 
          text-align: right;" 
          class="rounded-full" 
          variant="soft" 
          :onclick="downloadReport">
            Descargar
        </UButton>  
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div>
        <iframe :src= "pagerecord" width="100%" height="600px"></iframe>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  calendarEvent: Object,
})
const record = ref({} as any)
const pagerecord = ref('')
onMounted(() => {
  fetchRecord(props.calendarEvent?.id)
});

const fetchRecord = async (q: any) => {
  const response = await $fetch<any>("api/records/" + q)
  record.value = response
  pagerecord.value = 'api/api/pdf/ambulancia/' + record.value.id
}


const downloadReport = async () => {
  try {
    const response = await fetch("api/api/printpdf/ambulancia/" + record.value.id , {
      method: 'GET',
      headers: {
        'Accept': 'application/pdf', // Asegúrate de aceptar el tipo de contenido correcto
      },
    });

    if (!response.ok) {
      console.error('Error al descargar el archivo:', response.statusText);
      return;
    }

    const blob = await response.blob();
    const filename = 'ReporteHCTE' + record.value.id + '.pdf'; // Puedes ajustar el nombre del archivo según tus necesidades

    // Crear un enlace para descargar el archivo
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = filename;
    link.click();

    // Revocar la URL del objeto después de un tiempo
    setTimeout(() => {
      window.URL.revokeObjectURL(link.href);
    }, 250);
  } catch (error) {
    console.error('Error en la descarga:', error);
  }
};


</script>

<style></style>
