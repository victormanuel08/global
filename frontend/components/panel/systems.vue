<template>
  <div>
    <h1>Revisión de Sistemas</h1>
    <div class="grid grid-cols-4 gap-4 sm:grid-cols-4">
      <div v-for="(system, index) in systems" :key="index">
        <UCheckbox
          v-model="newSystems"
          class="border rounded p-1"
          :label="system.name"
          :value="system.id" 
          @change="saveSystems()"         
        />
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div>
        <label class="block text-sm font-medium text-gray-700">Observaciones:</label>
        <UTextarea v-model="record.systems_review" variant="outline" placeholder="Motivo de la Consulta" @change="saveSystems()" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
    calendarEvent: Object,
})

interface System {
  id: number;
  name: string;
}

const systems = ref([] as System[]);
const newSystems = ref([] as number[]);
const record = ref({} as any)

onMounted(() => {
  fetchSystems(); 
  fetchRecord(props.calendarEvent?.id)  
});

const saveSystems = async () => {
  const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}/`, {
    method: 'Patch',
    body: JSON.stringify({
      types_systems_review: newSystems?.value,
      systems_review: record.value?.systems_review
    })
  });
  //console.log('Respuesta:', response);
};

const fetchSystems = async () => {
  const response = await $fetch<any>('api/systems_review');
  systems.value = response.results;
  newSystems.value = props.calendarEvent?.types_systems_review || [];
};

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)    
    record.value = response    
    newSystems.value = record.value.types_systems_review || [];
}

</script>

<style></style>
