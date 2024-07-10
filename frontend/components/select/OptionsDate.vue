<template>
    <USelectMenu 
        v-model="modelValue" 
        option-attribute="concat" 
        :options="options" 
        :searchable="true"
        v-model:query="query" 
        :clearSearchOnClose="true" 
        @click="clickHandler">
    </USelectMenu>

</template>

<script setup lang="ts">

const options = ref<any[]>([])
const query = ref("")
const modelValue = defineModel<any>({ default: () => ({}) }) //Esto es para que el componente pue1da ser usado con v-model

type Props = {
    date?: any
    third?: any 
}

const props = withDefaults(defineProps<Props>(), {
    date: '',
    third: ''
})


const clickHandler = () => {
    retrieveFromApi()
}

const retrieveFromApi = async () => {
    // Obtén la fecha actual
    const currentDate = new Date();

    // Ajusta la fecha de búsqueda para que sea superior al día actual
    const queryParams = {
        search: query.value,
        third: props.third.id,
        date: currentDate.toISOString(), // Convierte la fecha a formato ISO
    };

    const response = await $fetch<any>("api/availabilities", {
        query: queryParams,
    });

    options.value = response.results.map(option => ({
        ...option,
        concat: `${option.date} ${option.day}`,
    }));
};



watch([ props.date, () => props.third],
    async ([ newDate, newThird],
        [oldDate,oldThird]) => {
        if (oldThird !== newThird || oldDate !== newDate) {
            modelValue.value = {} 
        }
    }
)

</script>

<style scoped></style>

