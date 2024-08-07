<template>
<USelectMenu v-model="modelValue" option-attribute="username" :searchable="search">
</USelectMenu>
</template>

<script setup lang="ts">

const modelValue = defineModel<any>({default: () => ({})})

const search = async (q: string) => {
    const response = await $fetch<any>("api/auth/users", {
        query: {
            search: q
        }
    })

    return response.results
}
</script>

<style scoped>

</style>