<template>
    <div class="max-w-5xl mx-auto">
      <UCard class="my-2">
        <template #header>
          <div class="flex justify-between items-center">
            <h2 class="font-bold">Disponibilidad Especilistas</h2>
            <div class="flex gap-3 my-3">
                <UInput v-model="search" placeholder="Buscar" />
                <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
            </div>
          </div>
        </template>
        <div class="flex justify-center items-center">
          <h3 v-if="availabilities.length === 0">No hay Disponibilidades</h3>
        </div>
        <div>
          
        </div>     
        <div style="overflow: auto;">   
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Medico</th>
              <th :class="ui.th">Fecha</th>
              <th :class="ui.th">Dia(s)-Sobrecupo / Tiempo Consulta-Cuota</th>
              <th :class="ui.th">Horario</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>            
            
            <tr v-for="(availability, index) in availabilities" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  Dr. {{ availability.third_medic_full.name }}  {{ availability.third_medic_full.last_name }}
                  <SelectThird 
                    :third-type="'M'" 
                    class="border rounded p-1 w-32"  
                    v-model="availability.third_medic_full"                   
                    @change="saveItem(index, 'third_medic', availability.third_medic_full.id)">
                  </SelectThird>  
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    type="date"
                    v-model="availability.date"
                    @blur="saveItem(index,'name',availability.date)" 
                    class="border rounded p-1 w-32" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput                   
                    v-model="availability.day"
                    readonly                     
                    class="border rounded p-1 w-20" 
                  />
                  <UCheckbox 
                    v-model="availability.overflow" 
                    class="border rounded p-1"
                  />
                  {{ availability.time }} - {{ availability.quota }}
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    type="time"
                    v-model="availability.start_time" 
                    @blur="saveItem(index,'start_time',availability.start_time)" 
                    class="border rounded p-1 w-32" 
                  />
                  <UInput
                    type="time" 
                    v-model="availability.end_time" 
                    @blur="saveItem(index,'end_time',availability.end_time)" 
                    class="border rounded p-1 w-32"
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteAvailability(availability.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>            
            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput
                    type="text"
                    disabled
                    class="border rounded p-1 w-52"  
                    v-model="newAvailabilityThirdName">
                  </UInput>
                </div>
                <div class="flex items-center justify-center">
                  <SelectThird 
                    :third-type="'M'" 
                    class="border rounded p-1 w-52"  
                    v-model="newAvailabilityThird"
                    @change="newAvailabilityThirdName = 'Doc. ' + newAvailabilityThird?.name + ' ' + newAvailabilityThird?.second_name + ' ' + newAvailabilityThird?.last_name + ' ' + newAvailabilityThird?.second_last_name"
                  >
                  </SelectThird>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    type="date"
                    v-model="newAvailabilityDate" 
                    placeholder="Nombre" 
                    class="border rounded p-1 w-32"
                  />
                </div>
                <div class="flex items-center justify-center">
                  <UInput 
                    type="date"
                    v-model="newAvailabilityEndDate" 
                    placeholder="Nombre" 
                    class="border rounded p-1 w-32"
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectDays                     
                    :class="{
                      'border rounded p-1 w-40': newAvailabilityThird.speciality_full?.code === '012',
                      'border rounded p-1 w-56': newAvailabilityThird.speciality_full?.code !== '012'
                    }"
                    v-model="newAvailabilityDay" 
                    :start="newAvailabilityDate"
                    :end = "newAvailabilityEndDate"
                  />    
                  <UInput
                    type="number" 
                    v-model="newAvailabilityOverflow" 
                    class="border rounded p-1 w-16"
                    v-if="newAvailabilityThird.speciality_full?.code === '012'"
                  />   
                </div>
                <div class="flex items-center justify-center">       
                  <UInput
                    type="number" 
                    v-model="newAvailabilityTime" 
                    class="border rounded p-1 w-28"
                  />     
                  <UInput
                    type="number" 
                    v-model="newAvailabilityQuota" 
                    class="border rounded p-1 w-28"
                    disabled
                  />    
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    type="time"
                    v-model="newAvailabilityStartTime1"                     
                    class="border rounded p-1 w-32" 
                  />
                  <UInput
                    type="time" 
                    v-model="newAvailabilityEndTime1"                     
                    class="border rounded p-1 w-32"                    
                  />
                </div>

              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createAvailability()" :class="ui.span">💾</span>
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
const toast = useToast()
const newAvailabilityThird = ref('')
const newAvailabilityThirdName = ref('')
const newAvailabilityDate = ref(getCurrentDate())
const newAvailabilityDay = ref({} as Days)
const newAvailabilityEndDate = ref(getCurrentDate())
const newAvailabilityStartTime1 = ref('08:00:00')
const newAvailabilityEndTime1 = ref('12:00:00')
const newAvailabilityQuota = ref(0)
const newAvailabilityTime = ref(30)
const newAvailabilityOverflow = ref('2')
const options = ref([])

