<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Historias Clinicas</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="records.length === 0">No hay Historias Clinicas</h3>
      </div>
      <div>

      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Fecha</th>
              <th :class="ui.th">Identificacion</th>
              <th :class="ui.th">Paciente</th>
              <th :class="ui.th">Diagnostico</th>
            
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(record, index) in records" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  {{ formatDateYYYYMMDD(record.date_time) }}
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  Movil: {{ record.third_patient_full?.nit }}
                </div>
                <div class="flex items-center justify-center">
                  Clinica: {{ record.third_patient_full?.number_report }}
                </div>
              </td>

              <td :class="ui.td">
                <div class="flex items-center justify-center">

                  {{ record.third_patient_full?.name }} {{
                    record.third_patient_full?.last_name }}
                </div>
              </td>
              <td :class="ui.td">

                <div class="flex items-center justify-center">
                  {{ record.diagnosis_full?.description }}
                </div>
              </td>
    
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="showModalRecord(record.id)" :class="ui.span">📝</span>
                  <span @click="deleteRecord(record.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </UCard>
  </div>
</template>


<script setup lang="ts">

//const cities = ref([] as any[])
const newRecordPatient = ref({})
const newRecordMedic = ref({})
const newRecordDiagnose = ref({})
const newRecordDate = ref('')
const toast = useToast()
const query = ref('')
type Props = {
  third: string
}

const props = defineProps<Props>()

const querySet = {
  third_patient: props.third
}

const {
  data: records,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/records/");

const fetchRecords = async () => {


  const {
    data: records,
    pagination,
    search: querySet,
    pending,
  } = usePaginatedFetch<any>("/api/records/");
  console.log('fetchRecords', records.value)
  records.value = records.value.map((record: any) => {
    record.date_time = formatDateTime(record.date_time)
    return record
  })
}



const deleteRecord = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar esta Historia Clinica?')
  if (message) {
    const response = await $fetch(`api/records/${id}/`, {
      method: 'DELETE'
    })
    fetchRecords()
  }
}

const saveItem = async (index: number, field: string, value: string) => {
  const record = records.value[index];
  record[field] = value;
  const response = await $fetch(`api/records/${record.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchRecords();
};

const createRecord = async () => {
  const message = confirm('¿Estás seguro de crear este Registro Medico?')

  if (!message) {
    newRecordPatient.value = ''
    newRecordMedic.value = ''
    newRecordDiagnose.value = ''
    fetchRecords()
    return
  }

  const response = await $fetch('api/records/', {
    method: 'POST',
    body: {
      third_medic_id: newRecordMedic.value?.id,
      third_patient_id: newRecordPatient.value?.id,
      diagnosis_id: newRecordDiagnose.value?.id
    },
  })
  fetchRecords()
  newRecordPatient.value = ''
  newRecordMedic.value = ''
  newRecordDiagnose.value = ''
}

const showModalRecord = async (id: number) => {

}

onMounted(() => {
  fetchRecords()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}



</script>

<style scoped>
p {
  font-size: 8px;
}
</style>
