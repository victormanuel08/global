<template>
<USelectMenu v-model="modelValue" option-attribute="formatted_address" :searchable="search">
</USelectMenu>
</template>

<script setup lang="ts">

const modelValue = defineModel<any>({default: () => ({})})


type Props = {
  coordinates?: string
}


const props = withDefaults(defineProps<Props>(), {
    coordinates: ''
})

const search = async (q: string) => {
    const response = await $fetch<any>(`/api/geocode/?coordinates=${props.coordinates}`, {
        query: {
            search: q
        }
    })
  
    //console.log('responseADRES', response)
    return response
}
</script>

<style scoped>

</style>