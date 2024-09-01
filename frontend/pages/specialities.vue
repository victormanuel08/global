<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Especialidades</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="specialities.length === 0">No hay Especialidades</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Codigo</th>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(speciality, index) in specialities" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span v-if="speciality.code ==='AMB' || speciality.code==='012'">{{speciality.code}}</span>
                  <UInput v-model="speciality.code" @blur="saveItem(index, 'code', speciality.code)"
                    class="border rounded p-1 w-14" v-else/>
                  
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  
                    <span v-if="speciality.code ==='AMB' || speciality.code==='012'">{{speciality.description}}</span>
                    <UInput v-model="speciality.description" @blur="saveItem(index, 'description', speciality.description)"
                    class="border rounded p-1" v-else/>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteSpeciality(speciality.id)" :class="ui.span"
                    v-if="speciality.code !== 'AMB'">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newSpecialityCode" placeholder="Codigo" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newSpecialityDescription" placeholder="Nombre" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createSpeciality" :class="ui.span">
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
const newSpecialityDescription = ref('')
const newSpecialityCode = ref('')
//const search = ref('')

const {
  data: specialities,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/specialities/");

const fetchSpecialities = async () => {
  const {
    data: specialities,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/specialities/");

  console.log('fetchSpecialities', specialities.value)

}

const deleteSpeciality = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar esta Especialidad?')
  if (message) {
    const response = await $fetch(`api/specialities/${id}/`, {
      method: 'DELETE'
    })
    fetchSpecialities()
  }
}



const saveItem = async (index: number, field: string, value: string) => {
  const speciality = specialities.value[index];
  speciality[field] = value;
  if (field === 'code') {
    if (value === 'AMB' || value === 'O12') {
      alert('No puedes cambiar el código de la especialidad ')
      fetchSpecialities()
      return
    }
  }
  if (field === 'description') {
    if (value === 'AMBULANCIA' || value === 'TERAPIA FISICA') {
      alert('No puedes cambiar el código de la especialidad ')
      fetchSpecialities()
      return
    }
  }
  const response = await $fetch(`api/specialities/${speciality.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchSpecialities();
};

const createSpeciality = async () => {
  const message = confirm('¿Estás seguro de crear esta Especialidad?')

  if (!message) {
    newSpecialityCode.value = ''
    newSpecialityDescription.value = ''
    fetchSpecialities()
    return
  }

  const response = await $fetch('api/specialities/', {
    method: 'POST',
    body: {
      code: newSpecialityCode.value,
      description: newSpecialityDescription.value,
    }
  })
  fetchSpecialities()
  newSpecialityCode.value = ''
  newSpecialityDescription.value = ''
}

onMounted(() => {
  fetchSpecialities()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
