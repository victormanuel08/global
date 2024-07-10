<template>
    <div class="signature-box border rounded">
        <div class="signature-content border rounded">
            <canvas ref="signatureCanvas" :width="canvasWidth" :height="canvasHeight"></canvas>
        </div>
        <div class="buttons mb-2">
            <UButton variant="soft" @click="clearSignature">Limpiar</UButton>
            <UButton variant="soft" @click="saveSignature">Guardar</UButton>
        </div>
    </div>
</template>

<script>
import SignaturePad from 'signature_pad';

export default {
    data() {
        return {
            canvasWidth: 500, // Ancho del lienzo (en px)
            canvasHeight: 200, // Alto del lienzo (en px)
        };
    },
    mounted() {
        const canvas = this.$refs.signatureCanvas;
        const signaturePad = new SignaturePad(canvas);

        // Configura opciones adicionales si es necesario
        signaturePad.penColor = 'blue';
        // ...

        // Puedes acceder a la firma como base64
        const signatureData = signaturePad.toDataURL();
        console.log('Firma en base64:', signatureData);
    },
    methods: {
        clearSignature() {
            const signaturePad = new SignaturePad(this.$refs.signatureCanvas);
            signaturePad.clear();
        },
        saveSignature() {
            const signatureData = this.$refs.signatureCanvas.toDataURL('image/png');
            // Aquí puedes hacer algo con la firma guardada (por ejemplo, enviarla al servidor)
            console.log('Firma guardada:', signatureData);
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
    border: 2px double blue; /* Borde doble de color azul */
    border-radius: 20px; /* Esquinas redondeadas */
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
