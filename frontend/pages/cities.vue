<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Ciudades</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="cities.length === 0">No hay ciudades</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Ciudad</th>
              <th :class="ui.th">Departamento</th>
              <th :class="ui.th">Region</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(citie, index) in cities" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="citie.name" @blur="saveItem(index, 'name', citie.name)" class="border rounded p-1 " />
                  <UInput v-model="citie.municipality_dane_code"
                    @blur="saveItem(index, 'municipality_dane_code', citie.municipality_dane_code)"
                    class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="citie.departament" @blur="saveItem(index, 'departament', citie.departament)"
                    class="border rounded p-1" />

                  <UInput v-model="citie.departament_dane_code"
                    @blur="saveItem(index, 'departament_dane_code', citie.departament_dane_code)"
                    class="border rounded p-1 w-10" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="citie.region" @blur="saveItem(index, 'region', citie.region)"
                    class="border rounded p-1 w-auto" />
                </div>

              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteCitie(citie.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newCitieName" placeholder="Ciudad" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newCitieDepartament" placeholder="Departamento" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newCitieRegion" placeholder="Region" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createCitie" :class="ui.span">💾</span>
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
const newCitieName = ref('')
const newCitieDepartament = ref('')
const newCitieRegion = ref('')
//const search = ref('')



const {
  data: cities,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/cities/");

const fetchCities = async () => {
  const {
    data: cities,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/cities/");

  console.log('fetchCities', cities.value)

}

const deleteCitie = async (id: number) => {
  autorized.value = await validatePermissions('cities', 'delete');
  if (!autorized.value) {
    fetchCities()
    return
  }
  const message = confirm('¿Estás seguro de eliminar esta ciudad?')
  if (message) {
    const response = await $fetch(`api/cities/${id}/`, {
      method: 'DELETE'
    })
    fetchCities()
  }
}

const autorized = ref(false)

const saveItem = async (index: number, field: string, value: string) => {
  autorized.value = await validatePermissions('cities', 'change');
  if (!autorized) {   
    fetchCities()
    return
  }

  const citie = cities.value[index];
  citie[field] = value;
  const response = await $fetch(`api/cities/${citie.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchCities();
};

const createCitie = async () => {
  autorized.value = await validatePermissions('cities', 'add');
  if (!autorized) {
    fetchCities()
    return
  }
  const message = confirm('¿Estás seguro de crear esta ciudad?')

  if (!message) {
    newCitieName.value = ''
    newCitieDepartament.value = ''
    newCitieRegion.value = ''
    fetchCities()
    return
  }

  const response = await $fetch('api/cities/', {
    method: 'POST',
    body: {
      name: newCitieName.value,
      departament: newCitieDepartament.value,
      region: newCitieRegion.value
    }
  })
  fetchCities()
  newCitieName.value = ''
  newCitieDepartament.value = ''
  newCitieRegion.value = ''
}

onMounted(() => {
  fetchCities()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
