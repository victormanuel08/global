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


      


    </div>
  
    <ModalNewPolice :third="record.third_patient_full" :typeT="'C'" @close="handleModalClose" v-model="isPolice" />
</template>
<script lang="ts" setup>
import { ref, onMounted, watch } from 'vue';

const props = defineProps({
    calendarEvent: Object,
});

const record = ref({} as Record);
const Location = ref({} as location);
const coordinates = ref("");
const addressOption = ref<any>({});
const isPolice = ref<boolean>(false);
const thirdSelected = ref<any>({});
const detail = ref(false);
const isSing = ref(false);

type location = {
    latitude: number;
    longitude: number;
};

if (props.calendarEvent) {
    record.value = props.calendarEvent as Record;
    if (props.calendarEvent.policy_full) {
        record.value.policy_full = {
            ...props.calendarEvent.policy_full,
            concat: props.calendarEvent.policy_full.name + ' - ' + props.calendarEvent.policy_full.description + ' - ' + props.calendarEvent.policy_full.date_start + ' - ' + props.calendarEvent.policy_full.date_end,
        };
    } else {
        record.value.policy_full = {
            concat: '',
        };
    }
}

console.log('calendarEvent', props.calendarEvent);

const showModalPolice = (value: any) => {
    console.log('showModalThird', thirdSelected);
    isPolice.value = true;
};

const address = ref<any>();

watch(Location, async (newLocation, oldLocation) => {
    if (newLocation.latitude && newLocation.longitude) {
        coordinates.value = newLocation.latitude + ', ' + newLocation.longitude;
    }
});

const validate = (value: any) => {
    if (record.value.address === '') {
        record.value.address = addressOption.value.formatted_address;
    } else {
        if (confirm('El campo ya tiene una dirección previa guardada. ¿Desea guardar la dirección sugerida?')) {
            record.value.address = addressOption.value.formatted_address;
        }
    }
    saveItem(value, 'address', record.value.address);
    saveItem(props.calendarEvent?.id, 'latitude', Location.value.latitude);
    saveItem(props.calendarEvent?.id, 'longitude', Location.value.longitude);
};

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
};

const signedRecord = async () => {
    isSing.value = true;
};

const handleModalClose = async (value: any) => {
    isSing.value = false;
    const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}`);
    record.value.third_medic_full = response.third_medic_full
};

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

    const policyarray = props.calendarEvent?.third_patient_full.policy.map((item: any) => item.id) || [];
    policyarray.push(index);

    const response = await $fetch(`api/thirds/${props.calendarEvent?.third_patient_full.id}`, {
        method: 'PATCH',
        body: JSON.stringify({
            policy: policyarray,
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
            concat: props.calendarEvent.policy_full.name + ' - ' + props.calendarEvent.policy_full.description + ' - ' + props.calendarEvent.policy_full.date_start + ' - ' + props.calendarEvent.policy_full.date_end,
        };
    } else {
        record.value.policy_full = {
            concat: '',
        };
    }
});

const handlePolicyChange = (value: any) => {
    record.value.policy_full = value;
    saveItem(record.value.id, 'policy', value.id);
};
</script>
