<template>
    <USelectMenu v-model="internalValue" option-attribute="concat" multiple :searchable="search" trailing by="id" @change="handleChange">
    </USelectMenu>
</template>

<script setup lang="ts">
const props = defineProps({
    modelValue: Array,
    third: [String, Number]
});
const internalValue = ref(props.modelValue);
const allPolicys = ref([]); // Para almacenar todos los policys, incluidos los de tipo "PA" y "SE"

watch(() => props.modelValue, (newValue) => {
    internalValue.value = newValue;
});

const emit = defineEmits(['update:modelValue']);
const handleChange = (value: any) => {
    emit('update:modelValue', value);
};

const search = async (q: string) => {
    const fetchResponse = await $fetch<any>("api/polices", {
        query: { 
            search: q, 
            type_police__ne: ["PA", "SE"]
        }
    });
    const results = fetchResponse.results.map((item: any) => {
        return {
            ...item,
            concat: `${item.description} - ${item.third_entity_full.namenit} `
        };
    });

    return results;
};

// Cargar los policys asociados al tercero al montar el componente
onMounted(async () => {
    if (props.third) {
        const response = await $fetch<any>(`api/thirds/${props.third}`);
        allPolicys.value = response.policys; // Almacenar todos los policys
        internalValue.value = response.policys.filter((policy: any) => !["PA", "SE"].includes(policy.type_police)); // Filtrar para mostrar
        emit('update:modelValue', internalValue.value);
    }
});
</script>

<style scoped>
/* Aquí puedes agregar estilos personalizados si es necesario */
</style>
