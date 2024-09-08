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
                        @click="typeT = 'C', typeTA = 'A', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'C'" v-model="record.third_clinic_full"
                    @change="saveItem(record.id, 'third_clinic', record.third_clinic_full.id)">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Ambulancia:</label>
                <SelectVehicle v-model="thirdSelected.vehicle_full"
                    @change="saveItem(thirdSelected.id, 'vehicle', thirdSelected.vehicle_full.id)"
                    :vehicleType="'AM'" />
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
                <SelectInsurance :v-model="record.policy_full" :third="record.third_patient_full?.id"
                    @change="saveItem(record.id, 'policy', record.policy_full?.id)" :placeholder="'Aseguradora'">
                </SelectInsurance>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tipo Identificacion</label>
                <UInput v-model="record.number_report_id" placeholder="TI. Reporte Clinica"
                    @change="saveItem(record.id, 'number_report_id', record.number_report_id)" />
            </div>

            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">N° Id. Reporte Ingreso clinica</label>
                <UInput v-model="record.number_report" placeholder="N° Id. Reporte Ingreso clinica"
                    @change="saveItem(record.id, 'number_report', record.number_report)" />
            </div>
        </div>



        <div class="grid grid-cols-1  md:grid-cols-1">
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Observaciones Traslado:</label>
                <UTextarea v-model="record.observations" variant="outline" placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'observations', record.observations)"></UTextarea>
            </div>


        </div>

        <div class="grid grid-cols-2  md:grid-cols-6">
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgcc')">
                    📷 CEDULA
                </button>                
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgcc"  v-if="record.imgcc" @click="imgPreview(record.imgcc)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgso')">
                    📷 SOAT
                </button>                
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgso"  v-if="record.imgso" @click="imgPreview(record.imgso)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgtp')">
                    📷 T.PROPIEDAD
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgtp"  v-if="record.imgtp" @click="imgPreview(record.imgtp)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imglc')">
                    📷 LICENCIA
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imglc"  v-if="record.imglc" @click="imgPreview(record.imglc)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgco')">
                    📷 CONSENTIMIENTO
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgco"  v-if="record.imgco" @click="imgPreview(record.imgco)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgic')">
                    📷 IN. CLINICA
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgic"  v-if="record.imgic" @click="imgPreview(record.imgic)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imghd')">
                    📷 Huella
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imghd"  v-if="record.imghd" @click="imgPreview(record.imghd)" />
                <!--<a :href="record.imghd" download="huella_original.jpg" v-if="record.imghd">
                    Descargar imagen
                </a>
                -->
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="RegenerateHD(record.id)">
                    📷 Huella P.
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imghdr"  v-if="record.imghd" @click="imgPreview(record.imghdr)" />
            </div>
        </div>

        <div class="grid grid-cols-1  md:grid-cols-5">

            <div class="m-5">
                <button @click="signedRecord('signed')">
                    🖋️ Firmar
                </button>
                <img :src="record.signed" alt="Imagen Base64" width="60%" height="auto" v-if="record.signed" />
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_medic_clinic_full?.name }} {{ record.third_medic_clinic_full?.second_name
                        }} {{
                            record.third_medic_clinic_full?.last_name }} {{ record.third_medic_clinic_full?.second_last_name
                        }}
                    </p>
                </strong>
            </div>

            <div class="m-5">
                <button @click="signedRecord('signed_recived')">
                    🖋️ Firmar
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
                    🖋️ Firmar
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
            <div class="m-5">
                <button @click="signedRecord('signed_patient')">
                    🖋️ Firmar
                </button>
                <span class="flex grid-flow-col">
                    <img :src="record.signed_patient" alt="Imagen Base64" width="60%" height="auto"
                        v-if="record.signed_patient" />
          
                    <NuxtImg  class="rotated-image-transform" sizes="100vw sm:50vw md:70px" :src="record.imghdr"  v-if="record.imghdr" @click="imgPreview(record.imghdr)" />
                </span>
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Paciente: {{ record.third_patient_full?.name }} {{ record.third_patient_full?.second_name }} {{
                            record.third_patient_full?.last_name }} {{ record.third_patient_full?.second_last_name }}
                    </p>
                </strong>
            </div>
        </div>
    </div>
    <ModalSign :record="record" @close="handleModalClose" v-model="isSing" :detail="detail" :typeThird="typeSing" />
    <ModalPhoto :record="record" @close="handleModalClose" v-model="isPhoto" :detail="detail" :typeImg="typeImg" />
    <ModalEditThird :typeT="typeT" v-model="isThird" />
    <ModalNewPolice :third="record.third_patient_full" :typeT="'C'" @close="handleModalClose" v-model="isPolice" />
    <ModalImgpreview :imgRoute="imgRoute" @close="handleModalClose" v-model="isPreview" />

</template>

<script lang="ts" setup>

const typeSing = ref('')
const imgRoute = ref('')

const typeImg = ref('')
const isSing = ref(false)
const isPreview = ref(false)

const detail = ref(false)
const typeT = ref('')

const isThird = ref(false)
const isPhoto = ref(false)
const isPolice = ref(false)
const isDactilar = ref(false)

const thirdSelected = ref<any>({})

const showModalThird = (value: any) => {

    console.log('showModalThird', thirdSelected)
    isThird.value = true

}

const imgPreview = (value: any) => {
    imgRoute.value = value
    isPreview.value = true
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
    if (typeImg.value === 'imghd') {
        RegenerateHD(record.value.id)
        typeImg.value = ''
    }
}

const signedRecord = async (q: string) => {
    typeSing.value = q
    isSing.value = true
}

const RegenerateHD = async (recordId: string) => {
    try {
        const response = await $fetch('api/processimage/', {
            method: 'POST',
            body: JSON.stringify({ record_id: recordId }),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        console.log('Respuesta del servidor:', response);
    } catch (error) {
        console.error('Error al procesar la imagen:', error);
    }
    await fetchRecord(props.calendarEvent?.id)
};


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

<style>
.rotated-image-transform {
    /* Gira la imagen 90 grados hacia la izquierda */
    transform: rotate(-90deg);
}
</style>
