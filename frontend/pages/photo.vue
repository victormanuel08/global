<template>
  

      <h4>Fotografía</h4>


      <div v-show="!taked">
        <video autoplay ref="videoEl" :width="width" :height="height" @click="takePhoto()"> </video>
      </div>
      <div v-show="taked">
        <img ref="imgEl" :width="width" :height="height" @click="taked = false">
      </div>


      <button class="btn btn-primary" @click="okHandler">Ok</button>


</template>


<script setup lang="ts">


const videoEl = ref<HTMLVideoElement>();
const imgEl = ref<HTMLImageElement>();
const height = 300;
const width = 300;
const photob64 = ref("");
let stream: MediaStream;

const taked = ref(false);

const props = defineProps<{ show: boolean }>();
const emit = defineEmits<{
  (e: "update:show", v: boolean): void;
  (e: "update:photo", v: string): void;
}>();

const stopCamera = () => {
  if (stream) stream.getTracks()[0].stop();
};

const takePhoto = () => {
  const ratio = 1;
  const canvas = document.createElement("canvas");
  const context = canvas.getContext("2d") as CanvasRenderingContext2D;
  canvas.width = width / ratio;
  canvas.height = height / ratio;
  context.drawImage(
    videoEl.value as HTMLVideoElement,
    0,
    0,
    canvas.width,
    canvas.height
  );
  context.scale(1 / ratio, 1 / ratio);
  const data = canvas.toDataURL("image/png");
  console.log(data);
  (imgEl.value as HTMLImageElement).setAttribute("src", data);
  taked.value = true;
  photob64.value = data;
};

onUnmounted(stopCamera);

watch(
  () => props.show,
  async () => {
    if (props.show) {
      stream = await navigator.mediaDevices.getUserMedia({
        audio: false,
        video: { width: 300, height: 300 },
      });
      if (videoEl.value) videoEl.value.srcObject = stream;
    } else {
      stopCamera();
      photob64.value = "";
      taked.value = false;
    }
  }
);

const okHandler = () => {
  if (!photob64.value) takePhoto();
  emit("update:photo", photob64.value);
  emit("update:show", false);
};
</script>

<style scoped>

</style>