<template>
  <ModalEditRecordAmbulance :calendarEvent="recordObject" v-if="isAmbulance" />
  <ModalEditRecord :calendarEvent="recordObject" v-if="isMedicalOffice" />
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold"><span @click="isAmbulance = false, isMedicalOffice = false">Historias Clinicas</span>
          </h2>
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
              <th :class="ui.th">Paciente / Diagnostico</th>

              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(record, index) in records" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span v-if="record.number_report || record.third_medic_full?.speciality_full?.code == 'AMB'"
                    title="Ambulancia"> 🚑 </span><span v-else title="Consultorio Medico"> 🏥 </span><span>{{
                      (record.date_time_format) }}</span>
                </div>

              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-start">
                  Movil: {{ record.third_patient_full?.type_document }}. {{ record.third_patient_full?.nit }}
                </div>
                <div class="flex items-center justify-start" v-if="record.number_report">
                  Clinica: {{ record.number_report_id }}. {{ record.number_report }}
                </div>
              </td>

              <td :class="ui.td">
                <div class="flex items-center justify-center">

                  {{ record.third_patient_full?.name }} {{
                    record.third_patient_full?.last_name }}
                </div>
                <div class="flex items-center justify-center">
                  {{ record.diagnosis_full?.description }}
                </div>
              </td>


              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="showModalRecord(record)" :class="ui.span">📝</span>
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
const recordObject = ref<any>(null)
const isAmbulance = ref(false)
const isMedicalOffice = ref(false)
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

interface Record {
  number_report?: string;
  [key: string]: any;
}

const showModalRecord = async (val: Record) => {
 
  isAmbulance.value = false
  isMedicalOffice.value = false
  if (val.number_report || val.third_medic_full?.speciality_full?.code == 'AMB') {
    const message = confirm('¿Estás seguro de editar este Registro Medico de Ambulancia?')
    if (message) {
      recordObject.value = val
      isAmbulance.value = true
    }
  } else {

    const message = confirm('¿Estás seguro de editar este Registro Medico de Consultorio?')
    if (message) {
      recordObject.value = val
      isMedicalOffice.value = true
    }
  }

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
