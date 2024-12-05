<template>
  <USelectMenu v-model="modelValue" option-attribute="username" :searchable="search">
  </USelectMenu>
</template>

<script setup lang="ts">
const modelValue = defineModel<any>({ default: () => ({}) });

const search = async (q: string) => {
  const response = await $fetch<any>("api/auth/users", {
    query: {
      search: q,
    },
  });

  // Agregar la opción "Sin usuario" al inicio de la lista de resultados
  const noUserOption = { id: null, username: "Sin usuario" };

  // Devolver la opción "Sin usuario" seguida de los usuarios encontrados
  return [noUserOption, ...response.results];
};
</script>

<style scoped>
</style>
