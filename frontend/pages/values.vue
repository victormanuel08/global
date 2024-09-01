<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Valores</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="values.length === 0">No hay Valores</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Tipo</th>
              <th :class="ui.th">Valor</th>
              <th :class="ui.th">Año</th>
              <th :class="ui.th">Acciones</th>

            </tr>
          </thead>
          <tbody>

            <tr v-for="(value, index) in values" :key="index">

              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectChoice :choiceType="'VALUES_CHOICES'" v-model="value.type_values" @change="saveItem(index,'type_values',value.type_values.id)" class="border rounded p-1 w-36" />
                </div>
              </td>    
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="value.amount" @blur="saveItem(index, 'code', value.amount)"
                    class="border rounded p-1 w-36" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput type="date" v-model="value.year_date" @blur="saveItem(index, 'year_date', value.year_date)"
                    class="border rounded p-1 w-36" />
                </div>
              </td>    
    
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteValue(value.id)" :class="ui.span" >🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectChoice :choiceType="'VALUES_CHOICES'" v-model="newValuesType" class="border rounded p-1 w-36" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newValuesValue" placeholder="Valor" class="border rounded p-1 w-36 " />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput type="date" v-model="newValuesYear" placeholder="Nombre" class="border rounded p-1 w-36"  @change="toggleValues"/>
                </div>
              </td>

            
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createValue" :class="ui.span">
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
const newValuesType = ref({}) 
const newValuesValue = ref('')
const newValuesYear = ref('')
//const search = ref('')

const {
  data: values,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/values/");

const toggleValues = (value: string) => {
  newValuesYear.value = formatDateYYYY0101(value)  
}
const fetchValues = async () => {
  const {
    data: values,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/values/");

  console.log('fetchValues', values.value)

}

const deleteValue = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este Valor?')
  if (message) {
    const response = await $fetch(`api/values/${id}/`, {
      method: 'DELETE'
    })
    fetchValues()
  }
}



const saveItem = async (index: number, field: string, value: string) => {
  const val = values.value[index];
  val[field] = value;
  const response = await $fetch(`api/values/${val.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchValues();
};

const createValue = async () => {
  const consult = await $fetch('api/values/', {
    query: {
      search: newValuesType.value.id,
      year_date: newValuesYear.value
    }
  })

  if (consult.results.length > 0) {
    alert('Ya existe un valor con este tipo y año')
    newValuesType.value = ''
    newValuesValue.value = ''
    newValuesYear.value = ''
    return
  }


  const message = confirm('¿Estás seguro de crear este Valor?')

  if (!message) {
    newValuesType.value = ''
    newValuesValue.value = ''
    newValuesYear.value = ''
    fetchValues()
    return
  }

  const response = await $fetch('api/values/', {
    method: 'POST',
    body: {
      type_values: newValuesType.value.id,
      amount: newValuesValue.value,
      year_date: newValuesYear.value
    }
  })
  fetchValues()
  newValuesType.value = ''
  newValuesValue.value = ''
  newValuesYear.value = ''
}

onMounted(() => {
  fetchValues()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
