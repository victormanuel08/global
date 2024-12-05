<template>
  <UModal :record="record" :close="close" :detail="detail">
    <div class="signature-box border rounded">
      <div class="buttons mb-2 d-flex justify-content-center">
        <UButton variant="soft" class="btn-clear" @click="clearSignature">Limpiar</UButton>
        <UButton variant="soft" class="btn-save" @click="saveSignature">Guardar</UButton>
      </div>
      <div class="signature-content border rounded">
        <canvas ref="signatureCanvas" :width="canvasWidth" :height="canvasHeight" v-show="mode === 'signature'"></canvas>
        <div v-show="mode === 'paste'" id="pasteArea" contenteditable="true" class="paste-area border rounded mt-2" @input="updateImage"></div>
        <img ref="preview" :src="imageSrc" alt="Previsualización de la imagen" class="mt-2" v-if="imageSrc">
      </div>
      <div class="buttons mb-2 d-flex justify-content-center">
        <UButton variant="soft" @click="setMode('signature')">Firmar a Mano</UButton>
        <UButton variant="soft" @click="setMode('paste')">Pegar Imagen</UButton>
        <UButton variant="soft" @click="loadImage">Cargar Imagen</UButton>
      </div>
    </div>
  </UModal>
</template>

<script>
import SignaturePad from "signature_pad";

export default {
  props: {
    record: Object,
    detail: Boolean,
    third: Boolean,
    typeThird: String,
  },
  data() {
    return {
      canvasWidth: 500,
      canvasHeight: 200,
      imageSrc: null,
      signaturePad: null,
      mode: 'signature', // Modo por defecto
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.initializeSignaturePad();
      this.initializePasteArea();
    });
  },
  methods: {
    setMode(mode) {
      this.mode = mode;
      if (mode === 'signature') {
        this.initializeSignaturePad();
      }
    },
    initializeSignaturePad() {
      const canvas = this.$refs.signatureCanvas;
      if (canvas) {
        this.signaturePad = new SignaturePad(canvas);
        this.signaturePad.penColor = 'blue';
      } else {
        console.error('Canvas element not found');
      }
    },
    initializePasteArea() {
      const pasteArea = document.getElementById('pasteArea');
      if (pasteArea) {
        pasteArea.addEventListener('paste', this.handlePaste);
      } else {
        console.error('Paste area element not found');
      }
    },
    clearSignature() {
      if (this.signaturePad) {
        this.signaturePad.clear();
      }
      this.imageSrc = null;
    },
    async saveSignature() {
      let signatureData;
      if (this.mode === 'signature' && this.signaturePad) {
        signatureData = this.signaturePad.toDataURL('image/png');
      } else if (this.mode === 'paste' || this.mode === 'load') {
        signatureData = this.imageSrc;
      }

      if (signatureData) {
        console.log('Firma guardada:', signatureData);

        try {
          let payload, url;

          if (this.detail) {
            // Caso API: records_details
            payload = { [this.typeThird]: signatureData };
            url = `api/records_details/${this.record}`;
          } else if (this.third) {
            // Caso API: thirds
            payload = { signed: signatureData };
            url = `api/thirds/${this.third}`;
          } else {
            // Caso API: records
            payload = { [this.typeThird]: signatureData };
            url = `api/records/${this.record.id}`;
          }

          console.log('Payload:', payload);
          const response = await $fetch(url, {
            method: 'PATCH',
            body: JSON.stringify(payload),
          });
          console.log('Respuesta de la API:', response);

          this.$emit('close', false);
        } catch (error) {
          console.error('Error al guardar la firma:', error);
          alert('Hubo un error al guardar la firma. Por favor, intenta nuevamente.');
        }
      } else {
        console.error('No signature data available');
      }
    },
    loadImage() {
      const fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.accept = '.png';
      fileInput.onchange = async (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
          this.imageSrc = e.target.result;
          this.setMode('load');
        };
        reader.readAsDataURL(file);
      };
      fileInput.click();
    },
    handlePaste(event) {
      const items = event.clipboardData?.items;
      if (items) {
        for (const item of items) {
          if (item.type.startsWith('image/')) {
            const file = item.getAsFile();
            if (file) {
              const reader = new FileReader();
              reader.onload = (e) => {
                this.imageSrc = e.target.result;
                this.setMode('paste');
              };
              reader.readAsDataURL(file);
            }
          }
        }
      }
    },
    updateImage() {
      const pasteArea = document.getElementById('pasteArea');
      if (pasteArea && pasteArea.innerHTML.includes('<img')) {
        const imgTag = pasteArea.querySelector('img');
        if (imgTag) {
          this.imageSrc = imgTag.src;
        }
      }
    },
  },
};
</script>

<style scoped>
.signature-box {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  border: 2px double blue;
  border-radius: 20px;
}

.signature-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.paste-area {
  width: 100%;
  height: 100px;
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 10px;
}

.buttons {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
}

.btn-clear {
  background-color: #f8d7da;
  color: #721c24;
}

.btn-save {
  background-color: #d4edda;
  color: #155724;
}
</style>
