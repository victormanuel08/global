<template>
    <!--<div>
        <input type="file" @change="processImage" accept="image/*" />
        <canvas ref="canvas" style="display: none"></canvas>
        <img :src="processedImage" alt="Processed Image" v-if="processedImage" />
    </div>
    -->
</template>

<script>
//import cv from "opencv.js";
//console.log('cv', cv);
//export default {
//    data() {
//        return {
//            processedImage: null,
//        };
//    },
//    methods: {
//        processImage(event) {
//            const file = event.target.files[0];
//            const reader = new FileReader();
//            reader.onload = (e) => {
//                const img = new Image();
//                img.onload = () => {
//                    this.applyFingerprintFilter(img);
//                };
//                img.src = e.target.result;
//            };
//            reader.readAsDataURL(file);
//        },
//        applyFingerprintFilter(img) {
//            const canvas = this.$refs.canvas;
//            const ctx = canvas.getContext('2d');
//            canvas.width = img.width;
//            canvas.height = img.height;
//            ctx.drawImage(img, 0, 0);
//
//            const src = cv.imread(canvas);
//            const gray = new cv.Mat();
//            const edges = new cv.Mat();
//
//            // Convertir a escala de grises
//            cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY, 0);
//
//            // Aplicar filtro de umbral
//            cv.threshold(gray, edges, 100, 255, cv.THRESH_BINARY_INV);
//
//            // Detección de bordes con Canny
//            cv.Canny(edges, edges, 50, 150);
//
//            // Mostrar la imagen procesada
//            cv.imshow(canvas, edges);
//
//            // Convertir el canvas a una imagen para mostrar en el navegador
//            this.processedImage = canvas.toDataURL();
//
//            // Limpiar matrices para evitar fugas de memoria
//            src.delete();
//            gray.delete();
//            edges.delete();
//        },
//    },
//};
</script>

<style>

</style>