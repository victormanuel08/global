<template>
  <div>
    <div class="flex flex-row-1 gap-4 justify-center" v-if="pagerecord && !iframeError">
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
      <div v-if="pagerecord && !iframeError">
        <div v-if =" props.calendarEvent?.external_cause==='TA' " >

        </div>
        <div v-else>
          <iframe :src="pagerecord" width="100%" height="600px" />
        </div>
       
      </div>
      <div v-else>
        <p>El documento no está disponible. Por favor, inténtalo de nuevo más tarde, asegúrate de guardar las Lesiones Adecuadamente.</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>

// && props.calendarEvent?.imglc && imgtp &&" 
const props = defineProps({
  calendarEvent: Object,
});
const record = ref({} as any);
const pagerecord = ref('');
const iframeError = ref(false); // Nueva propiedad para manejar el error del iframe
import Swal from 'sweetalert2';
const toast = useToast();

// Cuando se monta el componente, obtenemos el registro
onMounted(() => {
  fetchRecord(props.calendarEvent?.id);
});

// Función para obtener el registro y la URL del PDF
const fetchRecord = async (q: any) => {
  try {
    const response = await $fetch<any>("api/records/" + q);
    
    if (!response || !response.id) {
      throw new Error('El registro no tiene un ID válido o no está disponible');
    }
    
    record.value = response;

    // Verifica si el PDF está disponible (en caso de error 500)
    const pdfResponse = await fetch('api/api/pdf/ambulancia/' + record.value.id);
    if (!pdfResponse.ok) {
      throw new Error(`Error al cargar el PDF: ${pdfResponse.statusText}`);
    }

    // Si la respuesta del PDF es correcta, actualiza la URL del iframe
    //pagerecord.value = 'api/api/pdf/ambulancia/' + record.value.id;
    pagerecord.value = 'api/api/pdf/ambulancia/' + record.value.id + '?t=' + new Date().getTime();

    iframeError.value = false; // Si todo está bien, no hay error en el iframe

  } catch (error) {
    console.error('Error al obtener el registro o el PDF:', error);
    toast.add({ title:  'Hubo un error al obtener el registro o el PDF' });
    pagerecord.value = ''; // Asegúrate de que pagerecord esté vacío en caso de error
    iframeError.value = true; // Marca que hubo un error al obtener el archivo PDF
  }
};

// Función para descargar el reporte
const downloadReport = async () => {
  try {
    const response = await fetch("api/api/printpdf/ambulancia/" + record.value.id, {
      method: 'GET',
      headers: {
        'Accept': 'application/pdf', // Asegúrate de aceptar el tipo de contenido correcto
      },
    });

    if (!response.ok) {
    
      toast.add({ title: 'Error al generar el PDF' });
 
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

    toast.add({ title: 'Error al descargar el PDF' });
  }
};

// Función para enviar el correo
const sendEmail = async () => {
  try {
    // Verifica que el registro tenga un ID válido
    if (!record.value || !record.value.id) {

      toast.add({ title: 'No se encontró un registro válido para enviar el correo.' });
      return;
    }

    // Crea el objeto FormData con los datos necesarios
    const formData = new FormData();
    formData.append('id', record.value.id); // ID del registro
    formData.append('type', 'ambulancia'); // Tipo de template (ambulancia)
    //formData.append('asunto', affair.value); // Asunto del correo
    //formData.append('mensaje', messaje.value); // Mensaje personalizado
    formData.append('destinatario', 'rinconvargasvictormanuel@gmail.com'); // Destinatario predeterminado o dinámico

    // Realiza la solicitud al endpoint del backend
    const response = await fetch('/api/sendemail/', {
      method: 'POST',
      body: formData,
    });

    // Maneja la respuesta del servidor
    if (response.ok) {
      const data = await response.json();
      //console.log('Respuesta del servidor:', data);
      Swal.fire({
        title: 'Correo enviado',
        text: 'El correo se envió correctamente.',
        icon: 'success',
      });
  
    } else {
      toast.add({ title: 'Error al enviar el correo' });
    }
  } catch (error) {

    toast.add({ title: 'Error al enviar el correo' });
  }
};
</script>

<style></style>
