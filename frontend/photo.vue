<template>
  <UModal v-model="innerShow">
    <div class="camera-modal border rounded">
      <div class="camera-container">
        <!-- Video o imagen principal -->
        <div class="camera-video">
          <video ref="cameraVideoEl" autoplay></video>
        </div>

        <!-- Botones al lado derecho de la imagen -->
        <div class="buttons-right">
          <button class="round-button large-icon" @click="toggleCamera">
            <span class="icon">🔄</span>
          </button>
          <button class="round-button large-icon" @click="takePhoto">
            <span class="icon">📷</span>
          </button>
          <button class="round-button large-icon" @click="addDefaultThumbnail">
            <span class="icon">🌟</span>
          </button>

          <!-- Input para subir archivo de imagen -->

          <input ref="fileInput" type="file" accept="image/*" @change="uploadPhoto" class="hidden" />
          <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
            📁
          </UButton>

        </div>
      </div>

      <div class="captured-photos">
        <!-- Mostrar las miniaturas de las fotos seleccionadas -->
        <div v-for="(photo, index) in capturedPhotos" :key="index" class="photo-item"
          :class="{ selected: selectedPhotos.includes(index) }" @click="togglePhotoSelection(index)">
          <img :src="photo || defaultThumbnail" alt="Captured" />
        </div>
      </div>

      <!-- Botones de guardar y unir en la parte inferior -->
      <div class="save-merge-buttons">
        <button class="round-button large-icon save-btn" @click="confirmPhoto">
          <span class="icon">💾</span>
        </button>
        <button class="round-button large-icon merge-btn" @click="mergePhotos">
          <span class="icon">🔗</span>
        </button>
      </div>
    </div>
  </UModal>
</template>

<script setup lang="ts">
const props = defineProps({ record: Object, detail: Boolean, typeImg: String });
const innerShow = defineModel<boolean>();
const cameraVideoEl = ref<HTMLVideoElement>();
const currentCamera = ref<'user' | 'environment'>('environment');
const capturedPhotos = ref<string[]>([]); // Almacena fotos capturadas
const selectedPhotos = ref<number[]>([]); // Índices de fotos seleccionadas
const selectedPhotoToSend = ref<string | null>(null);

const fileInput = ref<HTMLInputElement | null>(null);

const triggerFileInput = () => {
  fileInput.value?.click();
}


// Miniatura por defecto en Base64
const defaultThumbnail =
  'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAAAD/2wCEAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAEsAiwDAREAAhEBAxEB/8QAFgABAQEAAAAAAAAAAAAAAAAAAAEH/8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEAMQAAAB5xh8/x//xAAYEAACAwAAAAAAAAAAAAAAAAABAwIEEv/aAAgBAQABPwD4Jpjt/8QAFxEBAAMAAAAAAAAAAAAAAAAAAAESQf/aAAgBAgEBPwCnQn//xAAZEAACAwEAAAAAAAAAAAAAAAABEQADEzH/2gAIAQMBAT8AoeZP/8QAHRAAAQQCAwAAAAAAAAAAAAAAAAERITFhcYGx8P/aAAgBAQAGPwIOO1+obz1bsKZl+V3X/8QAGhAAAwEBAQEAAAAAAAAAAAAAAAERITFBUf/aAAgBAQABPyFJIzL2dw9Uwr4cLHP/2gAMAwEAAgADAAAAEOb/AP/EABkRAAMAAwAAAAAAAAAAAAAAAAABIRExgf/aAAgBAwEBPxCGDNRiW6//xAAYEQACAwAAAAAAAAAAAAAAAAABERAgMf/aAAgBAgEBPxBg07//xAAgEAEAAgICAgMAAAAAAAAAAAABABEhMUGBEzFBgWHw/9oACAEBAAE/EFKHwcewMk44jMjtSEYDY8gEXghO+NqzIsCkTdrDEsIVDpjRXnEnq8Q7nNGbp3BIpxYMGiREuf/9k=';

const togglePhotoSelection = (index: number) => {
  if (selectedPhotos.value.includes(index)) {
    selectedPhotos.value = selectedPhotos.value.filter((i) => i !== index);
  } else if (selectedPhotos.value.length < 2) {
    selectedPhotos.value.push(index);
  }
};

