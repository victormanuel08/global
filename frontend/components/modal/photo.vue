<template>
  <UModal v-model="innerShow">
    <div class="camera-modal border rounded">
      <div>
        <video ref="cameraVideoEl" autoplay></video>
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
        <UInput type="file" accept="image/*" @change="uploadPhoto" class="round-button large-icon" />
      </div>
    </div>
  </UModal>
</template>

<script setup lang="ts">
const props = defineProps<{
  record: any,
  detail: boolean,
  typeImg: string,
}>();

const innerShow = defineModel<boolean>();
const cameraVideoEl = ref<HTMLVideoElement>();
const currentCamera = ref('environment' as 'user' | 'environment');

const uploadPhoto = (event: any) => {
  const selectedFile = event[0];
  saveImage(props.record.id, props.typeImg, selectedFile);
};

const stopStream = () => {
  if (cameraVideoEl.value && cameraVideoEl.value.srcObject) {
    const mediaStream = cameraVideoEl.value.srcObject as MediaStream;
    const tracks = mediaStream.getTracks() as MediaStreamTrack[];
    tracks.forEach((track) => track.stop());
  }
};

const initStream = async () => {
  stopStream();
  const stream = await navigator.mediaDevices.getUserMedia({
    video: { facingMode: currentCamera.value }
  });
  if (cameraVideoEl.value) cameraVideoEl.value.srcObject = stream;
};

watch(innerShow, () => {
  if (innerShow.value) {
    initStream();
  } else {
    stopStream();
  }
});

const toggleCamera = () => {
  currentCamera.value = currentCamera.value === 'user' ? 'environment' : 'user';
  initStream();
};

const takePhoto = () => {
  if (!cameraVideoEl.value) return;
  if (cameraVideoEl.value.readyState === 4) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d') as CanvasRenderingContext2D;
    canvas.width = cameraVideoEl.value.videoWidth;
    canvas.height = cameraVideoEl.value.videoHeight;
    context.drawImage(cameraVideoEl.value, 0, 0);
    canvas.toBlob((blob) => {
      if (blob) {
        saveImage(props.record.id, props.typeImg, blob);
      }
    }, 'image/jpeg');
  }
};

const saveImage = async (index: number, field: string, blob: Blob) => {
  try {
    console.log("blob", blob);
    const file = new File([blob], 'HC-' + field + '-' + index + '.jpeg', { type: 'image/jpeg' });
    const formData = new FormData();
    formData.append(field, file);

    const response = await $fetch(`api/records/${index}/`, {
      method: 'PATCH',
      body: formData,
      headers: {
        "Content-Type": "multipart/form-data; boundary=----"
      },
    });
    innerShow.value = false;
  } catch (error) {
    console.error('Error en la solicitud al servidor:', error);
  }
};
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
