<template>
    <ModalEditRecordAmbulance :calendarEvent="thirdSelected" v-if="isAmbulance" />
    <ModalEditThird :third="thirdSelected" :typeT="'P'" @update:modelValue="modalClosedHandler" v-model="isThird" />
</template>
<script lang="ts" setup>

const props = defineProps({
    calendarEvent: Object,
    third: Object,
})
const isAmbulance = ref(false)
const thirdSelected = ref<any>({})
const isThird = ref(false)
onMounted(() => {
    isThird.value = true
})
const modalClosedHandler = (value: any) => {
  if (!value) {
    // La modal se ha cerrado
    isAmbulance.value = true;
    console.log('modalClosedHandler', props);
    alert('La modal se ha cerrado');
  }
};
</script>

<style></style>