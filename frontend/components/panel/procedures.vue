<template>
  <div>
    <h1>Procedimientos</h1>
    <div class="grid grid-cols-2 gap-4 md:grid-cols-5">
      <div v-for="(service, index) in services" :key="index">
        <UCheckbox v-model="newServices" class="border rounded p-1"
          :label="service.description"
          @change="saveServices()" 
          :value="service.id"/>
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div>
        <label class="block text-sm font-medium text-gray-700">Otros:</label>
        <UInput v-model="procedures_others" variant="outline" placeholder="Motivo de la Consulta"
          @change="saveServices()" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  calendarEvent: Object,
})

interface Services {
  id: number;
  code: string;
  description: string;
  speciality: number;
  amount_particular: number;
  amount_soat: number;

}

const services = ref([] as Services[]);
const newServices = ref([] as number[]);
const record = ref({} as any)
const procedures_others = ref('')


onMounted(() => {
  fetchServices();
  fetchRecord(props.calendarEvent?.id)
});

const saveServices = async () => {
  console.log('Guardando', newServices.value + ' ' + procedures_others.value);
  const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}/`, {
    method: 'Patch',
    body: JSON.stringify({
      service: newServices?.value,
      procedures_others: procedures_others?.value
    })
  });
  console.log('Respuesta:', response);
};

const query = ref('');

const fetchServices = async () => {
  const queryParams = {
    search: query.value,
    speciality: props.calendarEvent?.third_medic_full?.speciality_full?.id,
  }

  const response = await $fetch<any>('api/services/', {
    query: queryParams
  });
  services.value = response.results;
  newServices.value = props.calendarEvent?.procedures || [];
};


const fetchRecord = async (q: any) => {
  const response = await $fetch<any>("api/records/" + q)
  record.value = response
  newServices.value = record.value.service || [];
  procedures_others.value = record.value.procedures_others || '';
}

</script>

<style></style>
