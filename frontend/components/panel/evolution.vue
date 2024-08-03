<template>
    <div class="max-w-5xl mx-auto">

        <UCard class="my-2">
            <template #header>
                <div class="flex justify-between items-center">
                    <h2 class="font-bold">Evolucion Historia Clinica</h2>
                    <div class="flex gap-3 my-3">
                        <UInput v-model="search" placeholder="Buscar" />
                        <UPagination v-model="pagination.page" :page-count="pagination.pageSize"
                            :total="pagination.resultsCount" />
                    </div>
                </div>
            </template>
            <div class="flex justify-center items-center">
                <h3 v-if="records.length === 0">No hay Evoluciones en esta Historias Clinicas</h3>
            </div>
            <div>

            </div>
            <table class="table-auto w-full permission-table">
                <thead>
                    <tr>
                        <th :class="ui.th">Fecha</th>
                        <th :class="ui.th">Medico</th>
                        <th :class="ui.th">Observacion</th>
                        <th :class="ui.th">Firma</th>

                    </tr>
                </thead>
                <tbody>

                    <tr v-for="(record, index) in records" :key="index">
                        <td :class="ui.td" style="overflow: hidden; width:10%">
                            <div>
                                {{ formatDateYYYYMMDD(record.date_time) }}
                            </div>
                        </td>
                        <td :class="ui.td" style="overflow: hidden; width:15%">
                            <div>
                                Dr(a){{ modelValue.calendarEvent?.medic.name }} {{
                                    modelValue.calendarEvent?.medic.last_name }}
                            </div>
                        </td>
                        <td :class="ui.td" style="overflow: hidden; width: 50%">
                            <div>
                                <UTextarea :rows="3" placeholder="Observación" v-model="record.observation"
                                    style="width: 100%; border: none; pointer-events: none;" class="m-2" disabled />
                            </div>
                        </td>
                        <td :class="ui.td">
                            <div class="flex items-center justify-center">

                                <img :src="record.signed" alt="Imagen Base64" width="60%" height="auto" />
                            </div>
                            <div class="flex items-center justify-center">
                                <strong>
                                    <hr style="border: 1px solid black; font-weight: bold;">
                                    <p>
                                        Dr(a). {{ modelValue.calendarEvent?.medic.name }} {{
                                            modelValue.calendarEvent?.medic.last_name }}
                                    </p>
                                </strong>
                            </div>
                        </td>

                    </tr>
                    <tr>
                        <td :class="ui.td" style="overflow: hidden; width:10%">
                            <div>
                                {{ formatDateYYYYMMDD(getCurrentDate()) }}
                            </div>
                        </td>
                        <td :class="ui.td" style="overflow: hidden; width:15%">
                            <div>
                                Dr(a){{ modelValue.calendarEvent?.medic.name }} {{
                                    modelValue.calendarEvent?.medic.last_name }}
                            </div>
                        </td>
                        <td :class="ui.td" style="overflow: hidden; width: 50%">
                            <div>
                                <UTextarea :rows="3" placeholder="Observación" v-model="newObservation"
                                    style="width: 100%;" class="m-2" />
                            </div>
                        </td>
                        <td :class="ui.td">
                            <div class="flex items-center justify-center">
                                <button v-if="newObservation" @click="signedRecord()">
                                    🖋️
                                </button>

                            </div>
                            <div class="flex items-center justify-center">
                                <strong>
                                    <hr style="border: 1px solid black; font-weight: bold;">
                                    <p>
                                        Dr(a). {{ modelValue.calendarEvent?.medic.name }} {{
                                            modelValue.calendarEvent?.medic.last_name }}
                                    </p>
                                </strong>
                            </div>
                        </td>

                    </tr>
                </tbody>
            </table>
        </UCard>
    </div>
    <ModalSign  :record="newRecordDetail" @close="handleModalClose" v-model="isSing" :detail="detail" :typeThird="'signed'" />
</template>


<script setup lang="ts">

const modelValue = defineProps({
    calendarEvent: Object,
})

const details = ref<any[]>([])
const newSing = ref('')
const newObservation = ref('')
const newRecordDetail = ref('')

const detail = ref(true)
const isSing = ref(false)

type Records = {
    id: number,
    date_time: string,
    third_medic_full: {
        id: number,
        name: string,
        second_name: string,
        last_name: string,
        second_last_name: string,
    },
    records_details: {
        id: number,
        signed: string,
        observation: string,
        date_time: string,
    }[]
}

onMounted(() => {
    fetchRecord()
});

const {
    data: records,
    pagination,
    search,
    pending,
} = usePaginatedFetch<any>("/api/records/" + modelValue.calendarEvent?.record + "/records_details/");


const fetchRecord = async () => {
    const {
        data: records,
        pagination,
        search,
        pending,
    } = usePaginatedFetch<any>("/api/records/" + modelValue.calendarEvent?.record + "/records_details/");
    
}

const createRecordDetail = async () => {
    const message = confirm('¿Estás seguro de crear esta Observacion?')

    if (!message) {
        newObservation.value = ''
        fetchRecord()
        return
    }

    const response = await $fetch('api/records_details/', {
        method: 'POST',
        body: {
            observation: newObservation.value,
            record: modelValue.calendarEvent?.record
        }
    })
    fetchRecord()
    newObservation.value = ''
    newRecordDetail.value = response?.id
};
const signedRecord = async () => {
    createRecordDetail()
    console.log("NEW RECORD", newRecordDetail)    
    isSing.value = true
};


const handleModalClose = (value: any) => {
    isSing.value = false
    fetchRecord()
}

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

</script>

<style></style>
