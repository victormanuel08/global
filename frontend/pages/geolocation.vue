<template>
  <div>
    <h1>Mi Ubicación</h1>
    <p v-if="Location">{{ Location.latitude }},{{ Location.longitude }}</p>
    <p v-else>No se pudo obtener la ubicación.</p>
    <p v-if="address">{{ address }}</p>
    <USelectMenu :options="address" v-model="modelValue" @click="clickHandler"/>

    

  </div>
</template>

<script setup lang="ts">




onMounted(() => {
  getLocation()

})

const toast = useToast()
const Location = ref({}as location)
const address = ref<any>()

type location = {
  latitude:number
  longitude:number

}

const getLocation = async () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                Location.value = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,                  
                };
            },
            (error) => {
                //console.error('Error al obtener la ubicación:', error.message);
                toast.add({title: 'Error al obtener la ubicación ', description: error.message})
            }           
        );
   
    } else {
        console.error('Geolocalización no está disponible en este navegador.');
    }

}

watch(Location, async (newLocation, oldLocation) => {
  if (newLocation.latitude && newLocation.longitude) {
   // const response = await $fetch<any>(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${newLocation.latitude}&lon=${newLocation.longitude}&zoom=18&addressdetails=1`)
   // address.value = response.display_name
    address.value = await getAddress(newLocation.latitude + ', ' + newLocation.longitude)

  }
})

</script>
