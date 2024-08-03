<template>
  <div>
    <NuxtImg
      src="~/assets/img/body.png"
      @click="handleImageClick"
      ref="myImage"
    />
    <div v-for="(point, index) in clickedPoints" :key="index">
      <!-- Representa los puntos aquí (por ejemplo, círculos) -->
      <!-- Usa las coordenadas almacenadas en point.x y point.y -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      clickedPoints: [], // Almacena las coordenadas de los clics
    };
  },
  methods: {
    handleImageClick(event) {
      const x = event.clientX;
      const y = event.clientY;
      this.clickedPoints.push({ x, y });
    },
  },
};
</script>


