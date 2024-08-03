<template>
  <div class="camera-modal">
    <div>
      <video ref="cameraVideo" autoplay></video>
    </div>
    <div class="grid grid-rows-2 p-4">
      <button class="round-button" @click="toggleCamera">
        <i class="fas fa-arrow-left"></i>
      </button>
      <button class="round-button" @click="takePhoto">
        <i class="fas fa-camera"></i>
      </button>
    </div>
  </div>
</template>

<script setup>

const cameraVideo = ref(null);
let currentCamera = 'user';

const initCamera = async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    cameraVideo.value.srcObject = stream;
  } catch (error) {
    console.error('Error al acceder a la cámara:', error);
  }
};

const toggleCamera = () => {
  currentCamera = currentCamera === 'user' ? 'environment' : 'user';
  initCamera();
};

const takePhoto = () => {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');
  canvas.width = cameraVideo.value.videoWidth;
  canvas.height = cameraVideo.value.videoHeight;
  context.drawImage(cameraVideo.value, 0, 0);
  const photo = canvas.toDataURL('image/png');
  console.log('Foto tomada:', photo);
};

onMounted(() => {
  initCamera();
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
}
</style>
