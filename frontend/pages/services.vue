<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Servicios</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="services.length === 0">No hay servicios</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Codigo</th>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Especialidad</th>
              <th :class="ui.th">Soat</th>
              <th :class="ui.th">Particular</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(service, index) in services" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.code" @blur="saveItem(index, 'code', service.code)"
                    class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.description" @blur="saveItem(index, 'description', service.description)"
                    class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">

                  <SelectSpecialities v-model="service.speciality_full" class="border rounded p-1 w-64"
                    @change="saveItem(index, 'speciality', service.speciality_full.id)">
                  </SelectSpecialities>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.amount_soat" @blur="saveItem(index, 'amount_soat', service.amount_soat)"
                    class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.amount_particular"
                    @blur="saveItem(index, 'amount_particular', service.amount_particular)" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteService(service.id)" :class="ui.span" v-if="service.code !== '012'">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceCode" placeholder="Codigo" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceDescription" placeholder="Nombre" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectSpecialities v-model="newServiceSpeciality" class="border rounded p-1 w-64">
                  </SelectSpecialities>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceAmountSoat" placeholder="$ Soat" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceAmountParticular" placeholder="$ Particular" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createService" :class="ui.span">
                    💾
                  </span>
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
const newServiceDescription = ref('')
const newServiceCode = ref('')
const newServiceSpeciality = ref({})
const newServiceAmountSoat = ref('')
const newServiceAmountParticular = ref('')
//const search = ref('')

const {
  data: services,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/services/");

const fetchServices = async () => {
  const {
    data: services,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/services/");

  console.log('fetchServcies', services.value)

}

const deleteService = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este Servicio?')
  if (message) {
    const response = await $fetch(`api/services/${id}/`, {
      method: 'DELETE'
    })
    fetchServices()
  }
}



const saveItem = async (index: number, field: string, value: string) => {
  const service = services.value[index];
  service[field] = value;
  const response = await $fetch(`api/services/${service.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchServices();
};

const createService = async () => {
  const message = confirm('¿Estás seguro de crear este Servicio?')

  if (!message) {
    newServiceCode.value = ''
    newServiceDescription.value = ''
    newServiceAmountSoat.value = ''
    newServiceAmountParticular.value = ''
    newServiceSpeciality.value = ''
    fetchServices()
    return
  }

  const response = await $fetch('api/services/', {
    method: 'POST',
    body: {
      code: newServiceCode.value,
      description: newServiceDescription.value,
      speciality: newServiceSpeciality.value.id,
      amount_soat: newServiceAmountSoat.value,
      amount_particular: newServiceAmountParticular.value
    }
  })
  fetchServices()
  newServiceCode.value = ''
  newServiceDescription.value = ''
  newServiceAmountSoat.value = ''
  newServiceAmountParticular.value = ''
  newServiceSpeciality.value = ''

}

onMounted(() => {
  fetchServices()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
