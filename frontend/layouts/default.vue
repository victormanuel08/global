<template>
    <div class="flex gap-3 bg-gray-100 border" style="height: calc(100vh - 48px) !important">
        <!-- Barra lateral -->
        <div class="w-48 bg-gray-100 hidden md:block">
            <div class="py-16 text-center">
                <img src="@/assets/img/GLOBALIPS.PNG" alt="GLOBAL" class="object-contain w-full md:w-1/1 lg:w-1/1">
            </div>
            <div class="py-16 text-center">
                <UDropdown :items="dropdownCreateItems" :popper="{ placement: 'bottom-start' }">
                    <UButton color="white" label="Acciones" trailing-icon="i-heroicons-chevron-down-20-solid" />
                </UDropdown>
            </div>
        </div>

        <!-- Contenido principal -->
        <div class="flex-grow bg-white border overflow-auto rounded-lg">
            <!-- Menú a la derecha (visible solo en pantallas grandes) -->
            <div class="p-2 bg-gray-100 rounded-full shadow m-4 text-right hidden md:block">
               imagen pc
            </div>
            <div class="p-2 bg-gray-100 rounded-full shadow m-4 text-left block md:hidden">
               imagen cel
            </div>

            
            <div class="p-2 bg-gray-100 rounded-full shadow m-4 text-right block md:hidden">
                
                <UDropdown :items="dropdownCreateItems" :popper="{ placement: 'bottom-end' }">
                    <UButton color="white" label="Acciones" trailing-icon="i-heroicons-chevron-down-20-solid" />
                </UDropdown>
            </div>

            <slot></slot>
        </div>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped>
/* Estilos específicos para este componente */
</style>
