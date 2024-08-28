<template>

    <div class="max-w-5xl mx-auto">
        <UCard class="my-2">
            <template #header>
                <div class="flex justify-between items-center">
                    <h2 class="font-bold">Tarifas {{ props.calendarEvent?.description }} - {{
                        props.calendarEvent?.third_entity_full?.name }}</h2>
                    <div class="flex gap-3 my-3">

                        <UInput v-model="search" placeholder="Buscar" />
                        <UPagination v-model="pagination.page" :page-count="pagination.pageSize"
                            :total="pagination.resultsCount" />
                    </div>
                </div>
            </template>
            <div class="flex justify-center items-center">
                <h3 v-if="fees.length === 0">No hay Tarifas para el Contrato </h3>
            </div>
            <div style="overflow: auto;">
                <table class="table-auto w-full permission-table">
                    <thead>
                        <tr>
                            <th :class="ui.th">Especialidad</th>
                            <th :class="ui.th">Servicio</th>
                            <th :class="ui.th">Valor</th>
                            <th :class="ui.th">Acciones</th>

                        </tr>
                    </thead>
                    <tbody>

                        <tr v-for="(fee, index) in fees" :key="index">
                            <td :class="ui.td">
                                <div class="grid grid-flow-row justify-left">
                                    <span>{{ fee.specialities }}</span>
                                </div>
                            </td>

                            <td :class="ui.td">
                                <div class="grid grid-flow-row justify-left">
                                    <span>{{ fee.service }}</span>
                                </div>
                            </td>


                            <td :class="ui.td">
                                <div class="grid grid-flow-row justify-center">
                                    {{ fee.amount }}

                                </div>
                            </td>



                            <td :class="ui.td">
                                <div class="flex items-center justify-center">

                                    <span @click="deleteFees(fee.id)" :class="ui.span">🗑️</span>
                                </div>
                            </td>
                        </tr>

                        <tr>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-left">
                                    <span>
                                        <SelectSpecialities v-model="newFeeSpeciality" class="border rounded p-1" />
                                    </span>
                                </div>
                            </td>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-left">
                                    <span>
                                        <SelectServices v-model="newFeeService" :specialities="newFeeSpeciality"
                                            class="border rounded p-1" />
                                    </span>
                                </div>
                            </td>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-left">
                                    <UInput v-model="newFeeAmount" placeholder="$ Total" class="border rounded p-1" />
                                </div>
                            </td>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-center">
                                    <span @click="createFee" :class="ui.span">
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

<script lang="ts" setup>
const props = defineProps({
    calendarEvent: Object,
})

const newFeeSpeciality = ref<any>({})
const newFeeService = ref<any>({})
const newFeeAmount = ref('0')


const {
    data: fees,
    pagination,
    search,
    pending,
} = usePaginatedFetch<any>(`/api/fees/?search&policy=${props.calendarEvent?.id}`);



const fetchFees = async () => {
    const {
        data: fees,
        pagination,
        search,
        pending,
    } = usePaginatedFetch<any>("/api/fees/");
}

const deleteFees = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar esta Tarifa?')
  if (message) {
    const response = await $fetch(`api/fees/${id}/`, {
      method: 'DELETE'
    })
    fetchFees()
  }
}

onMounted(() => {
  fetchFees()
})


const createFee = async () => {
    const response = await $fetch<any>("/api/fees/", {
        method: "POST",
        body: {
            speciality: newFeeSpeciality.value.id,
            service: newFeeService.value.id,
            amount: newFeeAmount.value,
            policy: props.calendarEvent?.id,
            third_entity: props.calendarEvent?.third_entity_full.id
        }
    })

    if (response) {
        fees.value.push(response)
        newFeeSpeciality.value = {}
        newFeeService.value = {}
        newFeeAmount.value = '0'
    }
}

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}


</script>

<style></style>