type Days = {
    id: number
    name: string
    days: string
}

const {
    data: availabilities ,
    pagination,
    search ,
    pending,
} = usePaginatedFetch<any>("/api/availabilities/");

const fetchAvailabilities = async () => {
  const {
    data: availabilities ,
    pagination,
    search ,
    pending,
  } = usePaginatedFetch<any>("/api/availabilities/");

  console .log('fetchAvailabilities',availabilities.value)
  
}

const deleteAvailability = async (id: number) => {
    const message = confirm('¿Estás seguro de eliminar esta Disponibilidad?')
    if (message) {
        const response = await $fetch(`api/availabilities/${id}/`, {
            method: 'DELETE'
        })
        fetchAvailabilities()
    }
}

const saveItem = async (index: number, field: string, value: string) => {
  const availability = availabilities.value[index];
  availability[field] = value;
  const response = await $fetch(`api/availabilities/${availability.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  console.log('saveItem',response)
    fetchAvailabilities();
};

const createAvailability = async () => { 
  
  const message = confirm('¿Estás seguro de crear este Cronograma? ' + newAvailabilityDay.value.days);

  if (!message) {
    // Restablecer los valores
    newAvailabilityThird.value = '';
    newAvailabilityDate.value = '';
    newAvailabilityQuota.value = 0;
    newAvailabilityStartTime1.value = '';
    newAvailabilityEndTime1.value = '';
    fetchAvailabilities();
    return;
  }  

  // Insertar registros para cada fecha
  for (const date of newAvailabilityDay.value.days.split(',')) {
    toast.add({title: 'Creando Cronograma', description: 'Por favor espere...'});
    console.log('createAvailability',formatDateYYYYMMDD(date))
    const response = await $fetch('api/availabilities/', {
      method: 'POST',
      body: {        
        date: formatDateYYYYMMDD(date),
        start_time: newAvailabilityStartTime1.value,
        end_time: newAvailabilityEndTime1.value,
        quota: newAvailabilityQuota.value,
        time: newAvailabilityTime.value,
        third: newAvailabilityThird.value.id,
        overflow: newAvailabilityOverflow?.value
      },
    });
  }

  // Restablecer valores
  fetchAvailabilities();
  newAvailabilityThird.value = '';
};

onMounted(() => {
  fetchAvailabilities()
  calcQuota(newAvailabilityStartTime1.value, newAvailabilityEndTime1.value, newAvailabilityTime.value) 
})

watch (newAvailabilityDay, async (newDay, oldDay) => {
  console.log('newAvailabilityDay',newDay)
})

watch([newAvailabilityStartTime1, newAvailabilityEndTime1, newAvailabilityTime], async ([newStartTime, newEndTime, newTime], [oldStartTime, oldEndTime, oldTime]) => {
  calcQuota(newStartTime, newEndTime, newTime);
});

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

const calcQuota = (timestart: string, timeend: string, timeValue: number) => {
  console.log('calcQuota',timestart, timeend, timeValue)
  const startTimeMinutes = parseInt(timestart.split(':')[0]) * 60;
  const endTimeMinutes = parseInt(timeend.split(':')[0]) * 60;
  const durationMinutes = endTimeMinutes - startTimeMinutes;
  const quota = durationMinutes / timeValue;
  console.log('calcQuota',quota)
  newAvailabilityQuota.value = quota
  return quota
};

</script>