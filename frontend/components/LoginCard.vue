<template lang="pug">
div
    h2.font-bold.text-xl.mb-16.text-center Ingreso usuarios
    UInput.mb-4(size="xl" v-model="email" label="Email" type="email" placeholder="Email" :ui="ui.input")
    UInput.mb-4(size="xl" v-model="password" label="Password" type="password" placeholder="Password" :ui="ui.input")
    UButton(size="xl" @click="login" block :ui="ui.button") INGRESAR
</template>

<script setup lang="ts">

const ui = {
    input: {
        rounded: 'rounded-full',
    },
    button: {
        rounded: 'rounded-full',
    }
}

</script>

<style scoped>

</style>