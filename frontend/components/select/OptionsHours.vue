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
const modelValue = defineModel<any>({ default: () => ({}) }) 

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
    const currentDate = new Date();
    
    const queryParams = {
        search: query.value,
        type: props.third.id,
        date__gte: currentDate.toISOString(),
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

