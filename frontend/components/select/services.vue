<template>
    <USelectMenu v-model="modelValue" option-attribute="description" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true" @click="clickHandler"
        :placeholder="'Servicio'">
    </USelectMenu>
</template>

<script setup lang="ts">

const options = ref<any[]>([])
const query = ref("")

const modelValue = defineModel<any>({ default: () => ({}) }) // Esto es para que el componente pueda ser usado con v-model

type Props = {
    specialities?: string | number | object | any
    services?: string | number | object | any
}

const props = withDefaults(defineProps<Props>(), {
    specialities: '',
    services: ''
})

console.log('stprops', props)

const clickHandler = () => {
    retrieveFromApi()
}

const retrieveFromApi = async () => {
    const queryParams: any = {
        search: query.value,
    }

    if (props.specialities) {
        queryParams.speciality = props.specialities?.id;
    }

    const response = await $fetch<any>("api/services", {
        query: queryParams
    })

    options.value = response.results
    console.log('optionsTQP', options.value)
}

watch(
    [query, () => props.specialities],
    async ([newQuery, newSpeciality], [oldQuery, oldSpeciality]) => {
        if (oldSpeciality !== newSpeciality) {
            // Si la especialidad cambió, borramos el servicio que teníamos seleccionado
            modelValue.value = {};
        }
        // Llama a retrieveFromApi() aquí o realiza otras acciones necesarias
        retrieveFromApi();
    }
);

</script>



