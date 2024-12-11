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
                <label class="block text-sm font-medium text-gray-700">Transportado a: <span
                        @click="typeT = 'C', typeTA = 'A', typeTT = 'Clinica', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'C'" v-model="record.third_clinic_full"
                    @change="saveItem(record.id, 'third_clinic', record.third_clinic_full.id)">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Medico Clinica: <span
                        @click="typeT = 'M', typeTT = 'Medico', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'M'" v-model="record.third_medic_clinic_full"
                    @change="saveItem(record.id, 'third_medic_clinic', record.third_medic_clinic_full.id)">
                </SelectThird>
            </div>

            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Conductor: <span
                        @click="typeT = 'O', typeTT = 'Conductor', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'O'" v-model="record.third_driver_full"
                    @change="saveItem(record.id, 'third_driver', record.third_driver_full.id)"
                    :placeholder="'Conductor'">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Auxiliar: <span
                        @click="typeT = 'M', typeTT = 'Auxiliar', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'M'" v-model="record.third_medic_full"
                    @change="saveItem(record.id, 'third_medic', record.third_medic_full.id)">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Ambulancia:</label>
                <SelectVehicle v-model="record.vehicle_full"
                    @change="saveItem(record.id, 'vehicle', record.vehicle_full.id)" :vehicleType="'AM'" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">N° Id. Reporte Ingreso clinica</label>
                <UInput v-model="record.number_report" placeholder="N° Id. Reporte Ingreso clinica"
                    @change="saveItem(record.id, 'number_report', record.number_report)" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Condicion Accidentado:</label>
                <SelectChoice :choiceType="'TYPE_ACCIDENT_CHOICES'" v-model="record.condition_full"
                    @change="saveItem(record.id, 'condition', record.condition_full.id)" />
            </div>
        </div>



        <div class="grid grid-cols-1  md:grid-cols-1">
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Observaciones Traslado:</label>
                <UTextarea v-model="record.observations" variant="outline" placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'observations', record.observations)"></UTextarea>
            </div>


        </div>

        <div class="grid grid-cols-2  md:grid-cols-5">
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgcc')">
                    📷 CEDULA
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgcc" v-if="record.imgcc"
                    @click="imgPreview(record.imgcc)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgso')">
                    📷 SOAT
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgso" v-if="record.imgso"
                    @click="imgPreview(record.imgso)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgtp')">
                    📷 T.PROPIEDAD
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgtp" v-if="record.imgtp"
                    @click="imgPreview(record.imgtp)" />
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imglc')">
                    📷 LICENCIA
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imglc" v-if="record.imglc"
                    @click="imgPreview(record.imglc)" />
            </div>

            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imgic')">
                    📷 IN. CLINICA
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imgic" v-if="record.imgic"
                    @click="imgPreview(record.imgic)" />
            </div>
            <!--
            <div class="border rounded p-1 m-2">
                <button @click="photoRecord('imghd')">
                    📷 Huella
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imghd" v-if="record.imghd"
                    @click="imgPreview(record.imghd)" />
            
            </div>
            <div class="border rounded p-1 m-2">
                <button @click="RegenerateHD(record.id)">
                    📷 Huella P.
                </button>
                <NuxtImg sizes="100vw sm:50vw md:100px" :src="record.imghdr" v-if="record.imghd"
                    @click="imgPreview(record.imghdr)" />
            </div>
            -->
        </div>
        <div class="grid grid-cols-1 md:grid-cols-6 gap-5">
            <!-- Espaciador -->
            <div class="m-5"></div>

            <!-- Firmar Clínica -->
            <div class="m-5 flex flex-col items-center text-center min-h-[200px]">
                <button @click="signedRecord('signed_medic_clinic')"
                    v-if="record.third_clinic_full?.id && record.third_medic_clinic_full?.id">
                    🖋️ Firmar
                </button>
                <img :src="record.third_medic_clinic_full?.signed" alt="Imagen Base64" class="w-3/5 h-auto mt-2"
                    v-if="record.third_medic_clinic_full?.signed" />
                <div v-else
                    class="w-3/5 h-[80px] flex items-center justify-center border border-dashed border-gray-400">
                    <span class="text-gray-400 text-sm">Sin imagen</span>
                </div>
                <hr class="border border-black w-full my-2">
                <strong>
                    <p>
                        Dr(a). {{ record.third_clinic_full?.name }} {{ record.third_medic_clinic_full?.name }}
                        {{ record.third_medic_clinic_full?.second_name }} {{ record.third_medic_clinic_full?.last_name
                        }}
                        {{ record.third_medic_clinic_full?.second_last_name }} T.P {{ record.third_medic_clinic_full?.tp
                        }}
                        <span v-if="!record.third_medic_clinic_full?.id">. NO FIRMA.</span>
                    </p>
                </strong>
            </div>

            <!-- Firmar Médico Auxiliar -->
            <div class="m-5 flex flex-col items-center text-center min-h-[200px]">
                <button @click="signedRecord('signed_medic')">🖋️ Firmar</button>
                <img :src="record.third_medic_full?.signed" alt="Imagen Base64" class="w-3/5 h-auto mt-2"
                    v-if="record.third_medic_full?.signed" />
                <div v-else
                    class="w-3/5 h-[80px] flex items-center justify-center border border-dashed border-gray-400">
                    <span class="text-gray-400 text-sm">Sin imagen</span>
                </div>
                <hr class="border border-black w-full my-2">
                <strong>
                    <p>
                        Dr(a). Auxiliar {{ record.third_medic_full?.name }} {{ record.third_medic_full?.second_name }}
                        {{ record.third_medic_full?.last_name }} {{ record.third_medic_full?.second_last_name }}
                    </p>
                    <p>
                        Esp. {{ record.third_medic_full?.speciality_full?.description }} T.P {{
                            record.third_medic_full?.tp }}
                    </p>
                </strong>
            </div>

            <!-- Firmar Conductor -->
            <div class="m-5 flex flex-col items-center text-center min-h-[200px]">
                <button @click="signedRecord('signed_driver')" v-if="record.third_driver">
                    🖋️ Firmar
                </button>
                <img :src="record.third_driver_full?.signed" alt="Imagen Base64" class="w-3/5 h-auto mt-2"
                    v-if="record.third_driver_full?.signed" />
                <div v-else
                    class="w-3/5 h-[80px] flex items-center justify-center border border-dashed border-gray-400">
                    <span class="text-gray-400 text-sm">Sin imagen</span>
                </div>
                <hr class="border border-black w-full my-2">
                <strong>
                    <p>
                        Conductor: {{ record.third_driver_full?.name }} {{ record.third_driver_full?.second_name }}
                        {{ record.third_driver_full?.last_name }} {{ record.third_driver_full?.second_last_name }}
                        <span v-if="!record.third_driver_full?.signed">. NO FIRMA.</span>
                    </p>
                </strong>
            </div>

            <!-- Firmar Paciente -->
            <div class="m-5 flex flex-col items-center text-center min-h-[200px]">
                <button @click="signedRecord('signed_patient')" v-if="record.third_patient">
                    🖋️ Firmar
                </button>
                <span class="flex justify-center items-center gap-2 mt-2">
                    <img :src="record.signed_patient" alt="Imagen Base64" class="w-3/5 h-auto"
                        v-if="record.signed_patient" />
                    <div v-else
                        class="w-3/5 h-[80px] flex items-center justify-center border border-dashed border-gray-400">
                        <span class="text-gray-400 text-sm">Sin imagen</span>
                    </div>

                </span>
                <hr class="border border-black w-full my-2">
                <strong>
                    <p>
                        Paciente: {{ record.third_patient_full?.name }} {{ record.third_patient_full?.second_name }}
                        {{ record.third_patient_full?.last_name }} {{ record.third_patient_full?.second_last_name }}
                        <span v-if="!record.signed_patient">. NO FIRMA.</span> NO HUELLA
                    </p>
                </strong>
            </div>

            <!-- Espaciador -->
            <div class="m-5"></div>
        </div>


    </div>
    <ModalSign :record="record" @close="handleModalClose" v-model="isSing" :detail="detail" :third="third"
        :typeThird="typeSing" />



    <ModalPhoto :record="record" @close="handleModalClose" v-model="isPhoto" :detail="detail" :typeImg="typeImg" />
    <ModalEditThirdAmbulance :typeT="typeT" v-model="isThird" @thirdCreated="handleThirdCreated"
        @update:isThird="handleModalClose" />

    <ModalImgpreview :imgRoute="imgRoute" @close="handleModalClose" v-model="isPreview" />

