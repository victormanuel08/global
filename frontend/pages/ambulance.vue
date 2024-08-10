<template>
  <ModalEditRecordAmbulance :calendarEvent="thirdObject" v-if="isAmbulance" />
  <ModalEditThird :third="thirdSelected" :typeT="'P'" @close="modalClosedHandler(thirdSelected)"
    v-model="isThird" />
</template>
<script lang="ts" setup>
import { useThirdObject } from '~/stores/thirds';
const { thirdObject } = useThirdObject();
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
const modalClosedHandler = async (thirdSelected: any) => {
   if (thirdObject.value.id > 0) {
    //thirdSelected.value  = thirdObject.value
    isThird.value = false
    isAmbulance.value = true
  }
}

</script>
<style></style>