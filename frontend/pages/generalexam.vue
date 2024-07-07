<template>
    <div class="max-w-5xl mx-auto">
      <UCard class="my-2">
        <template #header>
          <div class="flex justify-between items-center">
            <h2 class="font-bold">Examen General</h2>
            <div class="flex gap-3 my-3">
                <UInput v-model="search" placeholder="Buscar" />
                <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
            </div>
          </div>
        </template>
        <div class="flex justify-center items-center">
          <h3 v-if="generalexams.length === 0">No hay examenes generales</h3>
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
            
            <tr v-for="(generalexam, index) in generalexams" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="generalexam.code" @blur="saveItem(index,'code',generalexam.code)" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="generalexam.name" @blur="saveItem(index,'name',generalexam.name)" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteGeneralExam(generalexam.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr> 
           
            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newGeneralExamCode" placeholder="Codigo" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newGeneralExamName" placeholder="Nombre" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createGeneralExam" :class="ui.span">💾</span>
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
const newGeneralExamName = ref('')
const newGeneralExamCode = ref('')
//const search = ref('')



const {
    data: generalexams ,
    pagination,
    search ,
    pending,
} = usePaginatedFetch<any>("/api/general_exam/");

const fetchGeneralExams = async () => {
  const {
    data: generalexams ,
    pagination,
    search ,
    pending,
  } = usePaginatedFetch<any>("/api/general_exam/");  
  
  console .log('fetchGeneralExams',generalexams.value)

}

const deleteGeneralExam = async (id: number) => {
    const message = confirm('¿Estás seguro de eliminar este Examen General?')
    if (message) {
        const response = await $fetch(`api/general_exam/${id}/`, {
            method: 'DELETE'
        })
        fetchGeneralExams()
    }
}



const saveItem = async (index: number, field: string, value: string) => {
  const generalexam = generalexams.value[index];
  generalexam[field] = value;
  const response = await $fetch(`api/general_exam/${generalexam.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
    fetchGeneralExams();
};

const createGeneralExam = async () => {
    const message = confirm('¿Estás seguro de crear este Examen General?')

    if (!message){
        newGeneralExamCode.value = ''
        newGeneralExamName.value = ''
        fetchGeneralExams()
        return
    }
    
    const response = await $fetch('api/general_exam/', {
        method: 'POST',
        body: {
            code: newGeneralExamCode.value,
            name: newGeneralExamName.value,
        }
    })
    fetchGeneralExams()
    newGeneralExamCode.value = ''
    newGeneralExamName.value = ''
}

onMounted(() => {
   fetchGeneralExams()
})

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

</script>
