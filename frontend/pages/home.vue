<template>
    <div>
        <h1>Mi Ubicación</h1>

    </div>
</template>

<script setup>
import useGeoLocation from '~/composables/geoLocation';
import { useUserLogin } from '~/stores/thirds';

const { userLogin } = useUserLogin();
console.log("UserLOGINHOME", userLogin.value)

</script>