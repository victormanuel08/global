<template>
    <USelectMenu v-model="modelValue" option-attribute="description" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true"  @change="contractual"
        :placeholder="'Contratos'">
    </USelectMenu>
    <ModalContractual :fee="modelValue" d></ModalContractual>
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





   

const contractual = async() => {

    retrieveFromApi()

}

const retrieveFromApi = async () => {
    const queryParams = {
        search: query.value,
        third_entity: props.third?.id,
    }
    if (props.specialities) {
        queryParams.speciality = props.specialities?.id;
    }
    if (props.service) {
        queryParams.service = props.service?.id;
    }
    try {
        const response = await $fetch<any>("api/fees", {
            query: queryParams
        })
        options.value = [
            {               
                description: "Contrato SOAT",
            }, 
      

            ...response.results.map((scheduled: any) => ({
                ...scheduled,           
            })),
        ];


    } catch (error) {
        console.error("Error al obtener los datos de la API:", error);
    }

}


watch(
    [query, () => props.specialities],
    async ([newQuery, newSpeciality], [oldQuery, oldSpeciality]) => {
        if (oldSpeciality !== newSpeciality) {
            modelValue.value = {};
        }
        retrieveFromApi();
    }
);


</script>
