<template>

  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Usuarios</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="users.length === 0">No hay Usuarios</h3>
      </div>
      <table class="table-auto w-full permission-table">
        <thead>
          <tr>
            <th :class="ui.th">Usuario</th>
            <th :class="ui.th"><span title="Indica si el usuario debe ser tratado como activo. Desmarque esta opción en lugar de borrar la cuenta." >Activo</span></th>
            <th :class="ui.th"><span title="Indica si el usuario puede entrar en este sitio de Super Administración de Backend.">Staff</span></th>
            <th :class="ui.th"><span title="Indica que este usuario tiene todos los permisos sin asignárselos explícitamente.">SuperUser</span></th>
            <th :class="ui.th">Acciones</th>
          </tr>
        </thead>
        <tbody>

          <tr v-for="(user, index) in users" :key="index">
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UInput v-model="user.username" @blur="saveItem(index, 'username', user.username)"
                  class="border rounded p-1 w-48" />
              </div>
              <div class="grid grid-cols-3 justify-center" v-if="showUserGroups && user.id === selectedUserId">
                <div v-for="(group, index) in groups" :key="index" class="justify-center">
                  {{ group.name }} {{ group.id }} {{ user.id }}
                  <UCheckbox 
                    v-model="groupSelected" 
                    @change="saveUserGroups(group.id)" 
                    :value="group.id" />
                </div>
                
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UCheckbox v-model="user.is_active" @change="saveItem(index, 'is_active', user.is_active)"
                  class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UCheckbox v-model="user.is_staff" @change="saveItem(index, 'is_staff', user.is_staff)"
                  class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UCheckbox v-model="user.is_superuser" @change="saveItem(index, 'is_superuser', user.is_superuser)"
                  class="border rounded p-1" />
              </div>
            </td>

            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="toggleUserGroups(user.id)" :class="ui.span">🔍</span>
                <span @click="deleteUser(user.id)" :class="ui.span">🗑️</span>
              </div>
            </td>
          </tr>

          <tr>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UInput v-model="newUserUsername" placeholder="Usuario" class="border rounded p-1 w-48" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UCheckbox v-model="newUserActive" placeholder="Nombre" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UCheckbox v-model="newUserStaff" placeholder="Staff" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UCheckbox v-model="newUserSuperuser" placeholder="Super User" class="border rounded p-1" />
              </div>
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="createUser" :class="ui.span">💾</span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </UCard>
  </div>
</template>


<script setup lang="ts">

//const cities = ref([] as any[])
const newUserUsername = ref('')
const newUserActive = ref(0)
const newUserStaff = ref(0)
const newUserSuperuser = ref(0)
const groups = ref([] as any[])
const showUserGroups = ref(false)
const selectedUserId = ref()
const saving = ref(false)
const groupSelected = ref([] as number[]);


//const search = ref('')

const {
  data: users,
  pagination,
  search,
  pending,
} = usePaginatedFetch<any>("/api/auth/users/");

const toggleUserGroups = (user_id: number) => {
  showUserGroups.value = !showUserGroups.value
  groupSelected.value = []
  selectedUserId.value = user_id
}

const fetchUsers = async () => {
  const {
    data: users,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/auth/users/");

  console.log('FecthUsers', users.value)

}

const fetchGroups = async () => {
  const response = await $fetch<any>('api/auth/groups/')
  console.log('fetchGroups', response)
  groups.value = response.results
  console.log('fetchGroups', groups.value)
}

const deleteUser = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este Usuario?')
  if (message) {
    const response = await $fetch(`api/auth/users/${id}/`, {
      method: 'DELETE'
    })
    fetchUsers()
  }
}



const saveItem = async (index: number, field: string, value: string) => {
  const user = users.value[index];
  user[field] = value;
  const response = await $fetch(`api/auth/users/${user.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchUsers();
};

const saveCheck = async (index: number, field: string, value: string) => {
  const user = users.value[index];
  user[field] = value;
  const response = await $fetch(`api/auth/users/${user.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  fetchUsers();
};

const createUser = async () => {
  const message = confirm('¿Estás seguro de crear este Usuario?')

  if (!message) {
    newUserUsername.value = ''
    newUserActive.value = 0
    newUserStaff.value = 0
    newUserSuperuser.value = 0
    fetchUsers()
    return
  }

  const response = await $fetch('api/auth/users/', {
    method: 'POST',
    body: {
      username: newUserUsername.value,
      is_active: newUserActive.value,
      is_staff: newUserStaff.value,
      is_superuser: newUserSuperuser.value
    }
  })
  fetchUsers()
  newUserSuperuser.value = 0
  newUserStaff.value = 0
  newUserActive.value = 0
  newUserUsername.value = ''
}

onMounted(() => {
  fetchUsers()
  fetchGroups()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}


const saveUserGroups = async (value: number) => {
  console.log('Guardando', groupSelected.value + ' ' + selectedUserId.value);
  const oldusers = await $fetch<any>(`api/auth/groups/${value}/`, {
    method: 'GET',
  });
  console.log('RespuestaOld:', oldusers?.users);
  console.log('RespuestaNew:', selectedUserId?.value);
  const updatedusers = oldusers.users.concat(selectedUserId.value);
  console.log('RespuestaUpdated:', updatedusers);
  
  const response = await $fetch<any>(`api/auth/groups/${value}/`, {//aca pegar es group 
    method: 'PATCH',
    body: ({
        users: updatedusers,
      }),
  });
  console.log('Respuesta:', response);

};

</script>
