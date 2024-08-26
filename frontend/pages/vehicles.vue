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
              <th :class="ui.th">Placa</th>
              <th :class="ui.th">Marca</th>
              <th :class="ui.th">Tipo</th>
              <th :class="ui.th">Conductor</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(vehicle, index) in vehicles" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="vehicle.plate" @blur="saveItem(index, 'plate', vehicle.name)"
                    class="border rounded p-1 " />

                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="vehicle.brand" @blur="saveItem(index, 'brand', vehicle.brand)"
                    class="border rounded p-1" />

                </div>
              </td>
              <td :enter-class="ui.td">
                <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" v-model="vehicle.vehicle_type"
                  @change="saveItem(vehicle.id, 'vehicle_type', vehicle.vehicle_type)" />
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectThird :third-type="'P'" v-model="vehicle.third_driver_full" :placeholder="'Conductor'"
                    @change="saveItem(vehicle.id, 'third_driver', vehicle.third_driver_full.id)">
                  </SelectThird>
                </div>

              </td>

              <td :class="ui.td">
                <div class="flex items-center justify-center">
    
                  <span @click="deleteVehicle(vehicle.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newVehiclePlate" placeholder="Ciudad" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newVehicleBrand" placeholder="Ciudad" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" v-model="newVehicleType"
                 />
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectThird :third-type="'P'" v-model="newVehicleThird" :placeholder="'Conductor'"
                   >
                  </SelectThird>
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
  const message = confirm('¿Estás seguro de eliminar este Vehiculo?')
  if (message) {
    const response = await $fetch(`api/vehicles/${id}/`, {
      method: 'DELETE'
    })
    fetchVehicles()
  }
}



const saveItem = async (index: number, field: string, value: string) => {
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
  const message = confirm('¿Estás seguro de crear este Vehiculo?')

  if (!message) {
    newVehiclePlate.value = ''
    newVehicleBrand.value = ''
    newVehicleType.value = ''
    newVehicleThird.value = ''
    fetchVehicles()
    return
  }

  const response = await $fetch('api/vehicles/', {
    method: 'POST',
    body: {
      plate: newVehiclePlate.value,
      brand: newVehicleBrand.value,
      vehicle_type: newVehicleType.value.id,
      third_driver: newVehicleThird.value.id
    }
  })
  fetchVehicles()
  newVehiclePlate.value = ''
  newVehicleBrand.value = ''
  newVehicleType.value = ''
  newVehicleThird.value = ''

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
