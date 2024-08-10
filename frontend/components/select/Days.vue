<template>
    <USelectMenu v-model="modelValue" option-attribute="name" :options="options">
    </USelectMenu>
</template>

<script setup lang="ts">
const modelValue = defineModel<any>({ default: () => ({}) })
const options = ref<any[]>([])
type Props = {
    start?: any
    end?: any 
}
const props = withDefaults(defineProps<Props>(), {
    start: '',
    end: ''
})

const loadOptions = () => {
    options.value = listDaysOptions(props.start, props.end)
}
loadOptions()

watch([ props.start, () => props.end],
    async ([ newStart, newEnd],
        [oldStart,oldEnd]) => {
        if (oldEnd !== newEnd || oldStart !== newStart) {
            modelValue.value = {} 
        }
        loadOptions()
    }
)
</script>

<style scoped></style>