<template>
    <div class="max-w-5xl mx-auto">
      <UCard class="my-2">
        <template #header>
          <div class="flex justify-between items-center">
            <h2 class="font-bold">Terceros</h2>
            <div class="flex gap-3 my-3">
                <UInput v-model="search" placeholder="Buscar" />
                <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
            </div>
          </div>
        </template>
        <div class="flex justify-center items-center">
          <h3 v-if="thirds.length === 0">No hay Tecreros</h3>
        </div>
        <div>
          
        </div>        
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Identificacion</th>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Apellidos</th>
              <th :class="ui.th">varios</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>            
            
            <tr v-for="(third, index) in thirds" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="third.nit" 
                    @blur="saveItem(index,'nit',third.nit)" 
                    class="border rounded p-1 w-20" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="third.name"
                    @blur="saveItem(index,'name',third.name)" 
                    class="border rounded p-1 w-20" 
                  />
                  <UInput v-model="third.second_name" 
                    @blur="saveItem(index,'second_name',third.second_name)" 
                    class="border rounded p-1 w-20" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="third.last_name" 
                    @blur="saveItem(index,'last_name',third.last_name)" 
                    class="border rounded p-1 w-20" 
                  />
                  <UInput 
                    v-model="third.second_last_name" 
                    @blur="saveItem(index,'second_last_name',third.second_last_name)" 
                    class="border rounded p-1 w-20"
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  
                  <Select v-model="third.sex" @change="saveItem(index, 'sex', third.sex)" class="border rounded p-1 w-24">
                    <option v-for="option in sex_list" :key="option[0]" :value="third.sex">
                      {{ option[1] }}
                    </option>
                  </Select>
                  <USelect v-model="third.type" @change="saveItem(index, 'type', third.type)" class="border rounded p-1 w-24">
                    <option v-for="option in type_list" :key="option[0]" :value="third.type">
                      {{ option[1] }}
                    </option>
                  </USelect>
                  <USelect 
                    v-model="third.blood_type" 
                    :option-attribute = [0]
                    @change="saveItem(index, 'blood_type', third.blood_type)" 
                    class="border rounded p-1 w-14"
                    :options="blood_list"
                  >
                  </USelect>
                </div>

              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="showModalThird(third.id)" :class="ui.span">🖊️</span>
                  <span @click="deleteThird(third.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr> 
           
            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdNit" placeholder="Identificacion" class="border rounded p-1 w-20" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdName" placeholder="Nombre" class="border rounded p-1 w-20"/>
                  <UInput v-model="newThirdSecondName" placeholder="Segundo Nombre" class="border rounded p-1 w-20" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdLastName" placeholder="Apellido" class="border rounded p-1 w-20" />
                  <UInput v-model="newThirdSecondLastName" placeholder="Segundo Apellido" class="border rounded p-1 w-20" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <Select v-model="newThirdSex" placeholder="Sexo" class="border rounded p-1 w-24">
                    <option v-for="option in sex_list" :key="option[0]" :value="option[0]">
                      {{ option[1] }}
                    </option>
                  </Select>
                  <Select v-model="newThirdType" placeholder="Etnia" class="border rounded p-1 w-24">
                    <option v-for="option in type_list" :key="option[0]" :value="option[0]">
                      {{ option[1] }}
                    </option>
                  </Select>
                  <Select v-model="newThirdBlood" placeholder="Rh" class="border rounded p-1 w-14">
                    <option v-for="option in blood_list" :key="option[0]" :value="option[0]">
                      {{ option[1] }}
                    </option>
                  </Select>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createThird" :class="ui.span">💾</span>
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
const newThirdNit = ref('')
const newThirdName = ref('')
const newThirdSecondName = ref('')
const newThirdLastName = ref('')
const newThirdSecondLastName = ref('')
const newThirdType = ref('')
const newThirdSex = ref('')
const newThirdBlood = ref('')
const blood_list = ref({})
const etnias_list = ref({})
const sex_list = ref({})
const maternity_breasfeeding_list = ref({})
const maternity_breastfeeding_complementary_list = ref({})
const maternity_breastfeeding_extend_list = ref({})
const maternity_pregnancy_list = ref({})
const maternity_violence_list = ref({})
const type_list = ref({})

//const search = ref('')



const {
    data: thirds ,
    pagination,
    search ,
    pending,
} = usePaginatedFetch<any>("/api/thirds/");

const fetchThirds = async () => {
  const {
    data: thirds ,
    pagination,
    search ,
    pending,
  } = usePaginatedFetch<any>("/api/thirds/");

  console .log('fetchThirds',thirds.value)
  
}

const fetchChoices = async () => {
  const response = await $fetch<any>('api/api/choices/')
  blood_list.value = response.BLOOD_CHOICES
  etnias_list.value = response.ETNIAS_CHOICES
  maternity_breasfeeding_list.value = response.MATERNITY_BREASTFEEDING_CHOICES
  maternity_breastfeeding_complementary_list.value = response.MATERNITY_BREASTFEEDING_COMPLEMENTARY_CHOICES
  maternity_breastfeeding_extend_list.value = response.MATERNITY_BREASTFEEDING_EXTEND_CHOICES
  maternity_pregnancy_list.value = response.MATERNITY_PREGNANCY_CHOICES
  maternity_violence_list.value = response.MATERNITY_VIOLENCE_CHOICES
  type_list.value = response.TYPE_CHOICES
  sex_list.value = response.SEX_CHOICES
  console.log('fetchChoices',response)
}

const deleteThird = async (id: number) => {
    const message = confirm('¿Estás seguro de eliminar este Tercero?')
    if (message) {
        const response = await $fetch(`api/thirds/${id}/`, {
            method: 'DELETE'
        })
        fetchThirds()
    }
}



const saveItem = async (index: number, field: string, value: string) => {
  const third = thirds.value[index];
  third[field] = value;
  const response = await $fetch(`api/thirds/${third.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  console.log('saveItem',response)
    fetchThirds();
};

const createThird = async () => {
    const message = confirm('¿Estás seguro de crear este Tercero?')

    if (!message){
        newThirdNit.value = ''
        newThirdName.value = ''
        newThirdSecondName.value = ''
        newThirdLastName.value = ''
        newThirdSecondLastName.value = ''
        newThirdType.value = ''
        newThirdSex.value = ''
        newThirdBlood.value = ''
        fetchThirds()
        return
    }
    
    const response = await $fetch('api/thirds/', {
        method: 'POST',
        body: {
          nit: newThirdNit.value,
          name: newThirdName.value,
          second_name: newThirdSecondName.value,
          last_name: newThirdLastName.value,
          second_last_name: newThirdSecondLastName.value,
          type: newThirdType.value,
          blood_type: newThirdBlood.value, 
          sex: newThirdSex.value

        },
    })
    fetchThirds()
    newThirdNit.value = ''
    newThirdName.value = ''
    newThirdSecondName.value = ''
    newThirdLastName.value = ''
    newThirdSecondLastName.value = ''
    newThirdType.value = ''    
    newThirdSex.value = ''
    newThirdBlood.value = ''
}

const showModalThird = async (id: number) => {
    showModalThird.value = id
}

onMounted(() => {
   fetchThirds()
   fetchChoices()
})

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

</script>
