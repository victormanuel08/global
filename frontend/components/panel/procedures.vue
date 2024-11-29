<template>
  <div class="grid grid-cols-1  md:grid-cols-4 m-4">
    <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Frecuencia Cardiaca:</label>
                <UInput v-model="record.ef_fc" @change="saveItem(record.id, 'ef_fc', record.ef_fc)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Frecuencia Respiratoria:</label>
                <UInput v-model="record.ef_fr" @change="saveItem(record.id, 'ef_fr', record.ef_fr)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Presion Arterial:</label>
                <UInput v-model="record.ef_pa" @change="saveItem(record.id, 'ef_pa', record.ef_pa)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Temperatura Corporal:</label>
                <UInput v-model="record.ef_temp" @change="saveItem(record.id, 'ef_temp', record.ef_temp)" />
            </div>


            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Respuesta Ocular:</label>
                <SelectChoice :choiceType="'GLASGOW_RO_CHOICES'" v-model="record.glasgow_ro_full"
                    @change="saveItem(record.id, 'glasgow_ro', record.glasgow_ro_full.id)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Respuesta Verbal:</label>
                <SelectChoice :choiceType="'GLASGOW_RV_CHOICES'" v-model="record.glasgow_rv_full"
                    @change="saveItem(record.id, 'glasgow_rv', record.glasgow_rv_full.id)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Respuest Motora:</label>
                <SelectChoice :choiceType="'GLASGOW_RM_CHOICES'" v-model="record.glasgow_rm_full"
                    @change="saveItem(record.id, 'glasgow_rm', record.glasgow_rm_full.id)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">GLASGOW TOTAL:</label>
                {{ glasgow }} / 15
            </div>
  </div>
  <div>
    <h1>Procedimientos</h1>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-5">
      <div v-for="(service, index) in services" :key="index">
        <UCheckbox v-model="newServices" class="border rounded p-1" :label="service.description"
          @change="saveServices()" :value="service.id" />
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-1 m-4">
      <div v-if ="checkedOthers || procedures_others.length > 0">
        <label class="block text-sm font-medium text-gray-700">Otros:</label>
        <UInput v-model="procedures_others" variant="outline" placeholder="Motivo de la Consulta"
          @change="saveServices()" />
      </div>
      <div hidden>
        <label class="block text-sm font-medium text-gray-700">Descripcion del Procedimiento:</label>
        <UTextarea v-model="record.descript_procedures" variant="outline" placeholder="Descripcion del Procedimiento"
          @change="saveItem(record.id, 'descript_procedures', record.descript_procedures)"></UTextarea>
      </div>
    </div>

  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  calendarEvent: Object,
})

const glasgow = ref<any>(0)
const checkedOthers = ref(false)

interface Services {
  id: number;
  code: string;
  description: string;
  speciality: number;
  amount_particular: number;
  amount_soat: number;

}

const services = ref([] as Services[]);
const newServices = ref([] as number[]);
const record = ref({} as any)
const procedures_others = ref('')


onMounted(() => {
  fetchServices();
  fetchRecord(props.calendarEvent?.id)
  retrieveFromApi(props.calendarEvent?.id);
  glasgow.value = parseInt(record.value.glasgow_ro) + parseInt(record.value.glasgow_rv) + parseInt(record.value.glasgow_rm);

});

const qq = ref()

const retrieveFromApi = async (q: any) => {

    if (typeof q === 'number') {
        qq.value = q
    } else {
        qq.value = q.id
    }


    const response = await $fetch<any>("api/records/" + qq.value)
    record.value = response

    glasgow.value = parseInt(record.value.glasgow_ro) + parseInt(record.value.glasgow_rv) + parseInt(record.value.glasgow_rm)
    record.value.priority_full = await getCHOICE(response.priority, 'PRIORITY_CHOICES')
    record.value.external_cause_full = await getCHOICE(response.external_cause, 'EXTERNAL_CAUSE_CHOICES')
    record.value.glasgow_ro_full = await getCHOICE(response.glasgow_ro, 'GLASGOW_RO_CHOICES')
    record.value.glasgow_rv_full = await getCHOICE(response.glasgow_rv, 'GLASGOW_RV_CHOICES')
    record.value.glasgow_rm_full = await getCHOICE(response.glasgow_rm, 'GLASGOW_RM_CHOICES')
    record.value.condition_full = await getCHOICE(record.value.condition, 'TYPE_ACCIDENT_CHOICES')

}

const saveServices = async () => {
  console.log('Guardando', newServices.value + ' ' + procedures_others.value);
  if (newServices.value.find((element) => element === 16)) {
    checkedOthers.value = true
  } else {
    checkedOthers.value = false
  }
  if (procedures_others.value.length > 0) {
    newServices.value = [...newServices.value, 16]
  }
  const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}/`, {
    method: 'Patch',
    body: JSON.stringify({
      service: newServices?.value,
      procedures_others: procedures_others?.value
    })
  });
 
  console.log('Respuesta:', response);
};

const saveItem = async (index: number, field: string, value: string) => {
  
  const response = await $fetch(`api/records/${index}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  if (field === 'glasgow_ro' || field === 'glasgow_rv' || field === 'glasgow_rm') {
        glasgow.value = parseInt(record.value.glasgow_ro_full?.id) + parseInt(record.value.glasgow_rv_full?.id) + parseInt(record.value.glasgow_rm_full?.id)
    }

  retrieveFromApi(index)
  //fetchRecord(props.calendarEvent?.id)
};

const query = ref('');

const fetchServices = async () => {
  const queryParams = {
    search: query.value,
    speciality: props.calendarEvent?.third_medic_full?.speciality_full?.id,
  }

  const response = await $fetch<any>('api/services/', {
    query: queryParams
  });
  services.value = response.results;
  newServices.value = props.calendarEvent?.procedures || [];
  if (newServices.value.find((element) => element === 16)) {
    checkedOthers.value = true
  } else {
    checkedOthers.value = false
  }
};


const fetchRecord = async (q: any) => {
  const response = await $fetch<any>("api/records/" + q)
  record.value = response
  newServices.value = record.value.service || [];
  procedures_others.value = record.value.procedures_others || '';
}

</script>

<style></style>
