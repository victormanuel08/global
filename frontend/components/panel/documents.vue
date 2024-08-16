<template>
    <div>

        <div class="grid grid-cols-1  md:grid-cols-4">
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Vitaidad</label>
                <UCheckbox v-model="record.live" class="border rounded p-1" label="Esta con Vida"
                    @change="saveItem(record.id, 'live', record.live)" />
            </div>

            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Hora Legada:</label>
                <UInput type="time" v-model="record.time_start" variant="outline"
                    placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'time_start', record.time_start)" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Hora Destino:</label>
                <UInput type="time" v-model="record.time_end" variant="outline" placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'time_end', record.time_end)" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tipo Solicitud:</label>
                <SelectChoice :choiceType="'HALF_CHOICES'" v-model="record.half_full"
                    @change="saveItem(record.id, 'half', record.half_full.id)" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Clinica: <span
                        @click="typeT = 'C', typeTA='A', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'C'" v-model="record.third_clinic_full"
                    @change="saveItem(record.id, 'third_clinic', record.third_clinic_full.id)">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Conductor: <span
                        @click="typeT = 'P', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'P'" v-model="record.third_driver_full"
                    @change="saveItem(record.id, 'third_driver', record.third_driver_full.id)"
                    :placeholder="'Conductor'">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Medico Clinica: <span
                        @click="typeT = 'M', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'M'" v-model="record.third_medic_clinic_full"
                    @change="saveItem(record.id, 'third_medic_clinic', record.third_medic_clinic_full.id)">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Poliza: <span
                        @click="typeT = 'E', showModalPolice('')">➕</span></label>
                <SelectInsurance v-model="record.policy_full" 
                    :third="record.third_patient_full?.id"
                    @change="saveItem(record.id, 'policy', record.policy_full?.id)"
                    :placeholder="'Aseguradora'">
                </SelectInsurance>
            </div>

            <div  class="m-2">
                <label class="block text-sm font-medium text-gray-700">N° Reporte Ingreso clinica</label>
                <UInput v-model="record.number_report"  placeholder="N° Reporte Ingreso clinica" 
                    @change="saveItem(record.id, 'number_report', record.number_report)" />
            </div>
        </div>



        <div class="grid grid-cols-1  md:grid-cols-1" >
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Observaciones Traslado:</label>
                <UTextarea v-model="record.observations" variant="outline" placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'observations', record.observations)"></UTextarea>
            </div>
 

        </div>

        <div class="grid grid-cols-1  md:grid-cols-3">
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgcc')">
                    📷 CEDULA
                </button>
                <img :src="record.imgcc" width="60%" height="auto" v-if="record.imgcc" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgso')">
                    📷 SOAT
                </button>
                <img :src="record.imgso" alt="Imagen Base64" width="60%" height="auto" v-if="record.imgso" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgtp')">
                    📷 TARJETA PROPIEDAD
                </button>
                <img :src="record.imgtp" alt="Imagen Base64" width="60%" height="auto" v-if="record.imgtp" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imglc')">
                    📷 LICENCIA CONDUCIR
                </button>
                <img :src="record.imglc" alt="Imagen Base64" width="60%" height="auto" v-if="record.imglc" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgco')">
                    📷 CONSENTIMIENTO
                </button>
                <img :src="record.imgco" alt="Imagen Base64" width="60%" height="auto" v-if="record.imgco" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgic')">
                    📷 INGRESO CLINICA
                </button>
                <img :src="record.imgic" alt="Imagen Base64" width="60%" height="auto" v-if="record.imgic" />
            </div>

        </div>

        <div class="grid grid-cols-1  md:grid-cols-5">
           <div></div>
            <div class="m-5">
                <button @click="signedRecord('signed')">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed" alt="Imagen Base64" width="60%" height="auto" v-if="record.signed" />
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_medic_clinic_full?.name }} {{ record.third_medic_clinic_full?.second_name }} {{
                            record.third_medic_clinic_full?.last_name }} {{ record.third_medic_clinic_full?.second_last_name }}
                    </p>
                </strong>
            </div>
            
            <div class="m-5">
                <button @click="signedRecord('signed_recived')">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed_recived" alt="Imagen Base64" width="60%" height="auto"
                    v-if="record.signed_recived" />
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_clinic_full?.name }} {{ record.third_clinic_full?.second_name }} {{
                            record.third_clinic_full?.last_name }} {{ record.third_clinic_full?.second_last_name }}
                    </p>
                </strong>
            </div>
            
            <div class="m-5">
                <button @click="signedRecord('signed_driver')">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed_driver" alt="Imagen Base64" width="60%" height="auto"
                    v-if="record.signed_driver" />
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Conductor: {{ record.third_driver_full?.name }} {{ record.third_driver_full?.second_name }} {{
                            record.third_driver_full?.last_name }} {{ record.third_driver_full?.second_last_name }}
                    </p>
                </strong>
            </div>

  
        </div>
    </div>
    <ModalSign :record="record" @close="handleModalClose" v-model="isSing" :detail="detail" :typeThird="typeSing" />
    <ModalPhoto :record="record" @close="handleModalClose" v-model="isPhoto" :detail="detail" :typeImg="typeImg" />
    <ModalEditThird  :typeT="typeT"   v-model="isThird" />
    <ModalNewPolice :third="record.third_patient_full" :typeT="'C'" @close="handleModalClose" v-model="isPolice" />

</template>

<script lang="ts" setup>

const typeSing = ref('')

const typeImg = ref('')
const isSing = ref(false)

const detail = ref(false)
const typeT = ref('')

const isThird = ref(false)
const isPhoto = ref(false)
const isPolice = ref(false)

const thirdSelected = ref<any>({})

const showModalThird = (value: any) => {

    console.log('showModalThird', thirdSelected)
    isThird.value = true

}

const showModalPolice = (value: any) => {
    console.log('showModalThird', thirdSelected)
    isPolice.value = true
}


const props = defineProps({
    calendarEvent: Object,
})

const record = ref({} as any)

onMounted(() => {
    fetchRecord(props.calendarEvent?.id)
});

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    record.value = response
    console.log('RECORDobjets', record.value)
    record.value.half_full = await getCHOICE(record.value.half, 'HALF_CHOICES')

}

const signedRecord = async (q: string) => {
    typeSing.value = q
    isSing.value = true
}

const photoRecord = async (q: string) => {
    typeImg.value = q
    isPhoto.value = true
}

const handleModalClose = async (value: any) => {
    isSing.value = false
    isPhoto.value = false
    //thirdSelected.value = {}
    console.log('handleModalClose', thirdSelected)
    console.log('handleModalClose', props.calendarEvent)
    await fetchRecord(props.calendarEvent?.id)

}

const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    await fetchRecord(props.calendarEvent?.id)

};

watch(isPhoto, (value) => {
    console.log('isPhoto', isPhoto)
    if (!value) {
        fetchRecord(props.calendarEvent?.id)
    }
});

watch(isSing, (value) => {
    console.log('isSing', isSing)
    if (!value) {
        fetchRecord(props.calendarEvent?.id)
    }
})

</script>

<style></style>
