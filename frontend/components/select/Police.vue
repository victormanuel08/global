<template>
    <USelectMenu v-model="modelValue" option-attribute="namenit" :options="options" :searchable="true" v-model:query="query"
        :clearSearchOnClose="true" @click="clickHandler"
        :placeholder="props.thirdType === 'P' ? 'Paciente' : props.thirdType === 'M' ? 'Médico' : props.thirdType === 'E' ? 'Entidad' : 'Clínica'"
        >
    </USelectMenu>

</template>
<script setup lang="ts">

const options = ref<any[]>([])
const typeThird = ref('asasasa')
const query = ref("")
const modelValue = defineModel<any>({ default: () => ({}) }) //Esto es para que el componente pue1da ser usado con v-model


type Props = {
    thirdType?: string
    specialities?: string | number
}

const props = withDefaults(defineProps<Props>(), {
    thirdType: '',
    specialities: ''
})

const clickHandler = () => {
    retrieveFromApi()
}

const retrieveFromApi = async () => {
    const queryParams = {
        search: query.value,
        type: props.thirdType,
    }

    if (props.specialities) {
        queryParams.speciality = props.specialities?.id;
    }

    const response = await $fetch<any>("api/thirds", {
        query: queryParams
    })

    options.value = response.results

   
}


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
