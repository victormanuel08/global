<template>
    <USelectMenu v-model="modelValue" option-attribute="placamovil" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true" @click="clickHandler"
        :placeholder="props.vehicleType === 'AM' ? 'Ambulancia' : 'Vehiculo'">
    </USelectMenu>
</template>

<script setup lang="ts">

const modelValue = defineModel<any>({ default: () => ({}) })
const options = ref<any[]>([])
const query = ref("")

type Props = {
    vehicleType?: string
}

const props = withDefaults(defineProps<Props>(), {
    vehicleType: '',
})

const clickHandler = () => {
    retrieveFromApi()
}


const retrieveFromApi = async () => {
    const queryParams = {
        search: query.value,
    }

    if (props.vehicleType) {
        queryParams.vehicle_type = props.vehicleType;
    }

    const response = await $fetch<any>("api/vehicles", {
        query: queryParams
    })
    options.value = response.results
}


</script>

<style scoped></style>