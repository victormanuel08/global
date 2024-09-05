<template>
    <USelectMenu v-model="modelValue" option-attribute="namenit" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true" @click="clickHandler"
        :placeholder="props.thirdType === 'P' ? 'Paciente' : props.thirdType === 'M' ? 'Médico' : props.thirdType === 'E' ? 'Entidad' : 'Clínica'">
    </USelectMenu>

</template>
<script setup lang="ts">

const options = ref<any[]>([])
const query = ref("")
const typeThird = ref('asasasa')

const modelValue = defineModel<any>({ default: () => ({}) }) //Esto es para que el componente pue1da ser usado con v-model


type Props = {
    third?: object
    thirdType?: string
    specialities?: string | number
    policeType?: string
}


const props = withDefaults(defineProps<Props>(), {
    third: {},
    thirdType: '',
    specialities: '',
    policeType: ''
})

console.log('stprops', props)

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

    if (props.third && props.thirdType === 'SE') {
        console.log('props.thirdapi', props.third)
        response.results.push(props.third)
    }

    options.value = response.results
    console.log('optionsTQP', options.value)

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
