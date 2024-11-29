<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <h1>Perfil</h1>
                <p>Esta es la página de psswswswswserfil {{ user }}</p>
            </div>
        </div>

        <!-- Sección User -->


        <!-- Sección Tercero -->

    </div>
</template>

<script lang="ts">

const authUserStorage = useAuthUserStorage();
const authTokensStorage = useAuthTokensStorage();
const user = computed(() => authUserStorage.value);
const user2 = authUserStorage.value;

console.log(user2);
console.log(user);

onMounted(() => {
    //console.log('mounted', user);
});


</script>
