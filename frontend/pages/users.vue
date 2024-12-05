<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Usuarios</h2>
          <div class="flex gap-3 my-3">
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" 
                         :page-count="pagination.pageSize" 
                         :total="pagination.resultsCount" 
            />
          </div>
        </div>
      </template>

      <div v-if="users.length === 0" class="flex justify-center items-center">
        <h3>No hay Usuarios</h3>
      </div>

      <table class="table-auto w-full permission-table">
        <thead>
          <tr>
            <th :class="ui.th">Usuario</th>
            <th :class="ui.th">
              <span title="Indica si el usuario debe ser tratado como activo.">Activo</span>
            </th>
            <th :class="ui.th">
              <span title="Indica si el usuario puede entrar en este sitio.">Staff</span>
            </th>
            <th :class="ui.th">
              <span title="Indica que este usuario tiene todos los permisos.">SuperUser</span>
            </th>
            <th :class="ui.th">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <!-- Usuarios existentes -->
          <tr v-for="(user, index) in users" :key="index">
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <UInput v-model="user.username" 
                        @blur="saveItem(index, 'username', user.username)" 
                        class="border rounded p-1 w-48" 
                />
              </div>
              <div v-if="showUserGroups && user.id === selectedUserId" class="grid grid-cols-3 justify-center">
                <div v-for="(group, index) in groups" :key="index" class="justify-center">
                  <input type="checkbox" 
                         :checked="validateGroupUser(group.id, selectedUserId)" 
                         @change="saveUserGroups(group.id, selectedUserId)" 
                         :data-group-id="group.id" 
                  />
                  {{ group.name }}
                </div>
              </div>
            </td>
            <td :class="ui.td">
              <UCheckbox v-model="user.is_active" 
                         @change="saveItem(index, 'is_active', user.is_active)" 
                         class="border rounded p-1" 
              />
            </td>
            <td :class="ui.td">
              <UCheckbox v-model="user.is_staff" 
                         @change="saveItem(index, 'is_staff', user.is_staff)" 
                         class="border rounded p-1" 
              />
            </td>
            <td :class="ui.td">
              <UCheckbox v-model="user.is_superuser" 
                         @change="saveItem(index, 'is_superuser', user.is_superuser)" 
                         class="border rounded p-1" 
              />
            </td>
            <td :class="ui.td">
              <div class="flex items-center justify-center">
                <span @click="toggleUserGroups(user.id)" :class="ui.span">🔍</span>
                <span @click="deleteUser(user.id)" :class="ui.span">🗑️</span>
              </div>
            </td>
          </tr>

          <!-- Formulario para nuevo usuario -->
          <tr>
            <td :class="ui.td">
              <UInput v-model="newUserUsername" placeholder="Usuario" class="border rounded p-1 w-48" />
            </td>
            <td :class="ui.td">
              <UCheckbox v-model="newUserActive" class="border rounded p-1" />
            </td>
            <td :class="ui.td">
              <UCheckbox v-model="newUserStaff" class="border rounded p-1" />
            </td>
            <td :class="ui.td">
              <UCheckbox v-model="newUserSuperuser" class="border rounded p-1" />
            </td>
            <td :class="ui.td">
              <span @click="createUser" :class="ui.span">💾</span>
            </td>
          </tr>
        </tbody>
      </table>
    </UCard>
  </div>
</template>

<script setup lang="ts">
// Estado
const newUserUsername = ref('');
const newUserActive = ref(false);
const newUserStaff = ref(false);
const newUserSuperuser = ref(false);
const groups = ref<any[]>([]);
const showUserGroups = ref(false);
const selectedUserId = ref<number | null>(null);
const groupSelected = ref<number[]>([]);
const toast = useToast();

const { data: users, pagination, search, refresh } = usePaginatedFetch<any>('/api/auth/users/');

// Métodos
const fetchUsers = () => refresh();

const fetchGroups = async () => {
  const response = await $fetch<any>('api/auth/groups/');
  groups.value = response.results;
};

const toggleUserGroups = async (userId: number) => {
  showUserGroups.value = !showUserGroups.value;
  const response = await $fetch<any>(`api/auth/users/${userId}`, { method: 'GET' });
  groupSelected.value = response?.groups || [];
  selectedUserId.value = userId;
};

const validateGroupUser = (groupId: number, userId: number): boolean => {
  return groupSelected.value.includes(groupId);
};

const saveItem = async (index: number, field: string, value: any) => {
  try {
    const user = users.value[index];
    user[field] = value;
    const response = await $fetch(`api/auth/users/${user.id}`, {
      method: 'PATCH',
      body: JSON.stringify({ [field]: value }),
    });
    refresh();
    toast.add({ title: `Usuario actualizado correctamente.` });
  } catch (error: any) {
    toast.add({ title: `Error al actualizar usuario: ${error.message}` });
  }
};

const saveUserGroups = async (groupId: number, userId: number) => {
  try {
    const response = await $fetch<any>(`api/auth/users/${userId}`, { method: 'GET' });
    const currentGroups = response?.groups || [];
    const isChecked = document.querySelector(`input[data-group-id="${groupId}"]`)?.checked;
    const updatedGroups = isChecked
      ? [...currentGroups, groupId]
      : currentGroups.filter((id: number) => id !== groupId);
    await $fetch(`api/auth/users/${userId}`, {
      method: 'PATCH',
      body: JSON.stringify({ groups: updatedGroups }),
    });
    toast.add({ title: `Grupos de usuario actualizados correctamente.` });
  } catch (error: any) {
    toast.add({ title: `Error al actualizar grupos: ${error.message}` });
  }
};

const deleteUser = async (id: number) => {
  if (confirm('¿Estás seguro de eliminar este Usuario?')) {
    try {
      await $fetch(`api/auth/users/${id}/`, { method: 'DELETE' });
      refresh();
      toast.add({ title: `Usuario eliminado correctamente.` });
    } catch (error: any) {
      toast.add({ title: `Error al eliminar usuario: ${error.message}` });
    }
  }
};

const createUser = async () => {
  if (confirm('¿Estás seguro de crear este Usuario?')) {
    try {
      await $fetch('api/auth/users/', {
        method: 'POST',
        body: JSON.stringify({
          username: newUserUsername.value,
          is_active: newUserActive.value,
          is_staff: newUserStaff.value,
          is_superuser: newUserSuperuser.value,
        }),
      });
      refresh();
      resetNewUser();
      toast.add({ title: `Usuario creado correctamente.` });
    } catch (error: any) {
      toast.add({ title: `Error al crear usuario: ${error.message}` });
    }
  }
};

const resetNewUser = () => {
  newUserUsername.value = '';
  newUserActive.value = false;
  newUserStaff.value = false;
  newUserSuperuser.value = false;
};

// Inicialización
onMounted(() => {
  fetchUsers();
  fetchGroups();
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
