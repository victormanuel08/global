<template>
  <UModal v-model="innerShow">
    <div class="camera-modal border rounded">
      <!-- Contenedor de la cámara y los botones -->
      <div class="camera-container">
        <!-- Video de la cámara -->
        <div class="video-container">
          <video ref="cameraVideoEl" autoplay></video>
        </div>

        <!-- Contenedor de los botones al lado del video -->
        <div class="button-container">
          <!-- Botón de cambiar cámara 
          <button class="round-button large-icon" @click="toggleCamera">
            🔄
          </button>
           Botón de tomar foto 
          <button class="round-button large-icon" @click="takePhoto">
            📷
          </button>
          -->
       
          <input type="file" accept="image/*" @change="uploadPhoto" class="hidden" ref="fileInput"/>

          <!-- Botón que activa el input de archivo -->
          <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
            <i class="fas fa-camera"></i> <!-- Icono más grande -->
          </UButton>
        </div>
      </div>
    </div>
  </UModal>
</template>

<script setup lang="ts">
const props = defineProps<{
  record: any,
  detail: boolean,
  typeImg: string,
}>()

const fileInput = ref<HTMLInputElement | null>(null)

const triggerFileInput = () => {
  fileInput.value?.click()
}

const innerShow = defineModel<boolean>()
const cameraVideoEl = ref<HTMLVideoElement>()
const listcameras = ref<any[]>([])
const selectedDeviceId = ref<string>("")

const uploadPhoto = (event: any) => {
  const selectedFile = event[0]
  saveImage(props.record.id, props.typeImg, selectedFile)
}

watch(innerShow, () => {
  if (innerShow.value) {
    initStream()
  } else {
    stopStream()
  }
})

const initStream = async () => {
  stopStream()

  const constraints: MediaStreamConstraints = {
    video: selectedDeviceId.value
      ? { deviceId: { exact: selectedDeviceId.value } }
      : true,
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints)
    if (cameraVideoEl.value) cameraVideoEl.value.srcObject = stream
  } catch (error) {
    console.error('Error al acceder al stream:', error)
    alert('No se pudo acceder a la cámara. Por favor, asegúrate de haber otorgado los permisos necesarios.')
  }
}

const toggleCamera = () => {
  initStream()
}

const stopStream = () => {
  if (cameraVideoEl.value && cameraVideoEl.value.srcObject) {
    const mediaStream = cameraVideoEl.value.srcObject as MediaStream
    const tracks = mediaStream.getTracks() as MediaStreamTrack[]
    tracks.forEach((track) => track.stop())
  }
}

const takePhoto = () => {
  if (!cameraVideoEl.value) return
  if (cameraVideoEl.value.readyState === 4) {
    const canvas = document.createElement('canvas')
    const context = canvas.getContext('2d') as CanvasRenderingContext2D
    canvas.width = cameraVideoEl.value.videoWidth
    canvas.height = cameraVideoEl.value.videoHeight
    context.drawImage(cameraVideoEl.value, 0, 0)
    canvas.toBlob((blob) => {
      if (blob) {
        saveImage(props.record.id, props.typeImg, blob)
      }
    }, 'image/jpeg')
  }
}

const saveImage = async (index: number, field: string, blob: Blob) => {
  try {
    const file = new File([blob], 'HC-' + field +'-'+ index+'.jpeg', { type: 'image/jpeg' })
    const formData = new FormData()
    formData.append(field, file)

    const response = await $fetch(`api/records/${index}/`, {
      method: 'PATCH',
      body: formData,
      headers: {
        "Content-Type": "multipart/form-data; boundary=----"
      },
    })
    innerShow.value = false
  } catch (error) {
    console.error('Error en la solicitud al servidor:', error)
  }
}

const getCameras = async () => {
  try {
    const devices = await navigator.mediaDevices.enumerateDevices()
    listcameras.value = devices.filter((device) => device.kind === 'videoinput')
    if (listcameras.value.length > 0) {
      selectedDeviceId.value = listcameras.value[0].deviceId
    }
  } catch (error) {
    console.error('Error al obtener dispositivos:', error)
  }
}

watch(innerShow, async (newValue) => {
  if (newValue) {
    await getCameras()
    initStream()
  } else {
    stopStream()
  }
})
</script>

<style scoped>
.camera-modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
}

.camera-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
  max-width: 800px; /* Ajusta el ancho máximo según sea necesario */
}

.video-container {
  flex: 1;
  max-width: 70%;
}

.button-container {
  display: flex;
  flex-direction: column;
  justify-content: center; /* Centrado vertical */
  align-items: center;    /* Centrado horizontal */
  gap: 1rem;
  flex: 1;
  max-width: 30%;
}

.round-button {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background-color: #ccc;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  font-size: 40px; /* Tamaño de ícono más grande */
}

button-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

video {
  width: 100%;
  height: auto;
  border: 1px solid #ddd;
  border-radius: 8px;
}
</style>
