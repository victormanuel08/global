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
            <div v-show="manualCoords" class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Coordenadas (Manual):</label>
                <UInput type="text" v-model="manualCoordinates" @input="handleManualCoordinateChange"
                     class="w-full" placeholder="Latitud, Longitud" />
            </div>

            <!-- Checkbox para coordenadas manuales -->
            <div class="mb-6">
                <input type="checkbox" id="manualCoords" v-model="manualCoords" />
                <label for="manualCoords" class="ml-2 text-sm font-medium text-gray-700">Usar coordenadas manuales</label>
            </div>

            <!-- Sugerencias -->
            <div class="col-span-full md:col-span-1">
                <label class="block text-sm font-medium text-gray-700 mb-2">Sugerencias:</label>
                <SelectAddress :coordinates="manualCoords ? manualCoordinates : coordinates" v-model="addressOption"
                    @change="validate(record.address)" class="w-full" />
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

        <!-- Modal Póliza -->
        <ModalNewPolice :third="record.third_patient_full" :typeT="'C'" @close="isPolice = false" v-model="isPolice" />
    </div>
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
const manualCoordinates = ref("");  // Coordenadas manuales
const addressOption = ref<any>({});
const manualCoords = ref(false);  // Estado para el checkbox de coordenadas manuales
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

// Mostrar el modal de la póliza
const showModalPolice = (value: any) => {
    isPolice.value = true;
};

const address = ref<any>();

// Vigilar las coordenadas
watch(Location, async (newLocation, oldLocation) => {
    if (newLocation.latitude && newLocation.longitude) {
        coordinates.value = newLocation.latitude + ', ' + newLocation.longitude;
    }
});

// Validar y guardar la dirección sugerida
const validate = async (value: any) => {
    try {
        const result = await Swal.fire({
            title: 'Confirmar acción',
            text: '¿Desea guardar la dirección sugerida?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, guardar',
            cancelButtonText: 'No, mantener la actual',
        });

        if (result.isConfirmed) {
            record.value.address = addressOption.value.formatted_address;

            saveItem(props.calendarEvent?.id, 'address', record.value.address);
            saveItem(props.calendarEvent?.id, 'latitude', Location.value.latitude);
            saveItem(props.calendarEvent?.id, 'longitude', Location.value.longitude);

            Swal.fire(
                'Actualizado',
                'La dirección sugerida ha sido guardada.',
                'success'
            );
        } 
    } catch (error: any) {
        toast.add({ title: 'Error al guardar la dirección sugerida', description: error.message });
    }
};

// Obtener ubicación actual
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
                toast.add({ title: 'Error al obtener la ubicación', description: error.message })
            }
        );
    }
};

// Activar el uso de coordenadas manuales
const handleManualCoordsChange = () => {
    // Cuando el checkbox cambie, simplemente no realizamos ninguna acción, solo mostrar u ocultar el campo
    if (!manualCoords.value) {
        manualCoordinates.value = "";  // Limpiamos las coordenadas cuando el checkbox es desmarcado
    }
};

// Detectar el cambio en el campo de coordenadas manuales
const handleManualCoordinateChange = async () => {
    const result = await Swal.fire({
        title: '¿Usar coordenadas manuales?',
        text: '¿Desea utilizar las coordenadas que ha ingresado manualmente?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí, usar',
        cancelButtonText: 'No, mantener coordenadas automáticas',
    });

    if (result.isConfirmed) {
        saveCoordinates();
    }
};

// Guardar las coordenadas manuales en el modelo
const saveCoordinates = async () => {
    const [lat, lng] = manualCoordinates.value.split(",").map(Number);

    // Asignar las coordenadas al modelo
    record.value.latitude = lat;
    record.value.longitude = lng;

    // Llamar a la función para guardar en el backend
    await saveItem(record.value.id, 'latitude', lat);
    await saveItem(record.value.id, 'longitude', lng);

    // También cargar la dirección correspondiente si las coordenadas son válidas
    loadAddressFromCoordinates(manualCoordinates.value);
};

// Cargar dirección desde las coordenadas
const loadAddressFromCoordinates = async (coords: string) => {
    const [lat, lng] = coords.split(",").map(Number);

    // Hacer la solicitud a la API para obtener la dirección
    const response: { address: string, length: number } = await $fetch(`api/geocode/?coordinates=${lat},+${lng}`);

    // Verificar si la respuesta contiene una dirección válida
    if (response.length > 0) {
        addressOption.value = response.address;  // Actualizar el select de direcciones

        // Actualizar latitude y longitude en el backend usando saveItem
        await saveItem(record.value.id, 'latitude', lat);
        await saveItem(record.value.id, 'longitude', lng);
    } else {
        toast.add({ title: 'No se encontró la dirección', description: 'No se pudo obtener la dirección para estas coordenadas.' });
    }
};


// Guardar item
const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    if (response) {
        toast.add({ title: 'Guardado', description: 'El registro ha sido actualizado correctamente.' });
        console.log('response', response);
    }

};

// Cambiar póliza
const handlePolicyChange = (value: any) => {
    record.value.policy_full = value;
    saveItem(record.value.id, 'policy', value.id);
};

// Cerrar modal
const handleModalClose = async (value: any) => {
    isSing.value = false;
    const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}`);
    record.value.third_medic_full = response.third_medic_full
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
</script>