</template>

<script lang="ts" setup>

const typeSing = ref('')
const third = ref({} as any)
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
const typeTT = ref('')
const createdThird = ref<any>({})
const toast = useToast()
const thirdSelected = ref<any>({})

const showModalThird = (value: any) => {

    console.log('showModalThird', thirdSelected)
    isThird.value = true
  

}

const imgPreview = (value: any) => {
    imgRoute.value = value
    isPreview.value = true
}




const props = defineProps({
    calendarEvent: Object,
})

const record = ref({} as any)

onMounted(() => {
    fetchRecord(props.calendarEvent?.id)
    fetchProps()
});


const fetchProps = async () => {


    props.calendarEvent.condition_full = await getCHOICE(props.calendarEvent.condition, 'TYPE_ACCIDENT_CHOICES')

}

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    record.value = response
    console.log('RECORDobjets', record.value)
    record.value.half_full = await getCHOICE(record.value.half, 'HALF_CHOICES')
    record.value.condition_full = await getCHOICE(record.value.condition, 'TYPE_ACCIDENT_CHOICES')
    if (typeImg.value === 'imghd') {
        RegenerateHD(record.value.id)
        typeImg.value = ''
    }
}

const signedRecord = async (q: string) => {
    typeSing.value = q
    if (q === 'signed_driver') {
        third.value = record.value.third_driver
    } else if (q === 'signed_medic') {
        third.value = record.value.third_medic
    } else if (q === 'signed_medic_clinic') {
        third.value = record.value.third_medic_clinic
    } else {
        third.value = null
    }
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
    isThird.value = false;  // Cerrar la modal
    console.log('handleModalClose', thirdSelected)
    console.log('handleModalClose', props.calendarEvent)
    await fetchRecord(props.calendarEvent?.id)


}

const handleThirdCreated = (newThird: any) => {
    createdThird.value = newThird; // Aquí puedes manejar el tercero creado (por ejemplo, mostrarlo en una lista)
    console.log('Nuevo tercero creado:', createdThird.value);
    toast.add({ title: ` ${typeTT.value}` });
    if (typeTT.value == 'Medico') {
        record.value.third_medic_clinic_full = newThird;
        saveItem(record.value.id, 'third_medic_clinic', newThird.id);
        toast.add({ title: `Medico Clinica Actulizado` });
    } else if (typeTT.value == 'Conductor') {
        record.value.third_driver_full = newThird;
        saveItem(record.value.id, 'third_driver', newThird.id);
        toast.add({ title: `Condutor Actulizado` });
    } else if (typeTT.value == 'Auxiliar') {
        record.value.third_medic_full = newThird;
        saveItem(record.value.id, 'third_medic', newThird.id);
        toast.add({ title: `Medico Aux Actulizado` });
    }  else if (typeTT.value == 'Clinica') {
        record.value.third_clinic_full = newThird;
        saveItem(record.value.id, 'third_clinic', newThird.id);
        toast.add({ title: `Clinica Actulizado` });
    }
    fetchRecord(record.value.id);

};

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
