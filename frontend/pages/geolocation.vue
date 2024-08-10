<template>
  <div>
    <h1>Mi Ubicación</h1>
    <p v-if="location">Latitud: {{ location.latitude }}, Longitud: {{ location.longitude }}</p>
    <p v-else>No se pudo obtener la ubicación.</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      location: null,
    };
  },
  mounted() {
    this.getLocation();
  },
  methods: {
    getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            this.location = {
              latitude: position.coords.latitude,
              longitude: position.coords.longitude,
            };
          },
          (error) => {
            console.error('Error al obtener la ubicación:', error.message);
          }
        );
      } else {
        console.error('Geolocalización no está disponible en este navegador.');
      }
    },
  },
};
</script>
