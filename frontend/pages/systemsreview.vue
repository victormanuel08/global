<template>
    <div class="max-w-5xl mx-auto">
      <UCard class="my-2">
        <template #header>
          <div class="flex justify-between items-center">
            <h2 class="font-bold">Sistemas de Revision</h2>
            <div class="flex gap-3 my-3">
                <UInput v-model="search" placeholder="Buscar" />
                <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
            </div>
          </div>
        </template>
        <div class="flex justify-center items-center">
          <h3 v-if="systemsreviews.length === 0">No hay Sistemas de Revision</h3>
        </div>        
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Code</th>
              <th :class="ui.th">Name</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>            
            
            <tr v-for="(systemsreview, index) in systemsreviews" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <input v-model="systemsreview.code" @blur="saveItem(index,'code',systemsreview.code)" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <input v-model="systemsreview.name" @blur="saveItem(index,'name',systemsreview.name)" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteSystemsReview(systemsreview.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr> 
           
            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <input v-model="newSystemsReviewCode" placeholder="Codigo" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <input v-model="newSystemsReviewName" placeholder="Nombre" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createSystemsReview" :class="ui.span">💾</span>
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
const newSystemsReviewName = ref('')
const newSystemsReviewCode = ref('')
//const search = ref('')



const {
    data: systemsreviews ,
    pagination,
    search ,
    pending,
} = usePaginatedFetch<any>("/api/systems_review/");

const fetchSystemsReviews = async () => {
  const {
    data: systemsreviews ,
    pagination,
    search ,
    pending,
  } = usePaginatedFetch<any>("/api/systems_review/");  
  
  console .log('fetchsystemsReview',systemsreviews.value)

}

const deleteSystemsReview = async (id: number) => {
    const message = confirm('¿Estás seguro de eliminar este Sistema de Revision?')
    if (message) {
        const response = await $fetch(`api/systems_review/${id}/`, {
            method: 'DELETE'
        })
        fetchSystemsReviews()
    }
}



const saveItem = async (index: number, field: string, value: string) => {
  const systemsreview = systemsreviews.value[index];
  systemsreview[field] = value;
  const response = await $fetch(`api/systems_review/${systemsreview.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
    fetchSystemsReviews();
};

const createSystemsReview = async () => {
    const message = confirm('¿Estás seguro de crear este Sistema de Revision?')

    if (!message){
        newSystemsReviewCode.value = ''
        newSystemsReviewName.value = ''
        fetchSystemsReviews()
        return
    }
    
    const response = await $fetch('api/systems_review/', {
        method: 'POST',
        body: {
            code: newSystemsReviewCode.value,
            name: newSystemsReviewName.value,
        }
    })
    fetchSystemsReviews()
    newSystemsReviewCode.value = ''
    newSystemsReviewName.value = ''
}

onMounted(() => {
   fetchSystemsReviews()
})

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

</script>
