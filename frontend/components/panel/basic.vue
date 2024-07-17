<template>
    <div>
        <h1>Datos Basicos</h1>
        <div class="grid grid-cols-1  md:grid-cols-1 m-4">
            <div>
                <label class="block text-sm font-medium text-gray-700">Razon Consulta:</label>                
                <UTextarea  
                    v-model="record.reason_consultation" 
                    variant="outline" 
                    placeholder="Motivo de la Consulta" 
                    @change="saveItem('reason_consultation',record.reason_consultation)"/>
            </div>
        </div>
        <div class="grid grid-cols-4 gap-4 md:grid-cols-4 m-4">
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Original: </label>
                <SelectDiagnoses 
                    v-model="record.diagnosis_full" 
                    class="border rounded p-1 w-80" 
                    @change="saveItem('diagnosis',record.diagnosis_full?.id)"
                />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Primario: </label>
                <SelectDiagnoses 
                    v-model="record.diagnosis_1_full" 
                    class="border rounded p-1 w-80" 
                    @change="saveItem('diagnosis_1',record.diagnosis_1_full?.id)"
                />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Secundario: </label>
                <SelectDiagnoses 
                    v-model="record.diagnosis_2_full" 
                    class="border rounded p-1 w-80" 
                    @change="saveItem('diagnosis_2',record.diagnosis_2_full?.id)"
                />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Terceario: </label>
                <SelectDiagnoses 
                    v-model="record.diagnosis_3_full" 
                    class="border rounded p-1 w-80" 
                    @change="saveItem('diagnosis_3',record.diagnosis_3_full?.id)"
                />
            </div>
        </div>
        <div class="grid grid-cols-4 gap-4 md:grid-cols-4 border-solid mt-6">
            <div ></div>
            <div></div>
            <div></div>
            <div >
                <button  @click="signedRecord()">
                    🖋️
                </button>
                <img  :src="record.signed" alt="Imagen Base64" width="60%" height="auto" />
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_medic_full?.name }} {{ record.third_medic_full?.second_name }} {{
                            record.third_medic_full?.last_name }} {{ record.third_medic_full?.second_last_name }}
                    </p>
                    <p>
                        Esp. {{ record.third_medic_full?.speciality_full.description }} 
                    </p>
                </strong>
            </div>
            
        </div>

    </div>
    <ModalSign  :record="record" @close="handleModalClose" v-model="isSing" :detail="detail"/>
</template>

<script lang="ts" setup>

const records = ref<any[]>([])

const modelValue = defineProps({
    calendarEvent: Object,
})

const detail = ref(false)
const isSing = ref(false)

type Record = {
    reason_consultation: string,
    diagnosis: string,
    diagnosis_full: {
        id: number,
        name: string,
        code: string,
    },
    diagnosis_1_full: {
        id: number,
        name: string,
        code: string,
    },
    diagnosis_2_full: {
        id: number,
        name: string,
        code: string,
    },
    diagnosis_3_full: {
        id: number,
        name: string,
        code: string,
    },
    third_patient_full: {
        id: number,
        name: string,
        second_name: string,
        last_name: string,
        second_last_name: string,
    },
    third_medic_full: {
        id: number,
        name: string,
        second_name: string,
        last_name: string,
        second_last_name: string,
    },
    diagnoses_1: string,
    diagnoses_2: string,
    diagnoses_3: string,
    signed: string,

}
const record = ref({} as Record)
onMounted(() => {
    console.log("RECORDID", modelValue.calendarEvent?.record)
    retrieveFromApi(modelValue.calendarEvent?.record)
    const signed = ref(record.value.signed)
})

const signed = ref(record.value.signed)
const retrieveFromApi = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    console.log("Record", response)
    record.value = response
}

const signedRecord = async () => {
    isSing.value = true
}

const handleModalClose = (value: any) => {
    isSing.value = false
    retrieveFromApi(modelValue.calendarEvent?.record)
}

const saveItem = async (field: string, value: string) => {
  const response = await $fetch(`api/records/${modelValue.calendarEvent?.record}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
    retrieveFromApi(modelValue.calendarEvent?.record)
};

</script>
<style></style>