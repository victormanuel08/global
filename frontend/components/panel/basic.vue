<template>
    <div>
        <h1>Datos Basicos</h1>

        <div class="grid grid-cols-1  md:grid-cols-1 m-4">

            <div>
                <label class="block text-sm font-medium text-gray-700">Motivo Servicio:</label>
                <UTextarea v-model="record.reason_consultation" variant="outline" placeholder="Motivo de la Consulta"
                    @change="saveItem(record.id, 'reason_consultation', record.reason_consultation)" />
            </div>
        </div>
        <div class="grid grid-cols-1  md:grid-cols-4 m-4">

            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Coordenadas:</label>
                <UInput type="text" :value="'Latitud: ' + Location.latitude + ', Longitud: ' + Location.longitude"
                    readonly />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Sugerencias:</label>
                <SelectAddress :coordinates="coordinates" v-model="addressOption" @change="validate(record.id)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                <UInput variant="outline" v-model="record.address"
                    @change="saveItem(record.id, 'address', record.address)" />
            </div>
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Poliza: <span
                        @click="typeT = 'E', showModalPolice('')">➕</span></label>

                <SelectInsurance v-model="record.policy_full" :third="record.third_patient_full?.id"
                    @change="handlePolicyChange" :placeholder="'Aseguradora'"> </SelectInsurance>
            </div>
        </div>
        <div class="grid grid-cols-1  md:grid-cols-4 m-4">

            <div class="mr-2" v-if="false">
                <label class="block text-sm font-medium text-gray-700">Prioridad:</label>
                <SelectChoice :choiceType="'PRIORITY_CHOICES'" v-model="record.priority_full"
                    @change="saveItem(record.id, 'priority', record.priority_full?.id), console.log(record.priority_full)"
                    :style="record.priority_full?.id === 'R' ? 'background-color: red' : record.priority_full?.id === 'Y' ? 'background-color: yellow' : record.priority_full?.id === 'G' ? 'background-color: green' : record.priority_full?.id === 'W' ? 'background-color: white' : 'background-color: black'"
                    :color="record.priority_full?.id === 'R' ? 'background-color: red' : record.priority_full?.id === 'Y' ? 'background-color: yellow' : record.priority_full?.id === 'G' ? 'background-color: green' : record.priority_full?.id === 'W' ? 'background-color: white' : 'background-color: black'">
                </SelectChoice>
            </div>

            <div class="mr-2" v-if="false">
                <label class="block text-sm font-medium text-gray-700">Condicion Accidentado:</label>
                <SelectChoice :choiceType="'TYPE_ACCIDENT_CHOICES'" v-model="record.condition_full"
                    @change="saveItem(record.id, 'condition', record.condition_full.id)" />
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
 
    <ModalNewPolice :third="record.third_patient_full" :typeT="'C'" @close="handleModalClose" v-model="isPolice" />
</template>

<script lang="ts" setup>




const props = defineProps({
    calendarEvent: Object,
})

const record = ref({} as Record)
if (props.calendarEvent) {
    record.value = props.calendarEvent as Record;
    if (props.calendarEvent.policy_full) {
        record.value.policy_full = {
            ...props.calendarEvent.policy_full,
            concat: props.calendarEvent.policy_full.name + ' - ' + props.calendarEvent.policy_full.description + ' - ' + props.calendarEvent.policy_full.date_start + ' - ' + props.calendarEvent.policy_full.date_end
        };
    } else {
        record.value.policy_full = {
            concat: ''
        };
    }
      
     
}

console.log('calendarEvent', props.calendarEvent)

const Location = ref({} as location)
const coordinates = ref("")
const addressOption = ref<any>({})
const isPolice = ref<boolean>(false)

type location = {
    latitude: number
    longitude: number
}


const showModalPolice = (value: any) => {
    console.log('showModalThird', thirdSelected)
    isPolice.value = true
}

const address = ref<any>()

watch(Location, async (newLocation, oldLocation) => {

    if (newLocation.latitude && newLocation.longitude) {

        coordinates.value = newLocation.latitude + ', ' + newLocation.longitude
       

    }
});

const validate = (value: any) => {

    if (record.value.address === '') {
        record.value.address = addressOption.value.formatted_address
    } else {
        if (confirm(('El campo ya tienen una direccion previa guardada. ¿Desea guardar la direccion sugerida?'))) {
            record.value.address = addressOption.value.formatted_address
        }
    }
    saveItem(value, 'address', record.value.address)
    saveItem(props.calendarEvent?.id, 'latitude', (newLocation.latitude))
    saveItem(props.calendarEvent?.id, 'longitude', (newLocation.longitude))
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






const thirdSelected = ref<any>({})

const detail = ref(false)
const isSing = ref(false)


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
    policy: string,
    policy_full: any,
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
    address: string,
}







const signedRecord = async () => {
    isSing.value = true
}

const handleModalClose = (value: any) => {
    isSing.value = false

}

const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });


};

const savePolicyThird = async (index: number) => {
    console.log('savePolicyThird', index, props.calendarEvent?.third_patient_full.id);
    
    // Obtener el array de IDs de las políticas actuales y agregar el nuevo índice
    const policyarray = props.calendarEvent?.third_patient_full.policy.map((item: any) => item.id) || [];
    policyarray.push(index);

    // Realizar la solicitud PATCH para actualizar el campo policy
    const response = await $fetch(`api/thirds/${props.calendarEvent?.third_patient_full.id}`, {        
        method: 'PATCH',
        body: JSON.stringify({
            policy: policyarray
        }),
    });

    console.log('Response:', response);
};



onMounted(() => {
    getLocation();

    record.value = props.calendarEvent as Record;
    if (props.calendarEvent.policy_full) {
        record.value.policy_full = {
            ...props.calendarEvent.policy_full,
            concat: props.calendarEvent.policy_full.name + ' - ' + props.calendarEvent.policy_full.description + ' - ' + props.calendarEvent.policy_full.date_start + ' - ' + props.calendarEvent.policy_full.date_end
        };
    } else {
        record.value.policy_full = {
            concat: ''
        };
    }
});



const handlePolicyChange = (value: any) => {
    record.value.policy_full = value; 
    saveItem(record.value.id, 'policy', value.id)
    //savePolicyThird(value.id)
}


</script>
<style></style>