const mergePhotos = () => {
  if (selectedPhotos.value.length === 2) {
    const [firstPhoto, secondPhoto] = selectedPhotos.value.map((index) => capturedPhotos.value[index]);
    const img1 = new Image();
    const img2 = new Image();
    img1.src = firstPhoto;
    img2.src = secondPhoto;
    img1.onload = () => {
      img2.onload = () => {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d') as CanvasRenderingContext2D;
        canvas.width = Math.max(img1.width, img2.width);
        canvas.height = img1.height + img2.height;
        context.drawImage(img1, 0, 0);
        context.drawImage(img2, 0, img1.height);
        const mergedPhotoUrl = canvas.toDataURL('image/jpeg');
        capturedPhotos.value.push(mergedPhotoUrl);
        selectedPhotoToSend.value = mergedPhotoUrl;

        // Deseleccionamos las fotos después de unirlas
        selectedPhotos.value = [];
      };
    };
  }
};

const confirmPhoto = () => {
  if (selectedPhotos.value.length === 1) {
    selectedPhotoToSend.value = capturedPhotos.value[selectedPhotos.value[0]];
  }

  if (selectedPhotoToSend.value && props.record && props.typeImg) {
    saveImage(props.record.id, props.typeImg, selectedPhotoToSend.value);
    selectedPhotos.value = [];
  }
};

const saveImage = async (index: number, field: string, base64: string) => {
  const formData = new FormData();
  formData.append(field, base64);
  await $fetch(`api/records/${index}/`, { method: 'PATCH', body: formData });
  innerShow.value = false;
};

const stopStream = () => {
  if (cameraVideoEl.value && cameraVideoEl.value.srcObject) {
    const mediaStream = cameraVideoEl.value.srcObject as MediaStream;
    mediaStream.getTracks().forEach((track) => track.stop());
  }
};

const initStream = async () => {
  stopStream();
  const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: currentCamera.value } });
  if (cameraVideoEl.value) cameraVideoEl.value.srcObject = stream;
};

const toggleCamera = () => {
  currentCamera.value = currentCamera.value === 'user' ? 'environment' : 'user';
  initStream();
};

const takePhoto = () => {
  if (!cameraVideoEl.value) return;
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d') as CanvasRenderingContext2D;
  canvas.width = cameraVideoEl.value.videoWidth;
  canvas.height = cameraVideoEl.value.videoHeight;
  context.drawImage(cameraVideoEl.value, 0, 0);
  capturedPhotos.value.push(canvas.toDataURL('image/jpeg'));
};

const uploadPhoto = (event: any) => {
  const selectedFile = event.target.files[0];
  const reader = new FileReader();
  reader.onload = (e: ProgressEvent<FileReader>) => {
    if (e.target?.result) capturedPhotos.value.push(e.target.result as string);
  };
  reader.readAsDataURL(selectedFile);
};

const addDefaultThumbnail = () => {
  capturedPhotos.value.push(defaultThumbnail);
  console.log("Miniatura por defecto añadida:", capturedPhotos.value);
};

watch(innerShow, () => {
  if (innerShow.value) initStream();
  else stopStream();
});
</script>

<style scoped>
/* Tus estilos aquí */
</style>


<style scoped>
.camera-modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  border: 2px solid #007bff;
  border-radius: 10px;
}

.camera-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  width: 100%;
}

.camera-video {
  width: 70%;
}

.buttons-right {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.round-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 20px;
  background: #007bff;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border: none;
}

.round-button:hover {
  background: #0056b3;
}

.icon {
  font-size: 24px;
}

.captured-photos {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
}

.photo-item {
  width: 80px;
  height: 80px;
  border: 2px solid transparent;
  cursor: pointer;
}

.photo-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.photo-item.selected {
  border-color: #007bff;
}

.save-merge-buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 10px;
}

.save-btn,
.merge-btn {
  width: 48%;
  padding: 10px;
  font-size: 16px;
  background: #28a745;
  color: white;
  border-radius: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.save-btn:hover,
.merge-btn:hover {
  background: #218838;
}
</style>
