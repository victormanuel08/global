<template>
    <USelectMenu v-model="modelValue" option-attribute="nit" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true" @click="clickHandler">
    </USelectMenu>
</template>
<script setup lang="ts">


const options = ref<any[]>([])
const query = ref("")
const modelValue = defineModel<any>({ default: () => ({}) }) //Esto es para que el componente pue1da ser usado con v-model


type Props = {
    thirdType?: string
    specialities?: string | number
}

const clickHandler = () => {
    retrieveFromApi()
}

const props = withDefaults(defineProps<Props>(), {
    thirdType: '',
    specialities: ''
})



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


watch([query, () => props.specialities],
    async ([newQuery,  newSpeciality],
        [oldQuery,oldSpeciality]) => {
        if (oldSpeciality !== newSpeciality) {
            modelValue.value = {} // Si la ciudad cambió entonces borramos el tercero que teníamos seleccionado
        }
        retrieveFromApi()
    }
)
</script>

