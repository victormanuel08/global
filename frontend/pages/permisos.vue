<template>
    <div class="max-w-5xl mx-auto ">
        <UCard v-for="group in groups" :key="group.id" class="my-2">
            <template #header>
                <h2 class="font-bold">Grupo {{ group?.name }}</h2>
            </template>
            <div style="overflow: auto;">
                <table class="table-auto w-full permission-table">
                    <thead>
                        <tr>
                            <th :class="ui.th">
                                Entidad
                            </th>
                            <th :class="ui.th">
                                Agregar
                            </th>
                            <th :class="ui.th">
                                Editar
                            </th>
                            <th :class="ui.th">
                                Delete
                            </th>
                            <th :class="ui.th">
                                Ver
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="permissions, entity in permissionsByEntity" :key="entity">
                            <td :class="ui.td">{{ entity }}</td>
                            <td :class="ui.td">
                                <UCheckbox :class="ui.check" v-model="group.permissionsTable[permissions[0].id]" />
                            </td>
                            <td :class="ui.td">
                                <UCheckbox :class="ui.check" v-model="group.permissionsTable[permissions[1].id]" />
                            </td>
                            <td :class="ui.td">
                                <UCheckbox :class="ui.check" v-model="group.permissionsTable[permissions[2].id]" />
                            </td>
                            <td :class="ui.td">
                                <UCheckbox :class="ui.check" v-model="group.permissionsTable[permissions[3].id]" />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <UButton variant="soft" block @click="saveGroupPermissions(group)" class="mt-2">Guardar</UButton>
        </UCard>
    </div>

</template>

<script setup lang="ts">
const toast = useToast()
const permissionsByEntity = ref({} as Record<string, any>)
const allPermisions = ref([] as any[])
const groups = ref([] as any[])
const saving = ref(false)
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

const saveGroupPermissions = async (group: any) => {
    const permissions = Object.entries(group.permissionsTable).filter(([_, value]) => value).map(([key, _]) => parseInt(key))
    const requestBody = {
        permissions
    }
    saving.value = true
    try {

        const response = await $fetch(`api/auth/groups/${group.id}/`, {
            method: 'PATCH',
            body: requestBody
        })
        saving.value = false
        toast.add({ title: 'Guardado' })
        console.log('saveGroupPermissions', response)
        fetchGroups()
    } catch (e) {
        console.error(e)
        saving.value = false
        window.alert("Error")
    }
   
}

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center'
}

</script>
