<template>
  <div>
    <div class="flex flex-row-1 gap-4 justify-center">
      <div>
        <UButton style="width: 80px; white-space: normal; text-align: right;" class="rounded-full" variant="soft" @click="downloadReport">
          Descargar
        </UButton>
        <UButton style="width: 100px; white-space: normal; text-align: right;" class="rounded-full" variant="soft" @click="sendEmail">
          Enviar Email
        </UButton>
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div style="text-align: center;">
        <h2>Las imagenes no seran mostradas en la previsualizacion</h2>
      </div>
      <div v-if="pagerecord">
        <iframe :src="pagerecord" width="100%" height="600px"></iframe>
      </div>
      <div v-else>
        <p>El documento no está disponible. Por favor, inténtalo de nuevo más tarde, asegurate de guardar las Lesiones Adecuadamente.</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  calendarEvent: Object,
});
const record = ref({} as any);
const pagerecord = ref('');
const to = ref('');
const affair = ref('');
const messaje = ref('');

onMounted(() => {
  fetchRecord(props.calendarEvent?.id);
});

const fetchRecord = async (q: any) => {
  try {
    const response = await $fetch<any>("api/records/" + q);
    record.value = response;
    pagerecord.value = 'api/api/pdf/ambulancia/' + record.value.id;
  } catch (error) {
    console.error('Error al obtener el registro:', error);
    pagerecord.value = ''; // Asegúrate de que pagerecord esté vacío en caso de error
  }
};

const downloadReport = async () => {
  try {
    const response = await fetch("api/api/printpdf/ambulancia/" + record.value.id, {
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

const sendEmail = async () => {
  try {
    const formData = new FormData();
    formData.append('id', record.value.id);
    formData.append('asunto', affair.value);
    formData.append('mensaje', messaje.value);
    formData.append('destinatario', 'rinconvargasvictormanuel@gmail.com');
    //formData.append('archivo',downloadReport()); // Asegúrate de proporcionar el archivo adjunto

    const response = await fetch('/api/sendemail/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      console.log('Respuesta del servidor:', data);
      alert('Correo enviado correctamente');
    } else {
      console.error('Error al enviar el correo:', response.statusText);
      alert('Error al enviar el correo:' + response.statusText);
    }
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
};
</script>

<style></style>
