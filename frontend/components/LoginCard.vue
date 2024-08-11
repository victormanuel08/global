<template>
<div>
    <h2 class="font-bold text-xl mb-16 text-center">Ingreso usuarios</h2>
    <UInput class="mb-4" size="xl" v-model="loginData.username" label="Email" type="email" placeholder="Email" :ui="ui.input"></UInput>
    <UInput class="mb-4" size="xl" v-model="loginData.password" label="Password" type="password" placeholder="Password" :ui="ui.input"></UInput>
    <UButton class="mb-4" size="xl"  block :ui="ui.button" @click="doLogin" >INGRESAR</UButton>
</div>

</template>

<script setup lang="ts">

import { useRouter } from 'vue-router';
import { jwtDecode } from "jwt-decode";
import { useUserLogin } from '~/stores/thirds';

const { userLogin } = useUserLogin();


const router = useRouter();

const ui = {
    input: {
        rounded: 'rounded-full',
    },
    button: {
        rounded: 'rounded-full',
    }
}

// Esto lo traje de Dipro, donde está todo aparentemente Ok con la autenticación
const authState = useAuthState()
const toast = useToast()
const loginData = ref({
    username: '',
    password: ''
})
const user = ref<any>()
const haveUser = computed(() => user.value && "id" in user.value)
const loading = ref(false)

onMounted(async () => {
    if (authState.value) {
        console.log("Ya hay un token guardado")
        try {
            const decoded = jwtDecode(authState.value);
            const user_id = decoded.user_id
            user.value = await $fetch(`/api/auth/users/${user_id}/`)
            console.log("User", user)
        } catch (error) {
            toast.add({ title: "Error en la autenticación" })
            console.log("Error en la autenticación")
            console.log(error)
            loading.value = false
        }
    }
})

const doLogout = () => {
    authState.value = null
    user.value = null
    useRouter().push('/')
}

const doLogin = async () => {
    loading.value = true
    try {
        const response = await $fetch('/api/auth/token/', {
            method: 'POST',
            body: loginData.value
        }) as any
        authState.value = response.access
        const decoded = jwtDecode(response.access);
        const user_id = decoded.user_id
        user.value = await $fetch(`/api/auth/users/${user_id}/`)
        userLogin.value = user.value
        sessionStorage.setItem('userLoginS', JSON.stringify(user.value))
        console.log("Raw response", response, "Decoded jwt", decoded, "User", user)
        toast.add({ title: "Autenticación Exitosa" })
        router.push('/home')
        console.log("UserLOGIN", userLogin.value)

        loading.value = false
    } catch (error) {
        toast.add({ title: "Error en la autenticación" })
        console.log(error)
        loading.value = false
    }
}

</script>

<style scoped>

</style>