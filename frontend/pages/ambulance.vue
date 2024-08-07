<template>
    <ModalEditRecordAmbulance 
      :calendarEvent="thirdSelected" 
      v-if="isAmbulance" />
    <ModalEditThird 
      :third="thirdSelected" 
      :typeT="'P'"  
      @update:modelValue="modalClosedHandler(thirdSelected)"
      v-model="isThird" />
</template>
<script lang="ts" setup>

const props = defineProps({
    calendarEvent: Object,
    third: Object,

})

const modalClosedHandler = (thirdSelected: any) => {
    
    isThird.value = false
    thirdSelected = thirdSelected
    isAmbulance.value = true
}


const isAmbulance = ref(false)
const thirdSelected = ref<any>({})

const isThird = ref(false)



onMounted(() => {
    isThird.value = true
})

</script>

<style></style>