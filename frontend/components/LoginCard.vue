<template>
<div>
    <h2 class="font-bold text-xl mb-16 text-center">Ingreso usuarios</h2>
    <UInput class="mb-4" size="xl" v-model="email" label="Email" type="email" placeholder="Email" :ui="ui.input"></UInput>
    <UInput class="mb-4" size="xl" v-model="password" label="Password" type="password" placeholder="Password" :ui="ui.input"></UInput>
    <UButton class="mb-4" size="xl"  block :ui="ui.button" @click="redirectToMenu" >INGRESAR</UButton>
</div>

</template>

<script setup lang="ts">

import { useRouter } from 'vue-router';

const router = useRouter();

const redirectToMenu = () => {  

};

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