<template>
    <USelectMenu v-model="modelValue" option-attribute="description" :searchable="search" :placeholder="'Servicio'" :options="options" @click="loadOptions">
    </USelectMenu>
</template>
<script setup lang="ts">
const options = ref<any[]>([])

type Props = {
    specialities?: string | number | object | any
    services?: string | number | object | any
}
const props = withDefaults(defineProps<Props>(), {
    specialities: '',
    services: ''
})
const modelValue = defineModel<any>({ default: () => ({}) })
const filteredServices =  [];
filteredServices.length = 0;
 onMounted(() => {
    loadOptions();  

})

const loadOptions = async () => {
    filteredServices.length = 0;
    console.log('LOAD OPTIONS',props);
    if (props.services) {
        for (const key in props.services) {
            if (Object.prototype.hasOwnProperty.call(props.services, key)) {
                if (props.services[key].speciality === props.specialities.id) {
                    filteredServices.push(props.services[key]);
                }
            }
        }
        options.value = filteredServices;
    } else {
        const response = await $fetch<any>("api/services");
        options.value = response.results;
    }
}

const search = async (q: string) => {
   
    filteredServices.length = 0;
    console.log('LOAD OPTIONSquery',props);
    if (props.services) {    
        for (const key in props.services) {
            console.log('KEY',key);
            if (Object.prototype.hasOwnProperty.call(props.services, key)) {
                if (props.services[key].speciality === props.specialities.id) {
                    filteredServices.push(props.services[key]);
                }
            }
        }       
        return filteredServices;
    } else {
        console.log('NO VENGO DE PROPS');
        const response = await $fetch<any>("api/services", {
            query: {
                search: q
            }
        });
        return response.results;
    }
}

watch(    
    [() => props.specialities, () => props.services],
    async ([newSpeciality, newServices], [oldSpeciality, oldServices]) => {
        if (oldSpeciality !== newSpeciality || oldServices !== newServices) {
            modelValue.value = {};
            filteredServices.length = 0;
        }
    }    
)

</script>

<style scoped></style>