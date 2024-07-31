<template>
    <div>
        
        <div class="grid grid-cols-4  md:grid-cols-4">
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Vitaidad</label>
                <UCheckbox 
                    v-model="record.live" 
                    class="border rounded p-1" 
                    label="Esta con Vida" 
                    @change="saveItem(record.id, 'live', record.live)"
                />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Hora Legada:</label>
                <UInput 
                    type="time" 
                    v-model="record.time_start" 
                    variant="outline" 
                    placeholder="Descripcion de los Objetos" 
                    @change="saveItem(record.id, 'time_start', record.time_start)" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Hora Destino:</label>
                <UInput 
                    type="time" 
                    v-model="record.time_end" 
                    variant="outline" 
                    placeholder="Descripcion de los Objetos" 
                    @change="saveItem(record.id, 'time_end', record.time_end)" />
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tipo Solicitud:</label>             
                <SelectChoice :choiceType="'HALF_CHOICES'" v-model="record.half_full" @change="saveItem(record.id, 'half', record.half_full.id )"/>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Clinica: <span @click="typeT='C', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'C'"  v-model="record.third_clinic_full" @change="saveItem(record.id, 'third_clinic', record.third_clinic_full.id )">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Conductor: <span @click="typeT='P', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'P'"  v-model="record.third_driver_full" @change="saveItem(record.id, 'third_driver', record.third_driver_full.id )" :placeholder="'Conductor'">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Medico Clinica: <span @click="typeT='M', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'M'"  v-model="record.third_medic_clinic_full" @change="saveItem(record.id, 'third_medic_clinic', record.third_medic_clinic_full.id )">
                </SelectThird>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Entidad:  <span @click="typeT='E', showModalThird('')">➕</span></label>
                <SelectThird :third-type="'E'"  v-model="record.third_entity_full" @change="saveItem(record.id, 'third_entity', record.third_entity_full.id )">
                </SelectThird>
            </div>
        </div>

        <div class="grid grid-cols-2  md:grid-cols-2" v-if="record.obj" >
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Observaciones Traslado:</label>
                <UTextarea
                    v-model="record.observations"
                    variant="outline"
                    placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'observations', record.observations)"
                ></UTextarea>
            </div>
            <div class="m-2">
                <label class="block text-sm font-medium text-gray-700">Condicion Accidentado:</label>
                <UTextarea
                    v-model="record.condition"
                    variant="outline"
                    placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'condition', record.condition)"
                ></UTextarea>
            </div>
            
        </div>

        <div class="grid grid-cols-3  md:grid-cols-3"  >
            <div  class="border rounded p-1 m-2">
                <button @click="photoRecord('imgCC')">
                    📷 CEDULA
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
            </div>
            <div  class="border rounded p-1 m-2">
                <button @click="photoRecord('img')">
                    📷 SOAT
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
            </div>
            <div  class="border rounded p-1 m-2">
                <button @click="photoRecord('')">
                    📷 TARJETA PROPIEDAD
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
            </div>
            <div  class="border rounded p-1 m-2">
                <button @click="photoRecord('')">
                    📷 LICENCIA CONDUCIR
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
            </div>
            <div  class="border rounded p-1 m-2">
                <button @click="photoRecord('')">
                    📷 CONSENTIMIENTO
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
            </div>
            <div  class="border rounded p-1 m-2">
                <button @click="photoRecord('')">
                    📷 INGRESO CLINICA
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
            </div>
         
        </div>

        <div class="grid grid-cols-7  md:grid-cols-7"  >
            <div></div>
            <div class="m-5">
                <button @click="signedRecord('signed')">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed"/>
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_medic_full?.name }} {{ record.third_medic_full?.second_name }} {{
                            record.third_medic_full?.last_name }} {{ record.third_medic_full?.second_last_name }}
                    </p>
                </strong>
            </div>
            <div></div>            
            <div class="m-5">
                <button @click="signedRecord('signed_recived')">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed_recived" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_recived"/>
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Dr(a). {{ record.third_clinic_full?.name }} {{ record.third_clinic_full?.second_name }} {{
                            record.third_clinic_full?.last_name }} {{ record.third_clinic_full?.second_last_name }}
                    </p>
                </strong>
            </div>
            <div></div>
            <div class="m-5">
                <button @click="signedRecord('signed_driver')">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed_driver" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_driver"/>
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                        Conductor: {{ record.third_driver_full?.name }} {{ record.third_driver_full?.second_name }} {{
                            record.third_driver_full?.last_name }} {{ record.third_driver_full?.second_last_name }}
                    </p>
                </strong>
            </div>
            <div></div>
        </div>
    </div>
    <ModalSign :record="record" @close="handleModalClose" v-model="isSing" :detail="detail" :typeThird="typeSing" />
    <ModalPhoto :record="record" @close="handleModalClose" v-model="isPhoto" :detail="detail" :typeImg="typeImg" />
    <ModalEditThird  :third="thirdSelected"   :typeT="typeT" @close="handleModalClose" v-model="isThird" />
</template>

<script lang="ts" setup>

const typeSing = ref('')

const typeImg = ref('')
const isSing = ref(false)

const detail = ref(false)
const typeT = ref('')

const isThird = ref(false)
const isPhoto = ref(false)
const thirdSelected = ref<any>({})  

const showModalThird = (value: any) => {
    thirdSelected.value = value
    console.log('showModalThird',thirdSelected)    
    isThird.value = true
    
}

const handleImageUpload = async (event: any) => {
    const file = event.target.files[0];   
};

const modelValue = defineProps({
    calendarEvent: Object,
})

const record = ref({} as any)

onMounted(() => {
    fetchRecord(modelValue.calendarEvent?.record.id)  
});

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)    
    record.value = response  
    console.log('RECORDobjets',record.value)
    record.value.half_full = await getCHOICE(record.value.half, 'HALF_CHOICES')
}

const signedRecord = async (q: string) => {
    typeSing.value = q
    isSing.value = true
}

const photoRecord = async (q: string) => {
    typeImg.value = q
    isPhoto.value = true
    console.log('photoRecord',q)
    console.log('photoRecordtype',typeImg.value)
    console.log('photoRecordreord',record.value)
    console.log('photoRecorddetail',detail.value)
}

const handleModalClose = (value: any) => {
    isSing.value = false
    isPhoto.value = false
    fetchRecord(modelValue.calendarEvent?.record.id)  
   
}

const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    fetchRecord(modelValue.calendarEvent?.record.id)  
};


</script>

<style></style>
