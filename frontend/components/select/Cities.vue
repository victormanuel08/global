<template>
<USelectMenu v-model="modelValue" option-attribute="name" :searchable="search">
</USelectMenu>
</template>

<script setup lang="ts">

const modelValue = defineModel<any>({default: () => ({})})

const search = async (q: string) => {
    const response = await $fetch<any>("api/cities", {
        query: {
            search: q
        }
    })

    return response.results
}
</script>

<style scoped>

</style>