<template>
    <USelectMenu v-model="modelValue" option-attribute="concat" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true" @click="clickHandler" :placeholder="'Accidentes'"
        @change="loader">
    </USelectMenu>
</template>
<script setup lang="ts">

const options = ref<any[]>([])
const query = ref("")
const modelValue = defineModel<any>({ default: () => ({}) })
const specialities = ref<any[]>([])
const specialitiesSet = new Set();
const services = ref<any[]>([])

type Props = {
    third?: string | number
}

const props = withDefaults(defineProps<Props>(), {
    third: '',
})

const clickHandler = () => {
    options.value = []
    retrieveFromApi()
}

const retrieveFromApi = async () => {
    try {
        const response = await $fetch<any>(`api/thirds/${props.third}`);
        const policesIds = response.policys;
        for (const policeId of policesIds) {
            const police = await $fetch<any>(`api/polices/${policeId}`);
            const tp = await getCHOICE(police.type_police, 'TYPE_POLICE_CHOICES')
            police.concat = `${tp.name} - ${police.description} - ${police.date_start} - ${police.date_end}`;
            options.value.push(police);
        }
    } catch (error) {
        console.error("Error al obtener los datos de la API:", error);
    }
};

const loader = async () => {
    await modelValue.value
    const querySet = ref({})
    if (modelValue.value.payment_model === 'FF') {
        
    }
    if (modelValue.value.payment_model === 'EV' && modelValue.value.type_police === 'SE') {
        querySet.value = {
            amount_soat__gt: 0.1
        }
    }
    if (modelValue.value.payment_model === 'EV' && modelValue.value.type_police === 'PA') {
        querySet.value = {
            amount_particular__gt: 0.1
        }
    }
    const response = await $fetch<any>('api/services/', {
            method: 'GET',
            params: querySet.value
        });
        modelValue.value.services = response.results        
        specialitiesSet.clear()
        for (const service of modelValue.value.services) {
            specialitiesSet.add(service.speciality)
        }
        specialities.value = Array.from(specialitiesSet)
        modelValue.value.specialities = []
        for (const speciality of specialities.value) {
            const querySet = {
                id: speciality
            }    
            const response = await $fetch<any>('api/specialities/', {
                method: 'GET',
                params: querySet
            });
            modelValue.value.specialities = response.results
        }
        console.log('modelValue', modelValue.value)
    }
      


watch(
    [query, () => props.third],
    async ([newQuery, newThird], [oldQuery, oldThird]) => {
        if (oldThird !== newThird) {
            modelValue.value = {};
        }
        retrieveFromApi();
    }
);
</script>