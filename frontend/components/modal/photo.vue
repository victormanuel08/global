<template>
  <UModal :record="record" :close="close" :detail="detail">
    <div class="camera-modal border rounded">
      <div>
        <video ref="cameraVideo" autoplay></video>
      </div>
      <div class="grid grid-rows-5 p-4">
        <button class="round-button large-icon" @click="toggleCamera">
          🔄
        </button>
        <div></div>
        <button class="round-button large-icon" @click="takePhoto">
          📷
        </button>
        <div></div>
        <UInput type="file" accept="image/*" @change="uploadPhoto" class="round-button large-icon"/>
      </div>
    </div>
  </UModal>
</template>

<script setup>

const emit = defineEmits(['close'])

const cameraVideo = ref(null);
let currentCamera = 'user';

const props = defineProps({
  record: Object,
  detail: Boolean,
  typeImg: String,
});



const uploadPhoto = (event) => {
  console.log('Evento de cambio:', event[0]); 
  const selectedFile = event[0];
  console.log('Archivo seleccionado:', selectedFile); 
  saveImage(props.record.id, props.typeImg, selectedFile);
};


const initCamera = async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    if (cameraVideo.value) {
      cameraVideo.value.srcObject = stream;
    } else {
      console.error('El elemento de video es nulo.');
    }
  } catch (error) {
    console.error('Error al acceder a la cámara:', error);
  }
};

const toggleCamera = () => {
  currentCamera = currentCamera === 'user' ? 'environment' : 'user';
  initCamera();
};

const takePhoto = () => {
  if (cameraVideo.value.readyState === 4) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    canvas.width = cameraVideo.value.videoWidth;
    canvas.height = cameraVideo.value.videoHeight;
    context.drawImage(cameraVideo.value, 0, 0);
    canvas.toBlob((blob) => {
      if (blob) {        
        const downloadLink = document.createElement('a');
        downloadLink.href = URL.createObjectURL(blob);
        downloadLink.download = 'mi_foto.png'; 
        document.body.appendChild(downloadLink);        
        downloadLink.click();
        document.body.removeChild(downloadLink);
        saveImage(props.record.id, props.typeImg, blob);
      }
    }, 'image/png');
  }
};


const saveImage = async (index, field, file) => {
  try {
    const response = await fetch(`api/records/${index}`, {
      method: 'PATCH',
      body: JSON.stringify({
        [field]: file,
      }),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    if (response.ok) {
      console.log('Imagen guardada correctamente.');
    } else {
      console.error('Error al guardar la imagen.');
    }
  } catch (error) {
    console.error('Error en la solicitud al servidor:', error);
  }
};

const closeCameraAndModal = () => {
  if (cameraVideo.value && cameraVideo.value.srcObject) {
    const tracks = cameraVideo.value.srcObject.getTracks();
    tracks.forEach((track) => track.stop());
  }
};

onBeforeUnmount(() => {
  console.log('onBeforeUnmount');
  closeCameraAndModal();
});
</script>

<style scoped>

.button-container {
  display: flex;
  gap: 1rem;
}

.round-button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 24px; 
  background-color: #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  margin: m-2;
  padding: 4;
}

.camera-modal {
  display: flex;
  flex-direction: column-2;
  align-items: center;
  gap: 1rem;
  border: 2px solid blue;
  padding: 1rem;
  border-radius: 20px;
}

.large-icon {
  font-size: 24px;
}
</style>