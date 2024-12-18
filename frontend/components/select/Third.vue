<template>
    <USelectMenu
        v-model="modelValue"
        option-attribute="namenit"
        :options="options"
        :searchable="true"
        v-model:query="query"
        :clearSearchOnClose="true"
        @click="clickHandler"
        :placeholder="getPlaceholder"
    >
    </USelectMenu>
</template>

<script setup lang="ts">
import { ref, watch, defineProps, withDefaults } from 'vue';

const options = ref<any[]>([]);
const query = ref("");
const modelValue = ref<any>({}); // Aquí usas un modelo vacío por defecto

// Propiedades
type Props = {
    third?: object;
    thirdType?: string;
    specialities?: string | number;
    policeType?: string;
};

const props = withDefaults(defineProps<Props>(), {
    third: {},
    thirdType: '',
    specialities: '',
    policeType: ''
});

// Función para manejar el click
const clickHandler = () => {
    retrieveFromApi();
};

// Función para obtener el placeholder basado en 'thirdType'
const getPlaceholder = computed(() => {
    return props.thirdType === 'P'
        ? 'Paciente'
        : props.thirdType === 'M'
        ? 'Médico'
        : props.thirdType === 'E'
        ? 'Entidad'
        : props.thirdType === 'C'
        ? 'Clínica'
        : props.thirdType === 'O'
        ? 'Conductor'
        : 'Seleccione una opción';
});

// Función para recuperar los datos desde la API
const retrieveFromApi = async () => {
    const queryParams: any = { search: query.value };

    // Si thirdType es 'M' o 'O', asigna una lista de valores y luego los convierte en una cadena separada por comas
    if (props.thirdType === 'M' || props.thirdType === 'O') {
        queryParams.type = 'M,O'; // Usar una cadena con los tipos separados por coma
    } else {
        queryParams.type = props.thirdType; // Si no, asignar el valor individual
    }

    if (props.specialities) {
        queryParams.speciality = props.specialities; // Asumí que 'specialities' es un ID
    }

    // Hacer la solicitud a la API
    const response = await $fetch<any>("api/thirds", {
        query: queryParams
    });

    // Si hay un tercero (props.third) y el tipo es 'SE', lo agregamos a los resultados
    if (props.third && props.thirdType === 'SE') {
     
        response.results.push(props.third);
    }

    // Asignamos los resultados a las opciones
    options.value = response.results;
  
};


// Observar cambios en el query y specialities
watch(
    [query, () => props.specialities],
    async ([newQuery, newSpeciality], [oldQuery, oldSpeciality]) => {
        if (oldSpeciality !== newSpeciality) {
            // Si la especialidad cambió, borramos el tercero que teníamos seleccionado
            modelValue.value = {};
        }
        // Llama a retrieveFromApi() aquí o realiza otras acciones necesarias
        retrieveFromApi();
    }
);
</script>
