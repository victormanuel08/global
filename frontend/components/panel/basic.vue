<template>
    <div>
        <h1>Datos Basicos</h1>
        <div class="grid grid-cols-1  md:grid-cols-4 m-4">

            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Prioridad:</label>
                <SelectChoice :choiceType="'PRIORITY_CHOICES'" v-model="record.priority_full"
                    @change="saveItem(record.id, 'priority', record.priority_full.id), console.log(record.priority_full)"
                    :style="record.priority_full?.id === 'R' ? 'background-color: red' : record.priority_full?.id === 'Y' ? 'background-color: yellow' : record.priority_full?.id === 'G' ? 'background-color: green' : record.priority_full?.id === 'W' ? 'background-color: white' : 'background-color: black'"
                    :color="record.priority_full?.id === 'R' ? 'background-color: red' : record.priority_full?.id === 'Y' ? 'background-color: yellow' : record.priority_full?.id === 'G' ? 'background-color: green' : record.priority_full?.id === 'W' ? 'background-color: white' : 'background-color: black'">
                </SelectChoice>
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Causa Externa:</label>
                <SelectChoice :choiceType="'EXTERNAL_CAUSE_CHOICES'" v-model="record.external_cause_full"
                    @change="saveItem(record.id, 'external_cause', record.external_cause_full.id)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Condicion Accidentado:</label>
                <SelectChoice :choiceType="'TYPE_ACCIDENT_CHOICES'" v-model="record.condition_full"
                    @change="saveItem(record.id, 'condition', record.condition_full.id)" />
            </div>
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
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Coordenadas:</label>
               
                <UInput type="text" :value="'Latitud: ' + Location.latitude + ', Longitud: ' + Location.longitude" readonly />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                <UInput></UInput>
            </div>
        </div>

        <div class="grid grid-cols-1  md:grid-cols-1 m-4">

            <div>
                <label class="block text-sm font-medium text-gray-700">Motivo Servicio:</label>
                <UTextarea v-model="record.reason_consultation" variant="outline" placeholder="Motivo de la Consulta"
                    @change="saveItem(record.id, 'reason_consultation', record.reason_consultation)" />
            </div>
        </div>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-4 m-4">
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Original: </label>
                <SelectDiagnoses v-model="record.diagnosis_full"
                    @change="saveItem(record.id, 'diagnosis', record.diagnosis_full?.id)" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Primario: </label>
                <SelectDiagnoses v-model="record.diagnosis_1_full"
                    @change="saveItem(record.id, 'diagnosis_1', record.diagnosis_1_full?.id)" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Secundario: </label>
                <SelectDiagnoses v-model="record.diagnosis_2_full"
                    @change="saveItem(record.id, 'diagnosis_2', record.diagnosis_2_full?.id)" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Diagnostico Terceario: </label>
                <SelectDiagnoses v-model="record.diagnosis_3_full"
                    @change="saveItem(record.id, 'diagnosis_3', record.diagnosis_3_full?.id)" />
            </div>
        </div>
        <div class="grid grid-cols-1 gap-4 md:grid-cols-4 border-solid mt-6">
            <div></div>
            <div></div>
            <div></div>
            <div>
                <button @click="signedRecord()">
                    🖋️ Click para firmar y aceptar.
                </button>
                <img :src="record.signed" alt="Imagen Base64" width="60%" height="auto" v-if="record.signed" />
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_medic_full?.name }} {{ record.third_medic_full?.second_name }} {{
                            record.third_medic_full?.last_name }} {{ record.third_medic_full?.second_last_name }}
                    </p>
                    <p>
                        Esp. {{ record.third_medic_full?.speciality_full?.description }}
                    </p>
                </strong>
            </div>

        </div>

    </div>
    <ModalSign :record="record" @close="handleModalClose" v-model="isSing" :detail="detail" :typeThird="'signed'" />
    <ModalEditThird :third="thirdSelected" :typeT="'E'" @close="handleModalClose" v-model="isThird" />
</template>

<script lang="ts" setup>

const props = defineProps({
    calendarEvent: Object,
})

const Location = ref({}as location)

type location = {
  latitude:number
  longitude:number
}

const getLocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                Location.value = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                };
            },
            (error) => {
                console.error('Error al obtener la ubicación:', error.message);
            }
        );
    } else {
        console.error('Geolocalización no está disponible en este navegador.');
    }
}
function getColorForPriority(priorityName: any) {
    console.log('color', priorityName)
    switch (priorityName) {
        case 'red':
            return 'red'; // Color para alta prioridad
        case 'yellow':
            return 'yellow'; // Color para prioridad media
        case 'Baja':
            return '#4CAF50'; // Color para baja prioridad
        default:
            return '#CCCCCC'; // Color predeterminado (gris claro)
    }
}



const isThird = ref(false)
const thirdSelected = ref<any>({})

const detail = ref(false)
const isSing = ref(false)
const glasgow = ref<any>(0)

type Record = {
    id: number,
    reason_consultation: string,
    diagnosis: string,
    diagnosis_full: any
    diagnosis_1_full: any
    diagnosis_2_full: any
    diagnosis_3_full: any
    third_patient_full: {
        id: number,
        name: string,
        second_name: string,
        last_name: string,
        second_last_name: string,
    },
    third_medic_full: any
    third_entity_full: any
    service_full: any
    fee_full: any
    third_entity: number
    diagnoses_1: string,
    diagnoses_2: string,
    diagnoses_3: string,
    signed: string,
    priority: string,
    priority_full: any,
    external_cause: string,
    external_cause_full: any,
    glasgow_ro: string,
    glasgow_ro_full: any,
    glasgow_rv: string,
    glasgow_rv_full: any,
    glasgow_rm: string,
    glasgow_rm_full: any,
    condition_full: any,
    ef_fc: string,
    ef_fr: string,
    ef_pa: string,
    ef_temp: string,
    condition: string,
}
const record = ref({} as Record)

const color = ref({ backgroundColor: getColorForPriority(record.value.priority_full?.name) });

const signed = ref(record.value.signed)
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

const signedRecord = async () => {
    isSing.value = true
}

const handleModalClose = (value: any) => {
    isSing.value = false
    retrieveFromApi(props.calendarEvent?.id)
}

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

};

onMounted(() => {

    getLocation()
    retrieveFromApi(props.calendarEvent?.id);
    const signed = ref(record.value.signed);
    glasgow.value = parseInt(record.value.glasgow_ro) + parseInt(record.value.glasgow_rv) + parseInt(record.value.glasgow_rm);
});



const showModalThird = (value: any) => {
    thirdSelected.value = value

    isThird.value = true

}



</script>
<style></style>