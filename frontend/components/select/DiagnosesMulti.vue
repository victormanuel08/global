<template>
    <USelectMenu v-model="modelValue" option-attribute="name" multiple :searchable="search" trailing by="id">
       
    </USelectMenu>
</template>

<script setup lang="ts">
const modelValue = defineModel<any>({default: () => ({})})
const search = async (q: string) => {
    const response = await $fetch<any>("api/diagnoses", {
        query: {
            search: q
        }
    })
    return response.results
}
</script>

<style scoped>

</style>



