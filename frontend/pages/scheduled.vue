<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
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
      <div>

      </div>
      <table class="table-auto w-full permission-table">
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
                <span  :class="ui.span">
                  <template v-if="scheduled.confirmed">✅</template>
                  <template v-else>❌</template>
                </span>
                <UInput type="date" v-model="scheduled.date" @blur="saveItem(index, 'date', scheduled.date)"
                  class="border rounded p-1 w-30" />
                <UInput type="time" v-model="scheduled.time" @blur="saveItem(index, 'time', scheduled.time)"
                  class="border rounded p-1 w-30" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectSpecialities 
                  v-model="scheduled.speciality_full" 
                  class="border rounded p-1 w-60" 
                  @change = "showAlert"/>
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectThird 
                  :third-type="'M'" 
                  class="border rounded p-1 w-28"  
                  v-model="scheduled.third_medic_full" 
                  :specialities="scheduled.speciality_full.id" 
                  @change="saveItem(index, 'third_medic', scheduled.third_medic_full.id)">
                </SelectThird>
                <span  :class="ui.span" :title="scheduled.third_medic_full?.name + ' ' + scheduled.third_medic_full?.second_name + ' ' + scheduled.third_medic_full?.last_name + ' ' + scheduled.third_medic_full?.second_last_name">ℹ️</span>
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectThird :third-type="'P'" class="border rounded p-1 w-28"  v-model="scheduled.third_patient_full">
                </SelectThird>
                <span  :class="ui.span" :title="scheduled.third_patient_full?.name + ' ' + scheduled.third_patient_full?.second_name + ' ' + scheduled.third_patient_full?.last_name + ' ' + scheduled.third_patient_full?.second_last_name">ℹ️</span>
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="confirmScheduled(scheduled.id, scheduled.confirmed)" :class="ui.span" title="Confirmar o desconfirmar">
                  <template v-if="scheduled.confirmed">❌</template>
                  <template v-else>✅</template>
                </span>
                <span @click="addHistory(scheduled.id)" :class="ui.span" title="Agregar Historia Medica">📝</span>
                <span @click="deleteScheduled(scheduled.id)" :class="ui.span" title="Eliminar">🗑️</span>
              </div>
            </td>
          </tr>
          <tr>
            <td :class="ui.td">
              <div class="flex items-center justify-center">                   
                <SelectOptionsDate
                  v-model="newScheduledOptions" 
                  class="border rounded p-1 w-40"                    
                  :third="newScheduledMedic"
                />
                <SelectOptionsHours
                  v-model="newScheduledOptionsHours" 
                  class="border rounded p-1 w-40"                    
                  :third = "newScheduledMedic"
                  :date = "newScheduledDate"
                />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectSpecialities v-model="newScheduledSpeciality" class="border rounded p-1 w-60" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectThird class="border rounded p-1 w-28" :third-type="'M'" :specialities ="newScheduledSpeciality"
                  v-model="newScheduledMedic">
                </SelectThird>
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectThird :third-type="'P'" class="border rounded p-1 w-28" v-model="newScheduledPatient">
                </SelectThird>
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="createScheduled" :class="ui.span">💾</span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </UCard>
  </div>
</template>


<script setup lang="ts">


//const cities = ref([] as any[])
const newScheduledDate = ref(getCurrentDate())
const newScheduledTime = ref(getCurrentTime())
const newScheduledSpeciality = ref({})
const newScheduledPatient = ref({})
const newScheduledMedic = ref({})
const specialities = ref({})
const newScheduledOptions = ref({})
const newScheduledOptionsHours = ref({})

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

const showAlert = () => {
  alert('Se ha cambiado la especialidad, por favor seleccione un médico par poder guardar los cambios');
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

const saveItem = async (index: number, field: string, value: string) => {
  const scheduled = scheduleds.value[index];
  scheduled[field] = value;
  try {
    const apiUrl = `api/scheduleds/${scheduled.id}`;
    const response = await $fetch(apiUrl, {
      method: 'PATCH',
      body: JSON.stringify({
        [field]: value,
        ...(field === 'third_medic' ? { speciality: scheduled.speciality_full.id } : {}),
      }), 
    });

    fetchScheduleds();
    
  } catch (error) {
    console.error('Error al actualizar el elemento:', error);
  }
  fetchScheduleds();
};


const createScheduled = async () => {
  const message = confirm('¿Estás seguro de crear esta Cita?');
  console.log('newScheduledDate', newScheduledDate.value)
  console.log('newScheduledTime', newScheduledTime.value)

  if (!message) {
    newScheduledDate.value = getCurrentDate();
    newScheduledTime.value = getCurrentTime();
    newScheduledSpeciality.value = '';
    newScheduledPatient.value = '';
    newScheduledMedic.value = '';
    fetchScheduleds();
    return;
  }

  try {
    const response = await $fetch('api/scheduleds/', {
      method: 'POST',
      body: {
        date: newScheduledDate.value,
        time: newScheduledTime.value,
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
    toast.add({ title: 'Cita creada con éxito!' })
    
  } catch (error) {
    toast.add({ title: 'Error al crear la cita' })
    console.error('Error al crear la cita:', error);
  }
};


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
  toast.add({
    id: 'update_downloaded',
    title: 'Update downloaded.',
    description: 'It will be installed on restart. Restart now?',
    icon: 'i-octicon-desktop-download-24',
    timeout: 0,
    actions: [{
      label: 'Restart',
      click: () => {

      }
    }]
  })
  fetchScheduleds()
})

watch(
  [newScheduledMedic, newScheduledDate],
  async ([newMedicVal, newDateVal], [oldMedicVal, oldDateVal]) => {

    const availabilities =
    rangehours = rangeHours(newMedicVal.id, newDateVal)
    console.log('RangeHours', rangehours)
  }
);


const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
