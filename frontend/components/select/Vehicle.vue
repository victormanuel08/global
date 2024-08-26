<template>
<USelectMenu v-model="modelValue" option-attribute="plate" :searchable="search">
</USelectMenu>
</template>

<script setup lang="ts">

const modelValue = defineModel<any>({default: () => ({})})

const search = async (q: string) => {
    const response = await $fetch<any>("api/vehicles", {
        query: {
            search: q
        }
    })

    return response.results
}
</script>

<style scoped>

</style>