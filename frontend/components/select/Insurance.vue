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
const toast = useToast()
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

const isFee = ref(false)
const uniqueSpecialities = [] as any;

const loader = async () => {
    await modelValue.value;
    const querySet = ref({});
    // isFee toma el valor de true si el tipo de póliza es diferente de "PA" o "SE"
    isFee.value = !['PA', 'SE'].includes(modelValue.value.type_police);

    switch (modelValue.value.type_police) {
        case 'SE':
            querySet.value = { amount_soat__gt: 0.1 };
            isFee.value = false;
            break;
        case 'PA':
            querySet.value = { amount_particular__gt: 0.1 };
            isFee.value = false;
            break;
    }

    modelValue.value.services = [];
    modelValue.value.specialities = [];
    uniqueSpecialities.length = 0;

    if (!isFee.value) {
        const response = await $fetch<any>('api/services/', {
            method: 'GET',
            params: querySet.value
        });
        //console.log('responseIS FALSE', response);
        for (const fee of response.results) {
            modelValue.value.services.push(fee);
            const especialidadExistente = uniqueSpecialities.find(
                (especialidad: { id: any; }) => especialidad.id === fee.speciality_full.id
            );

            if (!especialidadExistente) {
                uniqueSpecialities.push(fee.speciality_full);
            }
        }
    } else {
        const feeResponse = await $fetch<any>(`/api/fees/?search&policy=${modelValue.value.id}`, {
            method: 'GET'
        });
        //console.log('feeResponseIS TRUEEEEE', feeResponse);
        for (const fee of feeResponse.results) {
            fee.service_full.amount = fee.amount;
            modelValue.value.services.push(fee.service_full);
            const especialidadExistente = uniqueSpecialities.find(
                (especialidad: { id: any; }) => especialidad.id === fee.service_full.speciality_full.id
            );

            if (!especialidadExistente) {
                uniqueSpecialities.push(fee.service_full.speciality_full);
            }
        }
    }

    modelValue.value.specialities = uniqueSpecialities;

    //console.log("dsdsdsdsds" + modelValue.value.description, modelValue.value);
};


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
