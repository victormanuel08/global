<template>
    <USelectMenu 
        v-model="modelValue" 
        option-attribute="description" 
        :options="options" 
        :searchable="true" 
        v-model:query="query"
        :clearSearchOnClose="true" 
        @click="clickHandler"
        @change="showContractual = true"
        :placeholder="'Servicios'"
        >
    </USelectMenu>
    <ModalContractual :fee="modelValue" v-model="showContractual"></ModalContractual>
</template>
<script setup lang="ts">

const showContractual = ref(false);



const options = ref<any[]>([])
const typeThird = ref('asasasa')
const query = ref("")
const modelValue = defineModel<any>({ default: () => ({}) }) //Esto es para que el componente pue1da ser usado con v-model


type Props = {
    third?: string
    specialities?: string | number
    service?: string | number
    policy?: string
}

const props = withDefaults(defineProps<Props>(), {
    third: '',
    specialities: '',
    service: ''
})

const clickHandler = () => {
    
    retrieveFromApi()
}

const retrieveFromApi = async () => {
    const value_description = ref('')
    const queryParams = {
        search: query.value,
        third_entity: props.third?.id,
    }

    if (props.specialities) {
        queryParams.speciality = props.specialities?.id;
    }

    if (props.service) {
        queryParams.service = props.service?.id;
        value_description.value = props.policy_full?.description
    }


    const response = await $fetch<any>("api/fees", {
        query: queryParams
    })

    if (props.specialities) {  
        value_description.value = props.service_full?.description
        console.log(value_description.value)
    }

    if (props.service) {
        queryParams.service = props.service?.id;
        value_description.value = props.policy_full?.description
    }

    options.value = response.results
    options.value.value_description = response.description
    console.log(options.value.value_description)

   
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
