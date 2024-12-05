<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Sistemas de Revisión</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>

      <!-- Mensaje cuando no hay datos -->
      <div class="flex justify-center items-center">
        <h3 v-if="systemsreviews.length === 0">No hay Sistemas de Revisión</h3>
      </div>

      <!-- Tabla de datos -->
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Código</th>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <!-- Filas existentes -->
            <tr v-for="(systemsreview, index) in systemsreviews" :key="systemsreview.id">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="systemsreview.code" 
                    @blur="saveItem(index, 'code', systemsreview.code)" 
                    class="border rounded p-1 w-14" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="systemsreview.name" 
                    @blur="saveItem(index, 'name', systemsreview.name)" 
                    class="border rounded p-1" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteSystemsReview(systemsreview.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>

            <!-- Nueva fila para agregar -->
            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="newSystemsReviewCode" 
                    placeholder="Código" 
                    class="border rounded p-1 w-14" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput 
                    v-model="newSystemsReviewName" 
                    placeholder="Nombre" 
                    class="border rounded p-1" 
                  />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createSystemsReview" :class="ui.span">💾</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </UCard>
  </div>
</template>

<script setup lang="ts">
// Variables reactivas
const newSystemsReviewName = ref('');
const newSystemsReviewCode = ref('');
const toast = useToast(); // Para notificaciones

// Hook para la paginación
const { data: systemsreviews, pagination, search, pending } = usePaginatedFetch<any>('/api/systems_review/');

// Función para obtener sistemas de revisión
const fetchSystemsReviews = async () => {
  await usePaginatedFetch<any>('/api/systems_review/');
};

// Función para eliminar un sistema de revisión
const deleteSystemsReview = async (id: number) => {
  if (confirm('¿Estás seguro de eliminar este Sistema de Revisión?')) {
    try {
      await $fetch(`api/systems_review/${id}/`, { method: 'DELETE' });
      toast.add({ title: `Sistema de Revisión con ID ${id} eliminado.` });
      fetchSystemsReviews();
    } catch (error) {
      console.error('Error al eliminar:', error);
      toast.add({ title: `Error al eliminar el Sistema de Revisión con ID ${id}.` });
    }
  }
};

// Función para guardar cambios en un sistema de revisión
const saveItem = async (index: number, field: string, value: string) => {
  const systemsreview = systemsreviews.value[index];
  systemsreview[field] = value;
  try {
    await $fetch(`api/systems_review/${systemsreview.id}`, {
      method: 'PATCH',
      body: JSON.stringify({ [field]: value }),
    });
    toast.add({ title: `Sistema de Revisión actualizado: ${field}` });
    fetchSystemsReviews();
  } catch (error) {
    console.error('Error al actualizar:', error);
    toast.add({ title: `Error al actualizar ${field}.` });
  }
};

// Función para crear un nuevo sistema de revisión
const createSystemsReview = async () => {
  if (confirm('¿Estás seguro de crear este Sistema de Revisión?')) {
    try {
      await $fetch('api/systems_review/', {
        method: 'POST',
        body: {
          code: newSystemsReviewCode.value,
          name: newSystemsReviewName.value,
        },
      });
      toast.add({ title: `Sistema de Revisión creado: ${newSystemsReviewName.value}` });
      fetchSystemsReviews();
      newSystemsReviewCode.value = '';
      newSystemsReviewName.value = '';
    } catch (error) {
      console.error('Error al crear:', error);
      toast.add({ title: 'Error al crear el Sistema de Revisión.' });
    }
  }
};

// Inicialización al montar el componente
onMounted(() => {
  fetchSystemsReviews();
});

// Estilos
const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  span: 'cursor-pointer',
};
</script>

<style scoped>
.table-auto {
  width: 100%;
  border-collapse: collapse;
}
.permission-table th,
.permission-table td {
  text-align: center;
}
</style>
