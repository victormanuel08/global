<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Vehiculos</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="vehicles.length === 0">No hay Vehiculos</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Datos Vehiculo</th>
              <th :class="ui.th">Tipo</th>
              <th :class="ui.th">Conductor/Empresa</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(vehicle, index) in vehicles" :key="index">
              <td :class="ui.td">
                <div class="grid grid-row justify-center">
                  <div>
                    <UInput v-model="vehicle.plate" @blur="saveItem(index, 'plate', vehicle.name)"
                      class="border rounded p-1 w-32" placeholder="Placa" />
                  </div>
                  <div>
                    <UInput v-model="vehicle.brand" @blur="saveItem(index, 'brand', vehicle.brand)"
                      class="border rounded p-1 w-32" placeholder="Marca / Movil" />
                  </div>
                </div>
              </td>
              <td :enter-class="ui.td">
                <div class="grid grid-row justify-center">
                  <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" v-model="vehicle.vehicle_type"
                    @change="saveItem(vehicle.id, 'vehicle_type', vehicle.vehicle_type)"
                    class="border rounded p-1 w-32" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-row justify-center">
                  <div>
                    <SelectThird :third-type="'P'" v-model="vehicle.third_driver_full" :placeholder="'Conductor'"
                      @change="saveItem(vehicle.id, 'third_driver', vehicle.third_driver_full.id)"
                      class="border rounded p-1 w-72">
                    </SelectThird>
                  </div>
                  <div>
                    <SelectThird :third-type="'E'" v-model="vehicle.third_entity_full" :placeholder="'Empresar'"
                      @change="saveItem(vehicle.id, 'third_entity', vehicle.third_entity_full.id)"
                      class="border rounded p-1 w-72">
                    </SelectThird>
                  </div>
                </div>
              </td>
              <td :class="ui.td">
                <div class="grid grid-row justify-center">

                  <span @click="deleteVehicle(vehicle.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="grid grid-row justify-center">
                  <div>
                    <UInput v-model="newVehiclePlate" placeholder="Placa" class="border rounded p-1" />
                  </div>
                  <div>
                    <UInput v-model="newVehicleBrand" placeholder="Modelo /  Movil" class="border rounded p-1" />
                  </div>
                </div>
              </td>

              <td :class="ui.td">
                <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" v-model="newVehicleType" />
              </td>
              <td :class="ui.td">
                <div class="grid grid-row justify-center">
                  <div>
                    <SelectThird :third-type="'P'" v-model="newVehicleThird" :placeholder="'Conductor'"
                      class="border rounded p-1" />

                  </div>
                  <div>
                    <SelectThird :third-type="'E'" v-model="newVehicleEntity" :placeholder="'Empresa'"
                      class="border rounded p-1" />

                  </div>
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

//const cities = ref([] as any[])
const newVehiclePlate = ref('')
const newVehicleBrand = ref('')
const newVehicleType = ref('')
const newVehicleThird = ref({})
const newVehicleEntity = ref({})
//const search = ref('')



const {
  data: vehicles,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/vehicles/");

const fetchVehicles = async () => {
  const {
    data: cities,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/vehicles/");

  console.log('fetchvehicles', vehicles.value)

}

const deleteVehicle = async (id: number) => {
  autorized.value = await validatePermissions('vehicles', 'delete');
  if (!autorized.value) {
    fetchVehicles()
    return
  }l
  const message = confirm('¿Estás seguro de eliminar este Vehiculo?')
  if (message) {
    const response = await $fetch(`api/vehicles/${id}/`, {
      method: 'DELETE'
    })
    fetchVehicles()
  }
}

const autorized = ref(false)

const saveItem = async (index: number, field: string, value: string) => {
  autorized.value = await validatePermissions('vehicles', 'change');
  if (!autorized){
    fetchVehicles();
    return
  }
  const vehicle = vehicles.value[index];
  vehicle[field] = value;
  const response = await $fetch(`api/vehicles/${vehicle.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchVehicles();
};

const createVehicle = async () => {
  autorized.value = await validatePermissions('vehicles', 'add');
  if (!autorized) {
    fetchVehicles()
    return
  }
  const message = confirm('¿Estás seguro de crear este Vehiculo?')

  if (!message) {
    newVehiclePlate.value = ''
    newVehicleBrand.value = ''
    newVehicleType.value = ''
    newVehicleThird.value = ''
    newVehicleEntity.value = ''
    fetchVehicles()
    return
  }
  

  const response = await $fetch('api/vehicles/', {
    method: 'POST',
    body: {
      plate: newVehiclePlate.value,
      brand: newVehicleBrand.value,
      vehicle_type: newVehicleType.value.id,
      third_driver: newVehicleThird.value.id,
      third_entity: newVehicleEntity.value.id
    }
  })
  fetchVehicles()
  newVehiclePlate.value = ''
  newVehicleBrand.value = ''
  newVehicleType.value = ''
  newVehicleThird.value = ''
  newVehicleEntity.value = ''

}

onMounted(() => {
  fetchVehicles()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
