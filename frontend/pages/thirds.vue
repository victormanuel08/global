<template>
  <ModalEditRecordAmbulance :calendarEvent="thirdSelected" v-if="isAmbulance" />
  <div class="max-w-5xl mx-auto">
   
      <UCard class="m-3">
        <template #header>
          <div class="flex justify-between items-center">
            <h2 class="font-bold">Terceros</h2>
            <div class="flex gap-3 my-3">
              <UInput v-model="search" placeholder="Buscar" />
              <UPagination v-model="pagination.page" :page-count="pagination.pageSize"
                :total="pagination.resultsCount" />
            </div>
          </div>
        </template>
        <div class="flex justify-center items-center">
          <h3 v-if="thirds.length === 0">No hay Tecreros</h3>
        </div>
        <div>

        </div>
        <div style="overflow: auto;">
          <table class="table-auto w-full permission-table">
            <thead>
              <tr>
                <th :class="ui.th">Identificacion</th>
                <th :class="ui.th">Nombre</th>
                <th :class="ui.th">Apellidos</th>
                <th :class="ui.th">Usuario</th>
                <th :class="ui.th">Acciones</th>
              </tr>
            </thead>
            <tbody>

              <tr v-for="(third, index) in thirds" :key="index">
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    {{ third.type_document }}
                    <UInput v-model="third.nit" @blur="saveItem(index, 'nit', third.nit)"
                      class="border rounded p-1 w-32" />
                  </div>
                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <UInput v-model="third.name" @blur="saveItem(index, 'name', third.name)"
                      :class="third.type_document === 'NI' ? 'border rounded p-1 w-64' : 'border rounded p-1 w-32'" />
                    <UInput v-model="third.second_name" @blur="saveItem(index, 'second_name', third.second_name)"
                      class="border rounded p-1 w-32" v-if="third.type_document !== 'NI'" />
                  </div>
                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <UInput v-model="third.last_name" @blur="saveItem(index, 'last_name', third.last_name)"
                      class="border rounded p-1 w-32" v-if="third.type_document !== 'NI'" />
                    <UInput v-model="third.second_last_name"
                      @blur="saveItem(index, 'second_last_name', third.second_last_name)"
                      class="border rounded p-1 w-32" v-if="third.type_document !== 'NI'" />
                  </div>
                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <SelectUsers class="border rounded p-1 w-32" v-model="third.user_full"
                      @change="saveItem(index, 'user', third.user_full.id)">
                    </SelectUsers>
                  </div>

                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                 
                    <span @click="showModalThird(third)" :class="ui.span">🖊️</span>
                    <span @click="deleteThird(third.id)" :class="ui.span">🗑️</span>
                  </div>
                </td>
              </tr>
              <tr>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <SelectChoice :choiceType="'TYPE_DOCUMENT_CHOICES'" v-model="newThirdDocument"
                      class="border rounded p-1 w-32" />
                  </div>
                  <div class="flex items-center justify-center">
                    <UInput v-model="newThirdNit" placeholder="Identificacion" class="border rounded p-1 w-32" />
                  </div>
                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <UInput v-model="newThirdName" placeholder="Nombre" class="border rounded p-1 w-64" />
                  </div>
                  <div class="flex items-center justify-center">
                    <UInput v-model="newThirdSecondName" placeholder="Segundo Nombre" class="border rounded p-1 w-64" />
                  </div>
                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <UInput v-model="newThirdLastName" placeholder="Apellido" class="border rounded p-1 w-64" />
                  </div>
                  <div class="flex items-center justify-center">
                    <UInput v-model="newThirdSecondLastName" placeholder="Segundo Apellido"
                      class="border rounded p-1 w-64" />
                  </div>
                </td>
                <td :class="ui.td">
                  <div class="flex items-center justify-center">
                    <SelectUsers class="border rounded p-1 w-32" v-model="newThirdUser">
                    </SelectUsers>
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
        </div>
      </UCard>
   
  </div>
  <ModalEditThird :third="thirdSelected" :typeT="'P'" v-model="isThird" @update:modelValue="modalClosedHandler" />
</template>


<script setup lang="ts">
import { getUniqueDomId } from '@fullcalendar/core/internal';




const newThirdDocument = ref({})
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
const newThirdUser = ref({})
const maternity_breasfeeding_list = ref({})
const maternity_breastfeeding_complementary_list = ref({})
const maternity_breastfeeding_extend_list = ref({})
const maternity_pregnancy_list = ref({})
const maternity_violence_list = ref({})
const type_list = ref({})
const isThird = ref(false)
const isAmbulance = ref(false)
const thirdSelected = ref({})
const user_full = ref({})

const close = defineEmits(['close'])

const {
  data: thirds,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/thirds/");

const fetchThirds = async () => {
  const {
    data: thirds,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/thirds/");



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

  fetchThirds();
};

const createThird = async () => {

  const message = confirm('¿Estás seguro de crear este Tercero?')

  if (!message) {
    newThirdDocument.value = ''
    newThirdNit.value = ''
    newThirdName.value = ''
    newThirdSecondName.value = ''
    newThirdLastName.value = ''
    newThirdSecondLastName.value = ''
    newThirdType.value = ''
    newThirdSex.value = ''
    newThirdBlood.value = ''
    newThirdUser.value = ''
    fetchThirds()
    return
  }

  const response = await $fetch('api/thirds/', {
    method: 'POST',
    body: {
      type_document: newThirdDocument.value.id,
      nit: newThirdNit.value,
      name: newThirdName.value,
      second_name: newThirdSecondName.value,
      last_name: newThirdLastName.value,
      second_last_name: newThirdSecondLastName.value,
      type: newThirdType.value,
      blood_type: newThirdBlood.value,
      sex: newThirdSex.value,
      user: newThirdUser.value.id

    },
  })
  fetchThirds()
  newThirdDocument.value = ''
  newThirdNit.value = ''
  newThirdName.value = ''
  newThirdSecondName.value = ''
  newThirdLastName.value = ''
  newThirdSecondLastName.value = ''
  newThirdType.value = ''
  newThirdSex.value = ''
  newThirdBlood.value = ''
}

onMounted(() => {
  window.onload = function () {
    window.scrollTo(0, 0);
  };
  fetchThirds()
  fetchChoices()
})

const showModalThird = (value: any) => {
  thirdSelected.value = value

  isThird.value = true
}

const showModalRecordAmbulance = (value: any) => {
  thirdSelected.value = value

  isAmbulance.value = true
}

watch(() => close, () => {
  isThird.value = false
  isAmbulance.value = false

})

const modalClosedHandler = (value: any) => {
  if (!value) { // Si el valor es false, significa que la modal se ha cerrado
    alert('close')
  }
}


const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
