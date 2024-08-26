<template>
<div class="flex flex-col justify-center h-full">
    <div>
        <div class="UCard mx-auto max-w-3xl shadow-xl py-16 px-4 forced-color-adjust-auto rounded-div" style="background-color: white">
            <div class="grid grid-cols-2 gap-8">
                <div class="py-16 text-center text-gray-400">
                    <img src="@/assets/img/GLOBALIPS.png" alt="RIVERA" class="object-contain w-1/1 md:w-1/1 lg:w-1/1 xl:w-1/1">
                </div>
                <LoginCard></LoginCard>
                <slot></slot>
            </div>
        </div>
    </div>
</div>
</template>



<script setup lang="ts">
import LoginCard from '~/components/LoginCard.vue';

definePageMeta({
    layout: 'public',
})



</script>

<style scoped>
.rounded-div {
    border-radius: 50px; /* Ajusta el valor según tus preferencias */
  }
</style>