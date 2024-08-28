<template>
  <div>
    <h1>Mi Ubicación</h1>
    <p v-if="Location">{{ Location.latitude }},{{ Location.longitude }}</p>

    <p v-else>No se pudo obtener la ubicación.</p>
  </div>
</template>

<script setup lang="ts">
import { get } from '@vueuse/core';



onMounted(() => {
  getLocation()

})
const Location = ref({}as location)
const address = ref<any>()

type location = {
  latitude:number
  longitude:number
}

const getLocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                Location.value = {
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

}
watch(Location, (newLocation, oldLocation) => {
  if (newLocation.latitude && newLocation.longitude) {
    const ll = newLocation.latitude + ',' + newLocation.longitude;
    address.value =  getAddress(ll)    
  }
})
</script>
