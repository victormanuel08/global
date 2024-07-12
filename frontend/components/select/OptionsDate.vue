<template>
    <USelectMenu 
        v-model="modelValue" 
        option-attribute="concat" 
        :options="options" 
        :searchable="true"
        v-model:query="query" 
        :clearSearchOnClose="true" 
        :placeholder="'Fecha'"
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
        //date__gtn: formatDateYYYYMMDD(currentDate.toString()), 
    };

    const response = await $fetch<any>("api/availabilities?page_size=1000", {
        query: queryParams,
    });

    options.value = response.results
        .filter(option => new Date(option.date) > currentDate)
        .map(option => ({
            ...option,
            concat: `${option.date} ${option.day} ( ${option.start_time} - ${option.end_time} )` ,
    }));
};



watch([ props.date, () => props.third],
    async ([ newDate, newThird ,oldDate,oldThird]) => {
        if (oldThird !== newThird || oldDate !== newDate) {
            modelValue.value = {} 
        }
    }
)

</script>

<style scoped></style>

