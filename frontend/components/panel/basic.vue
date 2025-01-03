<template>
    <div class="p-4">
        <h1 class="text-lg font-bold text-gray-700 mb-6 text-center md:text-left">Datos Básicos</h1>

        <!-- Motivo Servicio -->
        <div class="mb-6">
            <label class="block text-sm font-medium text-gray-700 mb-2">Motivo Servicio:</label>
            <UTextarea v-model="record.reason_consultation" variant="outline" placeholder="Motivo de la Consulta"
                @change="saveItem(record.id, 'reason_consultation', record.reason_consultation)" class="w-full" />
        </div>

        <!-- Coordenadas, Sugerencias, Dirección y Póliza -->
        <div class="grid grid-cols-1 gap-6 md:grid-cols-5">
            <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Ciudad:</label>
                <SelectCities v-model="record.city_full" @change="saveItem(record.id, 'city', record.city_full.id)"
                    class="w-full" />
            </div>
            <!-- Coordenadas -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Coordenadas:</label>
                <UInput type="text" :value="'Latitud: ' + Location.latitude + ', Longitud: ' + Location.longitude"
                    readonly class="w-full" />
            </div>

            <!-- Sugerencias -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Sugerencias:</label>
                <SelectAddress :coordinates="coordinates" v-model="addressOption" @change="validate(record.address)"
                    class="w-full" />
            </div>

            <!-- Dirección -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Dirección:</label>
                <UInput variant="outline" v-model="record.address"
                    @change="saveItem(record.id, 'address', record.address)" class="w-full" />
            </div>

            <!-- Póliza -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">
                    Póliza:
                    <span class="text-blue-500 cursor-pointer hover:underline"
                        @click="typeT = 'E'; showModalPolice('')">➕
                    </span>
                </label>
                <SelectInsurance v-model="record.policy_full" :third="record.third_patient_full?.id"
                    @change="handlePolicyChange" :placeholder="'Aseguradora-Póliza-Fecha Inicio-Fecha Fin'"
                    class="w-full" />
            </div>
        </div>

        <!-- Campos Ocultos -->
        <div class="grid grid-cols-1 gap-6 md:grid-cols-4 mt-6" v-if="false">
            <!-- Prioridad -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Prioridad:</label>
                <SelectChoice :choiceType="'PRIORITY_CHOICES'" v-model="record.priority_full"
                    @change="saveItem(record.id, 'priority', record.priority_full?.id)"
                    :style="getPriorityStyle(record.priority_full?.id)" class="w-full" />
            </div>

            <!-- Condición Accidentado -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Condición Accidentado:</label>
                <SelectChoice :choiceType="'TYPE_ACCIDENT_CHOICES'" v-model="record.condition_full"
                    @change="saveItem(record.id, 'condition', record.condition_full.id)" class="w-full" />
            </div>
        </div>
    </div>

    <!-- Modal Póliza -->
    <ModalNewPolice :third="record.third_patient_full" :typeT="'C'" @close="handleModalClose" v-model="isPolice" />
</template>

<script lang="ts" setup>
import { ref, onMounted, watch } from 'vue';
import Swal from 'sweetalert2';

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
const toast = useToast();


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

//console.log('calendarEvent', props.calendarEvent);

const showModalPolice = (value: any) => {
    //console.log('showModalThird', thirdSelected);
    isPolice.value = true;
};

const address = ref<any>();

watch(Location, async (newLocation, oldLocation) => {
    if (newLocation.latitude && newLocation.longitude) {
        coordinates.value = newLocation.latitude + ', ' + newLocation.longitude;
    }
});

const validate = async (value: any) => {
    try {
        // Verifica si `value` no es null, undefined ni vacío


        // Asegúrate de que el `Swal.fire` se ejecuta
        const result = await Swal.fire({
            title: 'Confirmar acción',
            text: '¿Desea guardar la dirección sugerida?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, guardar',
            cancelButtonText: 'No, mantener la actual',
        });

        // Si el usuario confirma
        if (result.isConfirmed) {
            record.value.address = addressOption.value.formatted_address;

            saveItem(value, 'address', record.value.address);
            saveItem(props.calendarEvent?.id, 'latitude', Location.value.latitude);
            saveItem(props.calendarEvent?.id, 'longitude', Location.value.longitude);

            Swal.fire(
                'Actualizado',
                'La dirección sugerida ha sido guardada.',
                'success'
            );
        } 


    } catch (error: any) {
        // Si ocurre algún error, lo mostramos en el toast
        toast.add({ title: 'Error al guardar la dirección sugerida', description: error.message });
    }
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
                //console.error('Error al obtener la ubicación:', error.message);
                toast.add({ title: 'Error al obtener la ubicación ', description: error.message })
            }
        );
    } else {

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
    //console.log('savePolicyThird', index, props.calendarEvent?.third_patient_full.id);

    const policyarray = props.calendarEvent?.third_patient_full.policy.map((item: any) => item.id) || [];
    policyarray.push(index);

    const response = await $fetch(`api/thirds/${props.calendarEvent?.third_patient_full.id}`, {
        method: 'PATCH',
        body: JSON.stringify({
            policy: policyarray,
        }),
    });

    //console.log('Response:', response);
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
