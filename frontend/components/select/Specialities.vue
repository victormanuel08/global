<template>
    <USelectMenu v-model="modelValue" option-attribute="description" :searchable="search" :placeholder="'Especialidad'">
    </USelectMenu>
</template>

<script setup lang="ts">


type Props = {
    specialities?: string | number
}


const props = withDefaults(defineProps<Props>(), {
    specialities: '',
})

const modelValue = defineModel<any>({ default: () => ({}) })

const search = async (q: string) => {
    if (props.specialities) {
        return props.specialities
    } else {
        const response = await $fetch<any>("api/specialities", {
            query: {
                search: q
            }
        })
        return response.results
    }
   

}
</script>

<style scoped></style>
