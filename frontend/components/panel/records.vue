<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Historia Clinica - {{ record.third_patient_full.name }} {{ record.third_patient_full.second_name }} {{ record.third_patient_full.last_name }} {{ record.third_patient_full.second_last_name }}</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="records.length === 0">No hay Historias Clinicas</h3>
      </div>
      <div>

      </div>
      <div style="overflow: auto;  width: auto ; text-align: center; min-height: 0;">
     
      <table class="table-auto w-full permission-table">
        <thead>
          <tr>
            <th :class="ui.th">Fecha</th>

            <th :class="ui.th">Medico</th>
            <th :class="ui.th">Diagnostico</th>
           
          </tr>
        </thead>
        <tbody>

          <tr v-for="(record, index) in records" :key="index">
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                {{ formatDateYYYYMMDD(record.date_time) }}
              </div>
            </td>

            <td :class="ui.td">
              <div class="flex items-center justify-center">
     
                {{ record.third_medic_full.name }} {{ record.third_medic_full.last_name }}  {{ record.third_medic_full.second_last_name }}
              </div>
            </td>
            <td :class="ui.td">

              <div class="flex items-center justify-center">

                {{ record.diagnosis_full?.description }} 
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

const props = defineProps({
  calendarEvent: Object,
})

const record = ref<any>({})

onMounted(() => {
  fetchRecord(props.calendarEvent?.id)
});

const fetchRecord = async (q: any) => {
  const response = await $fetch<any>("api/records/" + q)
  record.value = response

}
await fetchRecord(props.calendarEvent?.id);
const {
    data: records = [] as any,
    pagination,
    search,
    pending,
  } =  usePaginatedFetch<any>(`/api/records/?search&third_patient=${record.value.third_patient_full.id}`);

  records.value = records.value.map((record: any) => {
    record.date_time = formatDateTime(record.date_time)
    record
  })





const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}



</script>

<style scoped>
p {
  font-size: 8px;
}
</style>
