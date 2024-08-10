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
      <table class="table-auto w-full permission-table">
        <thead>
          <tr>
            <th :class="ui.th">Entidad</th>

            <th :class="ui.th">Inicio/Fin</th>
            <th :class="ui.th">Valor</th>

            <th :class="ui.th">Forma Pago</th>
            <th :class="ui.th">Tipo Poliza</th>
            <th :class="ui.th">Palntilla</th>
            <th :class="ui.th">Acciones</th>
          </tr>
        </thead>
        <tbody>

          <tr v-for="(policy, index) in policies" :key="index">
            <td :class="ui.td">
              <div class="grid grid-flow-row justify-center">

                <SelectThird :third-type="'E'" v-model="policy.third_entity_full"
                  @change="saveItem(index, 'third_entity', policy.third_entity_full.id)">
                </SelectThird>
                <UInput v-model="policy.description" @blur="saveItem(index, 'description', policy.description)"
                  class="border rounded p-1" />

              </div>
            </td>

            <td :class="ui.td">
              <div class="grid grid-flow-row justify-center">
                <UInput type="date" v-model="policy.date_start" @blur="saveItem(index, 'date_start', policy.date_start)"
                  class="border rounded p-1" />
                <UInput type="date" v-model="policy.date_end" @blur="saveItem(index, 'date_end', policy.date_end)"
                  class="border rounded p-1" />

              </div>
            </td>
            <td :class="ui.td">
              <div class="grid grid-flow-row justify-center">
                <UInput v-model="policy.amount_total" @blur="saveItem(index, 'amount_total', policy.amount_total)"
                  class="border rounded p-1" />
                <UInput v-model="policy.amount_affection"
                  @blur="saveItem(index, 'amount_affection', policy.amount_affection)" class="border rounded p-1" />
              </div>
            </td>

            <td :class="ui.td">
              <div class="grid grid-flow-row justify-center">
                <SelectChoice :choiceType="'PAYMENT_MODEL_CHOICES'" v-model="policy.payment_model_full" />
                <SelectChoice :choiceType="'TYPE_POLICE_CHOICES'" v-model="policy.type_policy_full" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="grid grid-flow-row justify-center">
                <SelectChoice :choiceType="'PAYMENT_MODEL_CHOICES'" v-model="policy.payment_model_full" />
                <SelectChoice :choiceType="'TYPE_POLICE_CHOICES'" v-model="policy.type_policy_full" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="grid grid-flow-row justify-center">
                <UCheckbox v-model="policy.template" @change="saveItem(index, 'template', policy.template)" />
              </div>
            </td>

            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="deletePolicies(policy.id)" :class="ui.span" v-if="policy.code !== '012'">🗑️</span>
              </div>
            </td>
          </tr>

          <tr>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UInput v-model="newPoliciesEntity" placeholder="Entidad" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UInput v-model="newPoliciesDescription" placeholder="Descripcion" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <SelectSpecialities v-model="newPoliciesSpeciality" class="border rounded p-1 w-64">
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
                <UInput v-model="newServiceAmountParticular" placeholder="$ Particular" class="border rounded p-1" />
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
    </UCard>
  </div>
</template>


<script setup lang="ts">
import { get } from '@vueuse/core';


//const cities = ref([] as any[])
const newPoliciesEntity = ref({})
const newPoliciesDescription = ref('')
const newPoliciesDateStart = ref('')
const newPoliciesDateEnd = ref('')
const newPoliciesAmountTotal = ref('')
const newPoliciesAmountAffectation = ref('')
const newPoliciesPaymentForm = ref('')



//const search = ref('')

const {
  data: policies,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/polices/");


policies.value.map(async (policy) => ({
  ...policy,
  type_police_full: await getCHOICE(policy.type_police, 'TYPE_POLICE_CHOICES'),
  payment_model_full: await getCHOICE(policy.payment_model, 'PAYMENT_MODEL_CHOICES'),
}))



const fetchPolicies = async () => {
  const {
    data: policies,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/polices/");

  
    policies.value.map(async (policy) => ({
      ...policy,
      type_police_full: await getCHOICE(policy.type_police, 'TYPE_POLICE_CHOICES'),
      payment_model_full: await getCHOICE(policy.payment_model, 'PAYMENT_MODEL_CHOICES'),
    }))

    console.log('fetchPolicies', policies.value)

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

const createPolicy = async () => {
  const message = confirm('¿Estás seguro de crear este Contrato?')

  if (!message) {
    newPolicyCode.value = ''

    fetchPolicies()
    return
  }

  const response = await $fetch('api/polices/', {
    method: 'POST',
    body: {
      code: newPolicyCode.value,

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
