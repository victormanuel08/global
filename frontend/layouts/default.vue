<template>
    <div class="flex gap-3 bg-gray-100 border " style="height: calc(100vh - 48px) !important">
        <!-- El cuerpo ocupa el 100% de la altura de la pantalla menos el alto del header -->
        <div class="w-48 bg-gray-100 ">
            <div class="py-16 text-center ">
                <img src="@/assets/img/GLOBALIPS.PNG" alt="GLOBAL"
                    class="object-contain w-1/1 md:w-1/1 lg:w-1/1 xl:w-1/1">
            </div>
        </div>
        <div class="flex-grow bg-white border overflow-auto rounded-lg">
            <div class="p-2 bg-gray-100 rounded-full shadow m-4 ">
                Global Safe
            </div>
            <slot></slot>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped></style>