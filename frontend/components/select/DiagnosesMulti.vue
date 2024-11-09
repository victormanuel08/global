<template>
    <USelectMenu v-model="internalValue" option-attribute="name" multiple :searchable="search" trailing by="id">
    </USelectMenu>
</template>

<script setup lang="ts">
const props = defineProps({
    modelValue: Array
});
const internalValue = ref(props.modelValue);

watch(() => props.modelValue, (newValue) => {
    internalValue.value = newValue;
});

const emit = defineEmits(['update:modelValue']);
const handleChange = (value: any) => {
    emit('update:modelValue', value);
};

const search = async (q: string) => {
    const response = await $fetch<any>("api/diagnoses", {
        query: {
            search: q
        }
    });
    return response.results;
};
</script>

<style scoped>
/* Aquí puedes agregar estilos personalizados si es necesario */
</style>
