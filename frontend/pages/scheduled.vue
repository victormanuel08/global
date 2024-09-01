<template>
  <ModalEditRecord :calendarEvent="recordObject" v-if="isMedicalOffice" />
  <div class="max-w-5xl mx-auto">
    <UCard class="m-3">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Citas</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="scheduleds.length === 0">No hay Citas</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table mx-2">
          <thead>
            <tr>
              <th :class="ui.th">Fecha</th>
              <th :class="ui.th">Especialidad</th>
              <th :class="ui.th">Medico</th>
              <th :class="ui.th">Paciente</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(scheduled, index) in scheduleds" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span :class="ui.span">
                    <template v-if="scheduled.confirmed">✅</template>
                    <template v-else>❌</template>
                  </span>
                  {{ scheduled.date }} - {{ scheduled.time }}
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  {{ scheduled.speciality_full?.description }}
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  {{ scheduled.third_medic_full?.nit }} - {{ scheduled.third_medic_full?.name + ' ' +
                    scheduled.third_medic_full?.second_name + ' ' + scheduled.third_medic_full?.last_name + ' ' +
                    scheduled.third_medic_full?.second_last_name }}
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  {{ scheduled.third_patient_full?.nit }} - {{ scheduled.third_patient_full?.name + ' ' +
                    scheduled.third_patient_full?.second_name + ' ' + scheduled.third_patient_full?.last_name + ' ' +
                    scheduled.third_patient_full?.second_last_name }}
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="confirmScheduled(scheduled.id, scheduled.confirmed)" :class="ui.span"
                    title="Confirmar o desconfirmar" v-if="!scheduled.record">
                    <template v-if="scheduled.confirmed">❌</template>
                    <template v-else>✅</template>
                  </span>
                  <span @click="addHistory(scheduled)" :class="ui.span" title="Agregar Historia Medica">📝</span>
                  <span @click="deleteScheduled(scheduled.id)" :class="ui.span" title="Eliminar"v-if="!scheduled.record">🗑️</span>
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
import type Records from './records.vue';

const authUserStorage = useAuthUserStorage()
const recordObject = ref<any>(null)
const isMedicalOffice = ref(false)

const newScheduledSpeciality = ref({})
const newScheduledPatient = ref({})
const newScheduledMedic = ref({})
const newScheduledDate = ref(getCurrentDate())
const newScheduledTime = ref(getCurrentTime())
const newScheduledOptions = ref({})
const newScheduledOptionsHours = ref({})
const rangehours = ref([])


const toast = useToast()

const {
  data: scheduleds,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/scheduleds/");

const fetchScheduleds = async () => {
  const {
    data: scheduleds,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/scheduleds/");
  console.log('fetchRecords', scheduleds.value)
}

const deleteScheduled = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar esta Cita?')
  if (message) {
    const response = await $fetch(`api/scheduleds/${id}/`, {
      method: 'DELETE'
    })
    fetchScheduleds()
  }
}

const confirmScheduled = async (id: number, confirmed: boolean) => {
  const value = !confirmed
  const cadena = value ? 'Confirmar' : 'Desconfirmar'
  const message = confirm('¿Estás seguro de ' + cadena + ' esta Cita?')
  if (message) {
    const response = await $fetch(`api/scheduleds/${id}`, {
      method: 'PATCH',
      body: JSON.stringify({
        confirmed: value,
      }),
    })
    fetchScheduleds()
  }
}

onMounted(() => {
  fetchScheduleds()
})

watch(newScheduledOptions, async (newVal, oldVal) => {
  if (newVal) {
    rangehours.value = newVal.rangetime; // Asigna rangetime a rangehours
  } else {
    newScheduledOptionsHours.value = {}; // Vacía el arreglo si newScheduledOptions no tiene selección
  }
});

const addHistory =async (value: any) => {

 if (value.record) {
    alert('Esta Cita ya tiene Historia Medica')
    const response =await  $fetch(`api/records/${value.record}/`)
    console.log('responseQ', response)
    recordObject.value = response
    isMedicalOffice.value = true
    return
  }
  const message = confirm('¿Estás seguro de agregar Historia Medica?. Esto normalmente se hace al iniiar la consulta')

  if (message) {
    const response = await  $fetch('api/records/', {
            method: 'POST',
            body: {
                third_patient: value.third_patient,
                third_medic: value.third_medic,    
            },
        })
        if (response) {
          const responseUpdated  = await $fetch(`api/scheduleds/${value.id}/`, {
            method: 'PATCH',
            body: JSON.stringify({
              record: response.id,
              confirmed: true
            }),
          })
          if (responseUpdated) {
            fetchScheduleds()
            alert('Historia Medica Agregada, Cita Confirmada')
          }
          
          
        }
  
      }
}


const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}


const createScheduled = async () => {
  const message = confirm('¿Estás seguro de crear esta Cita?');
  if (!message) {
    newScheduledDate.value = getCurrentDate();
    newScheduledTime.value = getCurrentTime();
    newScheduledSpeciality.value = '';
    newScheduledPatient.value = '';
    newScheduledMedic.value = '';
    newScheduledOptions.value = '';
    newScheduledOptionsHours.value = '';
    fetchScheduleds();
    return;
  }

  try {
    const response = await $fetch('api/scheduleds/', {
      method: 'POST',
      body: {
        date: newScheduledOptions.value.date,
        time: newScheduledOptionsHours.value.time_start,
        speciality: newScheduledSpeciality.value.id,
        third_patient: newScheduledPatient.value.id,
        third_medic: newScheduledMedic.value.id,
        confirmed: false
      },
    });
    fetchScheduleds();
    newScheduledDate.value = getCurrentDate();
    newScheduledTime.value = getCurrentTime();
    newScheduledSpeciality.value = '';
    newScheduledPatient.value = '';
    newScheduledMedic.value = '';
    newScheduledOptions.value = '';
    newScheduledOptionsHours.value = '';
  } catch (error) {
    console.error('Error al crear la cita:', error);
  }
};

</script>
