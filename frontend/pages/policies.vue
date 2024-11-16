<template>
  <div v-if="isFee">
    <div class="flex justify-center">
      <UButton variant="soft" @click="handleBackClick">Regresar</UButton>
    </div>

    <ModalEditFeePolicie :calendarEvent="policeObject" />
  </div>


  <div class="max-w-5xl mx-auto "v-if="!isFee">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold"><span @click="isFee = false">Contratos</span></h2>
          <div class="flex gap-3 my-3">
           
            <input ref="fileInput" type="file" accept=".txt" @change="uploadListFile" class="hidden" />
            <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
              Cargar Archivo</UButton>
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
              <!--
              <th :class="ui.th">Palntilla</th>
              -->
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
              <!--
              <td :class="ui.td">
                <div class="grid grid-flow-row justify-center">
                  <span v-if="policy.template">SI</span>
                  <span v-else>❌</span>

                </div>
              </td>
              -->
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span :class="ui.span" v-if="policy.type_police === 'SE' || policy.type_police === 'PA'"></span>
                  <span @click="feePolicies(policy)" :class="ui.span" v-else>📎</span>
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

              <!--
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <UCheckbox v-model="newPoliciesTemplate" />
                </div>
              </td>
              -->
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
const newPolicyCode = ref('')
const newPoliciesThirdEntity = ref({})
const newPoliciesDescription = ref('')

const newPoliciesDateStart = ref('')
const newPoliciesDateEnd = ref('')
const newPoliciesAmountTotal = ref('0')
const newPoliciesTypePolice = ref('')
const newPoliciesPaymentForm = ref('')
const newPoliciesTemplate = ref(false)

const policeObject = ref({})
const isFee = ref(false)

const {
  data: policies,
  pagination,
  search,
  pending,
  refresh
} = usePaginatedFetch<any>("/api/polices/");


let updatedPolicies = [];
if (policies.value) {
  updatedPolicies = await Promise.all(policies.value.map(async (policy: any) => {
    policy.type_police_full = await getCHOICE(policy.type_police, 'TYPE_POLICE_CHOICES');
    return policy;
  }));
}









const deletePolicies = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este Contrato?')
  if (message) {
    const response = await $fetch(`api/polices/${id}/`, {
      method: 'DELETE'
    })
    refresh()
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
  refresh()
};

const createPolice = async () => {
  const message = confirm('¿Estás seguro de crear este Contrato?')
  if (!message) {
    refresh()
    return
  }
  const response = await $fetch('api/polices/', {
    method: 'POST',
    body: {
      third_entity: newPoliciesThirdEntity.value.id,
      description: newPoliciesDescription.value,
      date_start: formatDateYYYYMMDD(newPoliciesDateStart.value),
      date_end: formatDateYYYYMMDD(newPoliciesDateEnd.value),
      amount_total: newPoliciesAmountTotal.value,
      type_police: newPoliciesTypePolice.value.id,
      payment_model: newPoliciesPaymentForm.value.id,
      template: newPoliciesTemplate.value

    }
  })
  refresh()
  newPolicyCode.value = ''
  newPoliciesThirdEntity.value = {}
  newPoliciesDescription.value = ''
  newPoliciesDateStart.value = ''
  newPoliciesDateEnd.value = ''
  newPoliciesAmountTotal.value = '0'
  newPoliciesTypePolice.value = ''
  newPoliciesPaymentForm.value = ''
  newPoliciesTemplate.value = false
}

const handleBackClick = () => {
  isFee.value = false;
};

onMounted(() => {
  refresh()
})

const feePolicies = (policy: any) => {
  isFee.value = false
  policeObject.value = policy
  isFee.value = true
  console.log('feePolicies', policy)
}

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}



const fileInput = ref<HTMLInputElement | null>(null)
const toast = useToast()
const triggerFileInput = () => {
  fileInput.value?.click()
}

const uploadListFile = async (event: any) => {
  const fileInput = event.target;
  if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
    toast.add({ title: "No se ha seleccionado ningún archivo." });
    console.error("No se ha seleccionado ningún archivo.");
    return;
  }

  const file = fileInput.files[0];
  toast.add({ title: "Archivo seleccionado: " + file.name });
  console.log("Archivo seleccionado:", file);

  const formData = new FormData();
  formData.append('file', file);

  if (!confirm("¿Estás seguro de cargar la lista de Contratos? Esto No sobrescribirá Ni borrará los Contratos actuales. Toda la lista sera creada incluso si ya hay un contrato similar.")) {
    return;
  }


  const reader = new FileReader();
  reader.onload = async (e) => {
    const text = e.target?.result as string;
    const lines = text.split('\n');
    for (const line of lines) {
      console.log("line", line);
      //toast.add({ title: "line: " + line });
      // 13279115,NOMBREPOLIZA,2024-09-03,2024-09-03,EV,MP,1000000
      const [nit, description,  date_start, date_end,fp,tp,amount] = line.split(',');
      const third_entity: any[] = await $fetch(`api/thirds/?nit=${nit}`, {
        method: 'GET'
      })
      toast.add({ title: "Nit: " + nit + " Descripcion: " + description + " Fecha Inicio: " + date_start + " Fecha Fin: " + date_end + " Forma de Pago: " + fp + " Tipo de Poliza: " + tp + " Monto: " + amount });
      
      console.log("third_entity", third_entity.results[0]);
      const thirdEntityId = third_entity.results[0]?.id ?? 0;
      if (thirdEntityId === 0) {
        toast.add({ title: "No se ha encontrado la entidad con NIT: " + nit });
        continue;
      }else{
        toast.add({ title: "Entidad encontrada: " + third_entity.results[0]?.name });
        await updatePolicesList(thirdEntityId, description, date_start, date_end, fp, tp, parseFloat(amount));
      }
      
    }
    toast.add({ title: "Lista de Servicios actualizada" });
    fileInput.value = null;
  };
  reader.readAsText(file);
};



const updatePolicesList = async (thirdEntityId: number, description: string, date_start: string, date_end: string, fp: string, tp: string, amount: number) => {
    try {
        const polices: { results: any[] } = await $fetch(`api/polices/?third_entity=${thirdEntityId}&description=${description}&date_start=${date_start}&date_end=${date_end}`, {
            method: 'GET'
        })
        console.log("polices", polices);
        
        const priceEditing = {
            third_entity: thirdEntityId,
            description: description,
            date_start: date_start,
            date_end: date_end,
            amount_total: amount,
            type_police: tp,
            payment_model: fp
        }
        if (polices.results.length > 0) {
            const police = polices.results[0]           
            const response = await $fetch(`api/polices/${police.id}`, {
                method: 'PATCH',
                body: priceEditing
            })
            toast.add({ title: `Contrato ${description} actualizado` })
        }else{
           
            const response = await $fetch(`api/polices/`, {
                method: 'POST',
                body: priceEditing
            })
            if (response){
              toast.add({ title: `Contrato ${description} creado` })
            }
            
        }
    } catch (error) {
        toast.add({ title: `Error al actualizar  ${description}` })
    }
    refresh()
}



</script>
