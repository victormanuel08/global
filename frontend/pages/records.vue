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
              <th :class="ui.th">Paciente</th>
              <th :class="ui.th">Medico / Diagnostico</th>

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
                  Identificacion: {{ record.third_patient_full?.type_document }}. {{ record.third_patient_full?.nit }}
                </div>
                <div class="flex items-center justify-start" v-if="record.number_report">
                  ID Temporal: {{ record.number_report_id }}. {{ record.number_report }}

                </div>
                <div class="flex items-center justify-left">
                  Nombre:
                  {{ record.third_patient_full?.name }} {{
                    record.third_patient_full?.last_name }}
                </div>
              </td>

              <td :class="ui.td">
                <div class="flex items-center justify-left">
                
                  {{ record.third_medic_full?.name }} 
                   {{  record.third_medic_full?.last_name }}
                </div>
                <div class="flex items-center justify-left">
                  {{ record.diagnosis_full?.description }}
                </div>
              </td>


              <td :class="ui.td">
                <div class="flex items-center justify-center">
                 
                  <span @click="showModalRecord(record)" :class="ui.span"
                    v-if="canedit(record.third_medic)">📝</span>
                  <span @click="deleteRecord(record.id)" :class="ui.span" v-if="record.isadmin">🗑️</span>
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
import Swal from 'sweetalert2';
const authUserStorage = ref( useAuthUserStorage());
const isLoading = ref(true);

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
  refresh,
} = usePaginatedFetch<any>("/api/records/");

const canedit = (thirdmedic: number): boolean => {
  return authUserStorage.value?.third?.id === thirdmedic;
};

const addUser = async () => {
  records.value = records.value.map((record: any) => {
    // Asegura que el campo user_load exista
    record.user_load = record.user_load || authUserStorage.value.third.id;

    // Verifica si el usuario pertenece a un grupo llamado "Admin"
    record.isadmin = Array.isArray(authUserStorage.value.groups_full) 
      ? authUserStorage.value.groups_full.some((group: any) => group.name === 'Administrador') 
      : false;

    return record;
  });
};





async function deleteRecord(id: any) {
  const result = await Swal.fire({
    title: '¿Estás seguro?',
    text: 'Esta acción eliminará esta Historia Clínica. No podrás revertirla.',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, eliminar',
    cancelButtonText: 'Cancelar'
  });

  if (result.isConfirmed) {
    try {
      await $fetch(`api/records/${id}/`, {
        method: 'DELETE'
      });
      Swal.fire('¡Eliminado!', 'La Historia Clínica ha sido eliminada.', 'success');
      refresh();
    } catch (error) {
      Swal.fire('Error', 'Ocurrió un problema al eliminar el registro.', 'error');
    }
  }
}




interface Record {
  number_report?: string;
  [key: string]: any;
}



const showModalRecord = async (val: Record) => {
  isAmbulance.value = false;
  isMedicalOffice.value = false;

  let message = '';
  let title = '';
  let isConfirmed = false;

  if (val.number_report || val.third_medic_full?.speciality_full?.code === 'AMB') {
    title = 'Registro Médico de Ambulancia';
    message = '¿Estás seguro de editar este Registro Médico de Ambulancia?';
  } else {
    title = 'Registro Médico de Consultorio';
    message = '¿Estás seguro de editar este Registro Médico de Consultorio?';
  }

  const result = await Swal.fire({
    title,
    text: message,
    icon: 'question',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Sí, continuar',
    cancelButtonText: 'Cancelar',
  });

  if (result.isConfirmed) {
    recordObject.value = val;
    if (val.number_report || val.third_medic_full?.speciality_full?.code === 'AMB') {
      isAmbulance.value = true;
    } else {
      isMedicalOffice.value = true;
    }
  }
};

onMounted(async () => {
  while (!authUserStorage.value?.third?.id) {
    await new Promise(resolve => setTimeout(resolve, 100));
  }

  addUser();
  isLoading.value = false;

});





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
