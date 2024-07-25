<template>
  <div>
    <h1>Procedimientos</h1>
    <div class="grid grid-cols-4 gap-4 sm:grid-cols-4">
      <div v-for="(procedure, index) in procedures" :key="index">
        <UCheckbox
          v-model="newProcedures"
          class="border rounded p-1"
          :label="procedure.name"
          :value="procedure.id" 
          @change="saveProcedures()"         
        />
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div>
        <label class="block text-sm font-medium text-gray-700">Otros:</label>
        <UInput v-model="procedures_others" variant="outline" placeholder="Motivo de la Consulta" @change="saveProcedures()" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const modelValue = defineProps({
    calendarEvent: Object,
})

interface Procedure {
  id: number;
  name: string;
}

const procedures = ref([] as Procedure[]);
const newProcedures = ref([] as number[]);
const record = ref({} as any)
const procedures_others = ref('')

onMounted(() => {  
  fetchProcedures(); 
  fetchRecord(modelValue.calendarEvent?.record.id)  
});

const saveProcedures = async () => {
  const response = await $fetch<any>(`api/records/${modelValue.calendarEvent?.record.id}/`, {
    method: 'Patch',
    body: JSON.stringify({
      procedures: newProcedures?.value,
      procedures_others: procedures_others?.value
    })
  });
  console.log('Respuesta:', response);
};

const fetchProcedures = async () => {
  const response = await $fetch<any>('api/procedures/');
  procedures.value = response.results;
  newProcedures.value = modelValue.calendarEvent?.record.procedures || [];  
};

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)    
    record.value = response    
    newProcedures.value = record.value.procedures || [];
    procedures_others.value = record.value.procedures_others || '';
}

</script>

<style></style>
