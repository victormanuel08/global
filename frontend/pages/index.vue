<template lang="pug">
.flex.flex-col.justify-center.h-full
    div
        UCard.mx-auto.max-w-3xl.shadow-xl.py-16.px-4
            .grid.grid-cols-2.gap-8
                div
                    .py-16.text-center.text-gray-400 Global safe logo
                div
                    LoginCard
</template>

<script setup lang="ts">
definePageMeta({
    layout: 'public',
})
</script>

<style scoped>

</style>