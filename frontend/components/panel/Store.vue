<template>
    <div class="flex gap-4 mb-4">
        <div class="grow">
            <SelectStore v-model="storeSelected"></SelectStore>
        </div>
        <div >
            <UButton @click="deleteHandler()">
                <i class="i-heroicons-trash-16-solid"></i>
                <i class="i-heroicons-map-pin"></i>
            </UButton>
        </div>
    </div>
    <UDivider class="mt-5 mb-2 font-size-50px color-#800000" />
    <div v-if="!isNew">
        Editando tercero: {{ storeSelected.name }}
        <UButton variant="link" @click="storeSelected = {} as Store;">&times;Borrar {{ storeSelected.name }} sin
            confirmacion</UButton>
    </div>
    <code>
      <!--  {{ JSON.stringify(thirdSelected, null, 2) }}  -->
    </code>
    <div class="grid grid-cols-2 gap-4">
        <div>
            <label>Nombre</label>
            <UInput v-model="storeEditing.name" />
        </div>
        <div>
            <label>Telefono</label>
            <UInput v-model="storeEditing.phone" />
        </div>
        <div>
            <label>Ciudad</label>
            <SelectCity v-model="storeEditing.city_name" ></SelectCity>
        </div>

    </div>
    <div class="grid grid-cols-1 gap-4">
        <div>
            <label>Email</label>
            <UInput v-model="storeEditing.email" />
        </div>
        <div>
            <label>Direccion</label>
            <UInput v-model="storeEditing.address" />
        </div>
    </div>
    <UDivider class="my-2"></UDivider>
    <UButton block @click="saveHandler">{{ isNew ? 'Crear' : 'Editar' }}</UButton>
</template>

<script setup lang="ts">
type Store = {
    id: number
    name: string
    email: string
    phone: number
    address: string
    description: string
    image: string
    city: number
    city_name: string
    city_full?: any[]   
}

const storeSelected = ref({} as Store)
const storeEditing = ref({} as Store)

const isNew = computed(() => !storeEditing.value.id)
const toast = useToast()
const emit = defineEmits(["update:modalShow"])




watch(() => storeSelected.value.id, async (value) => {
    storeEditing.value = { ...storeSelected.value }
    storeEditing.value.city_full = []
    //console.log("storeSelected.value", storeEditing.value)
    for (const cityId of storeEditing.value.city) {
       // storeEditing.value.city_full.push(await $fetch(`api/cities/${cityId}`))
    }
    
})

watch(() => storeEditing.value.city_name, async (value) => {
    storeEditing.value.city = storeEditing.value.city_name.id
})

const deleteHandler = async () => {
    try {
        if (!confirm("¿Estas seguro de eliminar la Bodega?")) {
            return
        }
        await $fetch(`api/stores/${storeEditing.value.id}`, {
            method: 'DELETE'
        })
        storeSelected.value = {} as Store
        storeEditing.value = {} as Store
        toast.add({ title: "Bodega eliminado" })
        emit("update:modalShow", false)
    } catch (e) {
        console.error(e)
    }
}

const saveHandler = async () => {
    try {
        if (isNew.value) {
            storeEditing.value.city = storeEditing.value.city_name.id
            const response = await $fetch("api/stores", {
                method: 'POST',
                body: storeEditing.value
            })
            storeSelected.value = response as Store

        } else {
            const savingObj = { ...storeEditing.value }
      
            // DEJO ESTO PA PROBAR 
            //savingObj.thirdtypes = [1] /// ESTO HAY QUE BORRARLO
            savingObj.city = storeEditing.value.city_name.id
            const response = await $fetch(`api/stores/${storeEditing.value.id}`, {
                method: 'PUT',
                body: savingObj
            })
            storeSelected.value = response as Store
        }
        toast.add({ title: "Bodega guardada" })
        emit("update:modalShow", false)

    } catch (e) {
        console.error(e)
    }
}

onMounted(async () => {

    
   
})

</script>

<style scoped></style>