<template>
<div class="mx-2">
    <h2 class="font-bold text-xl mb-16 text-center">Ingreso usuarios</h2>
    <UInput class="mb-4" size="xl" v-model="loginData.username" label="Email" type="email" placeholder="Username" :ui="ui.input"></UInput>
    <UInput class="mb-4" size="xl" v-model="loginData.password" label="Password" type="password" placeholder="Password" :ui="ui.input"></UInput>
    <UButton class="mb-4" size="xl"  block :ui="ui.button" @click="doLogin" >INGRESAR</UButton>
</div>

</template>

<script setup lang="ts">

import { useRouter } from 'vue-router';
import { jwtDecode } from "jwt-decode";

const CURRENT_USER_PATH = '/api/auth/users/me/'
const authUserStorage = useAuthUserStorage()


const router = useRouter();

const ui = {
    input: {
        rounded: 'rounded-full',
    },
    button: {
        rounded: 'rounded-full',
    }
}

const authTokensStorage = useAuthTokensStorage()
const toast = useToast()
const loginData = ref({
    username: '',
    password: ''
})
const loading = ref(false)



const doLogin = async () => {
    loading.value = true;
    try {
        // Realiza la solicitud para obtener los tokens
        const response = await $fetch('/api/auth/token/', {
            method: 'POST',
            body: loginData.value,
        }) as any;

        // Guarda el token de acceso
        authTokensStorage.accessToken.value = response.access;

        // Configura el encabezado de autorización para las solicitudes autenticadas
        const headers = {
            Authorization: `Bearer ${authTokensStorage.accessToken.value}`,
        };

        // Obtiene los datos del usuario actual usando el token
        authUserStorage.value = await $fetch(CURRENT_USER_PATH, { headers });

        // Notifica éxito y redirige
        toast.add({ title: "Autenticación Exitosa" });
        router.push('/home');
    } catch (error) {
        // Maneja errores
        toast.add({ title: "Error en la autenticación" });
        console.error(error);
    } finally {
        loading.value = false;
    }
};

</script>

<style scoped>

</style>