<template>
  <ModalEditRecordAmbulance :calendarEvent="recordObject" v-if="isAmbulance" />
</template>
<script lang="ts" setup>
const authUserStorage = useAuthUserStorage()
const isAmbulance = ref(false)
const recordObject = ref<any>(null)
const create = async (value: any) => {
  const response = await  $fetch('api/records/', {
            method: 'POST',
            body: {
                third_patient: value,
                third_medic: authUserStorage?.value?.third?.id,
                vehicle: authUserStorage?.value?.third?.vehicle,
                third_driver: authUserStorage?.value?.third?.vehicle_full?.id
                
            },
        })
        console.log('response', response)
        recordObject.value = response
        console.log('recordObject', recordObject.value)
}
onMounted(() => {
  const message = confirm('¿Estás seguro de crear un Rgeistro de Ambulancia?')
  if (message) {
    create(2)
    isAmbulance.value = true
  }else{
    return
  } 
})
</script>
<style></style>