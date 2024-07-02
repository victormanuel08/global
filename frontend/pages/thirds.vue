<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Terceros</h2>          
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="thirds.length === 0">No hay Terceros</h3>
      </div>
      <div class="flex justify-center items-center" v-if="showPermissionsModal">
        <h3>Texto Disponible.</h3>
      </div>
      <table class="table-auto w-full permission-table" v-if="!showPermissionsModal">
        <thead>
          <tr>            
            <th :class="ui.th">Identificacion</th>
            <th :class="ui.th">Nombre</th>
            <th :class="ui.th">Apellido</th>
            <th :class="ui.th">Tipo</th>
            <th :class="ui.th">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(third, index) in thirds" :key="index">            
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="third.nit" @blur="saveItem(index,'identification',third.identification)" 
                  class="border rounded p-1 w-20" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="third.name" @blur="saveItem(index, 'name', third.name)" 
                  class="border rounded p-1 w-20" />
                <input v-model="third.second_name" @blur="saveItem(index, 'second_name', third.second_name)"
                  class="border rounded p-1 w-20" />              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="third.last_name" @blur="saveItem(index, 'last_name', third.last_name)"
                  class="border rounded p-1 w-20" />
                <input v-model="third.second_last_name"
                  @blur="saveItem(index, 'second_last_name', third.second_last_name)" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="third.nit" @blur="saveItem(index,'identification',third.identification)" 
                  class="border rounded p-1 w-20" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="" :class="ui.span">✏️</span>
                <span @click="deleteThird(third.id)" :class="ui.span">🗑️</span>
              </div>
            </td>

          </tr>
          <tr>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="newGroupName" placeholder="Nuevo grupo" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="newGroupName" placeholder="Nuevo grupo" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="newGroupName" placeholder="Nuevo grupo" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <input v-model="newGroupName" placeholder="Nuevo grupo" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">                
                <span @click="createGroup" :class="ui.span">💾</span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </UCard>

  </div>
</template>


<script setup lang="ts">

const buttonPermisos = ref('');

const thirds = ref([] as any[])

const showModal = () => {
  buttonPermisos.value = 'Ocultar'
}

const showPermissionsModal = ref(false)

const deleteThird = async (id: number) => {
  await $fetch(`api/auth/thirds/${id}`, {
    method: 'DELETE'
  })
  fetchThirds()
}



const saveItem = async (index: number, field: string, value: string) => {
  const third = thirds.value[index];
  third[field] = value;
  await $fetch(`api/thirds/${third.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
};


const fetchThirds = async () => {
  const response = await $fetch<any>('api/thirds?page_size=1000')
  thirds.value = response.results
}

onMounted(() => {
  fetchThirds()
  console.log('thirds', thirds)
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
