<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Diagnosticos</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="diagnoses.length === 0">No hay ciudades</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Diagnostico</th>
              <th :class="ui.th">Descripcion</th>
              <th :class="ui.th">Extra</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(diagnose, index) in diagnoses" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="diagnose.code" @blur="saveItem(index, 'code', diagnose.code)"
                    class="border rounded p-1 w-14" />
                  <UInput v-model="diagnose.name" @blur="saveItem(index, 'name', diagnose.name)"
                    class="border rounded p-1 " />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="diagnose.description" @blur="saveItem(index, 'description', diagnose.description)"
                    class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="diagnose.extra" @blur="saveItem(index, 'extra', diagnose.extra)"
                    class="border rounded p-1 w-auto" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteDiagnose(diagnose.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newDiagnoseCode" placeholder="Codigo" class="border rounded p-1 w-14" />
                  <UInput v-model="newDiagnoseName" placeholder="Nombre" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newDiagnoseDescription" placeholder="Descripcion" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newDiagnoseExtra" placeholder="Extra" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createDiagnose" :class="ui.span">💾</span>
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
const newDiagnoseCode = ref('')
const newDiagnoseName = ref('')
const newDiagnoseDescription = ref('')
const newDiagnoseExtra = ref('')
//const search = ref('')

const {
  data: diagnoses,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/diagnoses/");

const fetchDiagnoses = async () => {

  const {
    data: diagnoses,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/diagnoses/");

}

const deleteDiagnose = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este diagnostico?')
  if (message) {
    const response = await $fetch(`api/diagnoses/${id}/`, {
      method: 'DELETE'
    })
    fetchDiagnoses()
  }
}



const saveItem = async (index: number, field: string, value: string) => {
  const diagnose = diagnoses.value[index];
  diagnose[field] = value;
  const response = await $fetch(`api/diagnoses/${diagnose.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchDiagnoses();
};

const createDiagnose = async () => {
  const message = confirm('¿Estás seguro de crear este Diagnostico?')

  if (!message) {
    newDiagnoseCode.value = ''
    newDiagnoseName.value = ''
    newDiagnoseDescription.value = ''
    newDiagnoseExtra.value = ''
    fetchDiagnoses()
    return
  }

  const response = await $fetch('api/diagnoses/', {
    method: 'POST',
    body: {
      code: newDiagnoseCode.value,
      name: newDiagnoseName.value,
      description: newDiagnoseDescription.value,
      extra: newDiagnoseExtra.value
    }
  })
  fetchDiagnoses()
  newDiagnoseCode.value = ''
  newDiagnoseName.value = ''
  newDiagnoseDescription.value = ''
  newDiagnoseExtra.value = ''
}

onMounted(() => {
  fetchDiagnoses()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
