<template>
    <UModal :img:close="close">
        <div class="signature-box border rounded">
            <div class="signature-content border rounded">
                <!--<vue-image-zoomer :regular="imgRoute"  />  :zoom="imgRoute" -->
                <img :src="imgRoute" alt="Imagen" />
            </div>
        </div>
    </UModal>
</template>

<script>
import { VueImageZoomer } from 'vue-image-zoomer';

export default {

    props: {
        imgRoute: String,
    },
    defineEmits: ['close'],
    components: {
        VueImageZoomer,
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