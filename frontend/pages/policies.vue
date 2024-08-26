<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Contratos</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="policies.length === 0">No hay Contratos</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Entidad/N°Poliza</th>

              <th :class="ui.th">Inicio/Fin</th>
              <th :class="ui.th">Valor Poliza/Afectado</th>


              <th :class="ui.th">Tipo Pago - Poliza</th>
              <th :class="ui.th">Palntilla</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(policy, index) in policies" :key="index">
              <td :class="ui.td">
                <div class="grid grid-flow-row justify-left">
                  <span>{{ policy.third_entity_full.name }}</span>
                  <span>N° {{ policy.description }}</span>
                </div>
              </td>

              <td :class="ui.td">
                <div class="grid grid-flow-row justify-left">
                  <span>Inicio: {{ policy.date_start }}</span>
                  <span>Fin: {{ policy.date_end }}</span>
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-flow-row justify-left">
                  <span v-if="policy.type_police !== 'EV'">Valor: {{ policy.amount_total }}</span>
                  <span v-if="policy.type_police === 'SE'">Afectacion:{{ policy.amount_affection }}</span>
                </div>
              </td>

              <td :class="ui.td">
                <div class="grid grid-flow-row justify-center">
                  {{ policy.payment_model }} - {{ policy.type_police }}

                </div>
              </td>

              <td :class="ui.td">
                <div class="grid grid-flow-row justify-center">
                  <span v-if="policy.template">SI</span>
                  <span v-else>❌</span>

                </div>
              </td>

              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span  :class="ui.span"
                    v-if="policy.type_police === 'SE' || policy.type_police === 'PA'"></span>
                    <span @click="feePolicies(policy.id)" :class="ui.span"
                    v-else>📎</span>
                  <span @click="deletePolicies(policy.id)" :class="ui.span" v-if="policy.code !== '012'">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="grid grid-rows justify-left">
                  <span>
                    <SelectThird v-model="newPoliciesThirdEntity" :third-type="'E'" class="border rounded p-1" />
                  </span>
                  <span>
                    <UInput v-model="newPoliciesDescription" placeholder="Descripcion" class="border rounded p-1" />
                  </span>
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-left">
                  <UInput v-model="newPoliciesDateStart" type="date" class="border rounded p-1" />
                  <UInput v-model="newPoliciesDateEnd" type="date" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-left">
                  <UInput v-model="newPoliciesAmountTotal" placeholder="$ Total" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-left">
                  <SelectChoice v-model="newPoliciesPaymentForm" :choice-type="'PAYMENT_MODEL_CHOICES'"
                    class="border rounded p-1" />
                  <SelectChoice v-model="newPoliciesTypePolice" :choice-type="'TYPE_POLICE_CHOICES'"
                    class="border rounded p-1" />
                </div>
              </td>


              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <UCheckbox v-model="newPoliciesTemplate" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <span @click="createPolice" :class="ui.span">
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
import { get } from '@vueuse/core';


//const cities = ref([] as any[])
const newPoliciesThirdEntity = ref({})
const newPoliciesDescription = ref('')

const newPoliciesDateStart = ref('')
const newPoliciesDateEnd = ref('')
const newPoliciesAmountTotal = ref('')
const newPoliciesTypePolice = ref('')
const newPoliciesPaymentForm = ref('')
const newPoliciesTemplate = ref(false)


const {
  data: policies,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/polices/");

const getChoice = async (value: string, choiceType: string) => {
  const response = await getCHOICE(value, choiceType)
  return response.id
}



const fetchPolicies = async () => {
  const {
    data: policies,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/polices/");

}



const deletePolicies = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este Contrato?')
  if (message) {
    const response = await $fetch(`api/policies/${id}/`, {
      method: 'DELETE'
    })
    fetchPolicies()
  }
}




const saveItem = async (index: number, field: string, value: string) => {

  const policy = policies.value[index];
  policy[field] = value;
  const response = await $fetch(`api/polices/${policy.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchPolicies();
};

const createPolice = async () => {
  const message = confirm('¿Estás seguro de crear este Contrato?')

  if (!message) {
    

    fetchPolicies()
    return
  }

  const response = await $fetch('api/polices/', {
    method: 'POST',
    body: {
      third_entity: newPoliciesThirdEntity.value.id,
      description: newPoliciesDescription.value,
      date_start: newPoliciesDateStart.value,
      date_end: newPoliciesDateEnd.value,
      amount_total: newPoliciesAmountTotal.value,
      type_police: newPoliciesTypePolice.value,
      payment_model: newPoliciesPaymentForm.value,
      template: newPoliciesTemplate.value

    }
  })
  fetchPolicies()
  newPolicyCode.value = ''


}

onMounted(() => {
  fetchPolicies()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
