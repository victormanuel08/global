<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Grupos</h2>
          <UButton variant="soft" @click="showModal">{{ buttonPermisos }}</UButton>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="groups.length === 0">No hay grupos</h3>
      </div>
      <div class="flex justify-center items-center" v-if="showPermissionsModal">
        <h3>Seleccione los permisos de cada Grupo. Recuerde dar click en Guardar en cada Grupo que haya editado.</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table" v-if="!showPermissionsModal">
          <thead>
            <tr>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(group, index) in groups" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="group.name" @blur="saveName(index)" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteGroup(group.id)" :class="ui.span">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newGroupName" placeholder="Nuevo grupo" class="border rounded p-1" />
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
      </div>
    </UCard>
    <div v-if="showPermissionsModal">
      <permisos></permisos>
    </div>
  </div>
</template>


<script setup lang="ts">
import permisos from './permisos.vue';

const permissionsByEntity = ref({} as Record<string, any>)
const allPermisions = ref([] as any[])
const groups = ref([] as any[])

const editing = ref(false)
const newGroupName = ref('')
const showPermissionsModal = ref(false)
const buttonPermisos = ref('Ver Permisos');

const showModal = () => {
  showPermissionsModal.value = !showPermissionsModal.value;
  buttonPermisos.value = showPermissionsModal.value ? 'Ocultar Permisos' : 'Ver Permisos';
};

const deleteGroup = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este grupo?')
  if (message) {
    const response = await $fetch(`api/auth/groups/${id}/`, {
      method: 'DELETE'
    })
    fetchGroups()
  }
}
const createGroup = async () => {
  const message = confirm('¿Estás seguro de crear este grupo?')

  if (!message) {
    newGroupName.value = ''
    fetchGroups()
    return
  }

  const response = await $fetch('api/auth/groups/', {
    method: 'POST',
    body: {
      name: newGroupName.value
    }
  })
  fetchGroups()
  newGroupName.value = ''
}

const saveName = async (index: number) => {
  const group = groups.value[index];
  const isNewGroup = group.id === 0;
 
 
    try {
      if (isNewGroup) {
        const response = await $fetch('api/auth/groups/', {
          method: 'POST',
          body: {
            name: group.name,
          },
        });
      } else {
        const response = await $fetch(`api/auth/groups/${group.id}/`, {
          method: 'PATCH',
          body: {
            name: group.name,
          },
        });
      }

      editing.value = false;
    } catch (error) {
      console.error('Error al guardar los cambios:', error);
    }
 
  fetchGroups();
  return;
};


const fetchPermissions = async () => {
  const response = await $fetch<any>('api/auth/permissions?page_size=1000')
  allPermisions.value = response.results
  response.results.forEach((permission: any) => {
    const entity_name = permission.entity_name
    if (entity_name in permissionsByEntity.value) {
      permissionsByEntity.value[entity_name].push(permission)
    } else {
      permissionsByEntity.value[entity_name] = [permission]
    }
  })
}

const fetchGroups = async () => {
  const response = await $fetch<any>('api/auth/groups?page_size=1000')
  for (const group of response.results) {
    group.permissionsTable = {}
    allPermisions.value.map((p: any) => p.id).forEach((permissionId: number) => {
      group.permissionsTable[permissionId] = group.permissions.includes(permissionId)
    })
  }
  groups.value = response.results
}

onMounted(() => {
  fetchPermissions().then(() => fetchGroups()) // Primero permisos, luego grupos
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

</script>
