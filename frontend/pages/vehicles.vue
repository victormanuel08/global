<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Vehículos</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" 
                         :page-count="pagination.pageSize" 
                         :total="pagination.resultsCount" />
          </div>
        </div>
      </template>

      <div v-if="vehicles.length === 0" class="flex justify-center items-center">
        <h3>No hay Vehículos</h3>
      </div>

      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Datos Vehículo</th>
              <th :class="ui.th">Tipo</th>
              <th :class="ui.th">Conductor/Empresa</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(vehicle, index) in vehicles" :key="vehicle.id">
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <UInput v-model="vehicle.plate" 
                          @blur="saveItem(index, 'plate', vehicle.plate)" 
                          class="border rounded p-1 w-32" 
                          placeholder="Placa" />
                  <UInput v-model="vehicle.brand" 
                          @blur="saveItem(index, 'brand', vehicle.brand)" 
                          class="border rounded p-1 w-32" 
                          placeholder="Marca / Móvil" />
                </div>
              </td>
              <td :class="ui.td">
                <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" 
                              v-model="vehicle.vehicle_type" 
                              @change="saveItem(vehicle.id, 'vehicle_type', vehicle.vehicle_type?.id)" 
                              class="border rounded p-1 w-32" />
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <SelectThird :third-type="'P'" 
                               v-model="vehicle.third_driver_full" 
                               :placeholder="'Conductor'" 
                               @change="saveItem(vehicle.id, 'third_driver', vehicle.third_driver_full?.id)" 
                               class="border rounded p-1 w-72" />
                  <SelectThird :third-type="'E'" 
                               v-model="vehicle.third_entity_full" 
                               :placeholder="'Empresa'" 
                               @change="saveItem(vehicle.id, 'third_entity', vehicle.third_entity_full?.id)" 
                               class="border rounded p-1 w-72" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <span @click="deleteVehicle(vehicle.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>
            <tr>
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <UInput v-model="newVehiclePlate" placeholder="Placa" class="border rounded p-1" />
                  <UInput v-model="newVehicleBrand" placeholder="Modelo / Móvil" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" v-model="newVehicleType" />
              </td>
              <td :class="ui.td">
                <div class="grid grid-rows justify-center">
                  <SelectThird :third-type="'P'" 
                               v-model="newVehicleThird" 
                               :placeholder="'Conductor'" 
                               class="border rounded p-1" />
                  <SelectThird :third-type="'E'" 
                               v-model="newVehicleEntity" 
                               :placeholder="'Empresa'" 
                               class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createVehicle" :class="ui.span">💾</span>
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
// Interfaz para vehículos
interface Vehicle {
  id: number;
  plate: string;
  brand: string;
  vehicle_type: { id: number } | null;
  third_driver_full: { id: number } | null;
  third_entity_full: { id: number } | null;
}

const newVehiclePlate = ref('');
const newVehicleBrand = ref('');
const newVehicleType = ref<{ id: number } | null>(null);
const newVehicleThird = ref<{ id: number } | null>(null);
const newVehicleEntity = ref<{ id: number } | null>(null);
const autorized = ref(false);

const toast = useToast();

const { data: vehicles, pagination, search, refresh } = usePaginatedFetch<Vehicle[]>('/api/vehicles/');

const deleteVehicle = async (id: number) => {
  autorized.value = await validatePermissions('vehicles', 'delete');
  if (!autorized.value) {
    toast.add({ title: `No tienes permisos para eliminar vehículos.` });
    return;
  }
  if (confirm('¿Estás seguro de eliminar este Vehículo?')) {
    try {
      await $fetch(`api/vehicles/${id}/`, { method: 'DELETE' });
      refresh();
      toast.add({ title: `Vehículo eliminado correctamente.` });
    } catch (error) {
      toast.add({ title: `Error al eliminar el vehículo` }); //${error.message}
    }
  }
};

const saveItem = async (index: number, field: keyof Vehicle, value: any) => {
  autorized.value = await validatePermissions('vehicles', 'change');
  if (!autorized.value) {
    toast.add({ title: `No tienes permisos para modificar vehículos.` });
    return;
  }
  const vehicle = vehicles.value[index];
  vehicle[field] = value;
  try {
    await $fetch(`api/vehicles/${vehicle.id}`, {
      method: 'PATCH',
      body: JSON.stringify({ [field]: value }),
    });
    refresh();
    toast.add({ title: `Vehículo actualizado correctamente.` });
  } catch (error) {
    toast.add({ title: `Error al actualizar el vehículo` });
  }
};

const createVehicle = async () => {
  autorized.value = await validatePermissions('vehicles', 'add');
  if (!autorized.value) {
    toast.add({ title: `No tienes permisos para agregar vehículos.` });
    return;
  }
  if (confirm('¿Estás seguro de crear este Vehículo?')) {
    try {
      await $fetch('api/vehicles/', {
        method: 'POST',
        body: {
          plate: newVehiclePlate.value,
          brand: newVehicleBrand.value,
          vehicle_type: newVehicleType.value?.id,
          third_driver: newVehicleThird.value?.id,
          third_entity: newVehicleEntity.value?.id,
        },
      });
      refresh();
      resetNewVehicle();
      toast.add({ title: `Vehículo creado correctamente.` });
    } catch (error) {
      toast.add({ title: `Error al crear el vehículo` });
    }
  }
};

const resetNewVehicle = () => {
  newVehiclePlate.value = '';
  newVehicleBrand.value = '';
  newVehicleType.value = null;
  newVehicleThird.value = null;
  newVehicleEntity.value = null;
};

onMounted(() => refresh());

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
