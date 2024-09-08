<template>
    <UModal :record="record" :close="close" :detail="detail">
        <div class="signature-box border rounded">
            <div class="signature-content border rounded">
                <canvas ref="signatureCanvas" :width="canvasWidth" :height="canvasHeight"></canvas>
            </div>
            <div class="buttons mb-2">
                <UButton variant="soft" @click="clearSignature">Iniciar</UButton>
                <UButton variant="soft" @click="saveSignature">Guardar</UButton>

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
        typeThird: String,
    },
    defineEmits: ['close'],
    methods: {
        data() {
            return {
                canvasWidth: 500, 
                canvasHeight: 200, 
            };
        },
        mounted() {
            const canvas = this.$refs.signatureCanvas;
            const signaturePad = new SignaturePad(canvas);
 
            signaturePad.penColor = 'blue';
       
            const signatureData = signaturePad.toDataURL();
            console.log('Firma en base64:', signatureData);
        },
        clearSignature() {
            const signaturePad = new SignaturePad(this.$refs.signatureCanvas);
            signaturePad.clear();
        },
        saveSignature() {
            const signatureData = this.$refs.signatureCanvas.toDataURL('image/png');
            console.log('Firma guardada:', signatureData);
            console.log('Firma guardadaen modal:', this.record)
            if (this.detail) {
                console.log('PROPMODALRECORD:', this.record);
                const response = $fetch(`api/records_details/${this.record}`, {
                    method: 'PATCH',
                    body: JSON.stringify({
                        [this.typeThird]: signatureData,
                    }),
                });
            } else {
                console.log('typeThrodSigned:', this.typeThird);
                console.log('singasasasas1111111:', this.record.id);
                const response = $fetch(`api/records/${this.record.id}`, {
                    method: 'PATCH',
                    body: JSON.stringify({
                        [this.typeThird]: signatureData,
                    }),
                });
            }
            this.$emit('close', false);
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

.buttons {
    margin-top: 2rem;
    display: flex;
    gap: 1rem;
}

</style>