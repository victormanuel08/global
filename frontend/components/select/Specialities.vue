<template>
    <USelectMenu v-model="modelValue" option-attribute="description" :searchable="search" :placeholder = "'Especialidad'">
    </USelectMenu>
</template>

<script setup lang="ts">
const modelValue = defineModel<any>({default: () => ({})})
const search = async (q: string) => {
    const response = await $fetch<any>("api/specialities", {
        query: {
            search: q
        }
    })
    return response.results
}
</script>

<style scoped>

</style>



