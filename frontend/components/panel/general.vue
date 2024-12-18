<template>
  <div>
    <h1>Examenes Generales</h1>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-3">
      <div v-for="(exam, index) in exams" :key="index">
        <UCheckbox
          v-model="newExams"
          class="border rounded p-1"
          :label="exam.name"
          :value="exam.id" 
          @change="saveExams()"         
        />
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div>
        <label class="block text-sm font-medium text-gray-700">Observaciones:</label>
        <UTextarea v-model="record.general_exam" variant="outline" placeholder="Motivo de la Consulta" @change="saveExams()" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
    calendarEvent: Object,
})

interface Exams {
  id: number;
  code: string;
  name: string;
}

const exams = ref([] as Exams[]);
const newExams = ref([] as number[]);
const record = ref({} as any)

onMounted(() => {
  fetchExams(); 
  fetchRecord(props.calendarEvent?.id)  
});

const saveExams = async () => {
  const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}/`, {
    method: 'Patch',
    body: JSON.stringify({
    types_general_exam: newExams?.value,
    general_exam: record.value?.general_exam
    })
  });
  //console.log('Respuesta:', response);
};

const fetchExams = async () => {
  const response = await $fetch<any>('api/general_exam');
  exams.value = response.results;
  newExams.value = props.calendarEvent?.types_general_exam || [];
};

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)    
    record.value = response    
    newExams.value = record.value.types_systems_review || [];
}

</script>

<style></style>
