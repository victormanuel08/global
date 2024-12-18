<template>
  <div class="max-w-5xl mx-auto">
    <UCard class="my-2">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Servicios</h2>
          <div class="flex gap-3 my-3">
            <SelectSpecialities v-model="newServiceSpeciality" class="border rounded p-1 w-64" />
            <input ref="fileInput" type="file" accept=".txt" @change="uploadListFile" class="hidden" />
            <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
              Cargar Archivo</UButton>
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="services.length === 0">No hay servicios</h3>
      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Codigo</th>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Especialidad</th>
              <th :class="ui.th">Soat</th>
              <th :class="ui.th">Particular</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(service, index) in services" :key="index">
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.code" @blur="saveItem(index, 'code', service.code)"
                    class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.description" @blur="saveItem(index, 'description', service.description)"
                    class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">

                  <SelectSpecialities v-model="service.speciality_full" class="border rounded p-1 w-64"
                    @change="saveItem(index, 'speciality', service.speciality_full.id)">
                  </SelectSpecialities>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.amount_soat" @blur="saveItem(index, 'amount_soat', service.amount_soat)"
                    class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="service.amount_particular"
                    @blur="saveItem(index, 'amount_particular', service.amount_particular)"
                    class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="deleteService(service.id, true)" :class="ui.span" v-if="service.code !== '012'">🗑️</span>
                </div>
              </td>
            </tr>

            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceCode" placeholder="Codigo" class="border rounded p-1 w-14" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceDescription" placeholder="Nombre" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectSpecialities v-model="newServiceSpeciality" class="border rounded p-1 w-64">
                  </SelectSpecialities>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceAmountSoat" placeholder="$ Soat" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newServiceAmountParticular" placeholder="$ Particular" class="border rounded p-1" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createService" :class="ui.span">
                    💾
                  </span>
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
const newServiceDescription = ref('')
const newServiceCode = ref('')
const newServiceSpeciality = ref<{ id?: number }>({})
const newServiceAmountSoat = ref('')
const newServiceAmountParticular = ref('')
//const search = ref('')

const {
  data: services,
  pagination,
  search,
  pending,
  refresh
} = usePaginatedFetch<any>("/api/services/");

const fetchServices = async () => {
  const {
    data: services,
    pagination,
    search,
    pending,
  } = usePaginatedFetch<any>("/api/services/");



}

const deleteService = async (id: number, confirmed: boolean) => {
  try {
    if (confirmed) {
      if (!confirm('¿Estás seguro de eliminar este Servicio?')) {
        return
      }
    }
    await $fetch(`api/services/${id}/`, {
      method: 'DELETE'
    })
    refresh()
    toast.add({ title: "Precio eliminado" })
  } catch (error) {
    toast.add({ title: "Error al eliminar el Precio" })
  }
}



const saveItem = async (index: number, field: string, value: string) => {
  const service = services.value[index];
  service[field] = value;
  const response = await $fetch(`api/services/${service.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
  refresh()
};

const createService = async () => {
  const message = confirm('¿Estás seguro de crear este Servicio?')

  if (!message) {
    newServiceCode.value = ''
    newServiceDescription.value = ''
    newServiceAmountSoat.value = ''
    newServiceAmountParticular.value = ''
    newServiceSpeciality.value = {}
    refresh()
    return
  }

  const response = await $fetch('api/services/', {
    method: 'POST',
    body: {
      code: newServiceCode.value,
      description: newServiceDescription.value,
      speciality: newServiceSpeciality.value.id,
      amount_soat: newServiceAmountSoat.value,
      amount_particular: newServiceAmountParticular.value
    }
  })
  refresh()
  newServiceCode.value = ''
  newServiceDescription.value = ''
  newServiceAmountSoat.value = ''
  newServiceAmountParticular.value = ''
  newServiceSpeciality.value = ''

}

onMounted(() => {
  refresh()
})

const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}

const fileInput = ref<HTMLInputElement | null>(null)
const toast = useToast()
const triggerFileInput = () => {
  if ( newServiceSpeciality.value.id === undefined) {
    toast.add({ title: "Seleccione una especialidad" })
    return
  }
  fileInput.value?.click()
}

const uploadListFile = async (event: any) => {
  const fileInput = event.target;
  if (!fileInput || !fileInput.files || fileInput.files.length === 0) {
    toast.add({ title: "No se ha seleccionado ningún archivo." });
    console.error("No se ha seleccionado ningún archivo.");
    return;
  }

  const file = fileInput.files[0];
  toast.add({ title: "Archivo seleccionado: " + file.name });


  const formData = new FormData();
  formData.append('file', file);

  if (!confirm("¿Estás seguro de cargar la lista de Servicios? Esto sobrescribirá y borrará todos los Servicios actuales de la especialidad seleccionada y establecerá estrictamente la lista suministrada.")) {
    return;
  }

  const serviceslist: { value: Array<{ id: number }> } = await $fetch(`api/services/?speciality=${newServiceSpeciality.value.id}`, {
    method: 'GET',
  });

  if (serviceslist.length > 0){
    await deleteServiceListByPackage(serviceslist.value);
  }

  const reader = new FileReader();
  reader.onload = async (e) => {
    const text = e.target?.result as string;
    const lines = text.split('\n');
    for (const line of lines) {

      toast.add({ title: "line: " + line });
      const [code, description,  pricesoat, priceparticular] = line.split(',');
     
      if (newServiceSpeciality.value.id !== undefined) {
        toast.add({ title: "Actualizando Servicio: " + code });
        await updateServicesList(newServiceSpeciality.value.id, code, description, parseFloat(pricesoat), parseFloat(priceparticular));
      } else {
        toast.add({ title: "Speciality ID no esta Definida" });
        console.error("Speciality ID no esta Definida");
      }
    }
    toast.add({ title: "Lista de Servicios actualizada" });
    fileInput.value = null;
  };
  reader.readAsText(file);
};



const deleteServiceListByPackage = async (list: Array<{ id: number }>) => {
  try {
    if (!confirm("¿Estas seguro de eliminar la lista de Servicios de la especialidad?")) {
      return
    }
    for (const service of list) {
      deleteService(service.id, false)
    }
    toast.add({ title: "Lista de Servicios eliminados" })
  } catch (error) {
    toast.add({ title: "Error al eliminar el Servicio" })
  }
}


const updateServicesList = async (speciality: number, code: string, description: string, pricesoat: number, priceparticular: number) => {
    try {
        const services = await $fetch<any>(`api/services/?code=${code}`, {
            method: 'GET'
        })
        toast.add({ title: `Actualizando precio para el código ${code}` })
 
        const priceEditing = {
                code: code,
                description: description,
                amount_soat: pricesoat,
                amount_particular: priceparticular,
                speciality: speciality
            }
        if (services.results.length > 0) {
            const service = services.results[0]
           
            const response = await $fetch(`api/services/${service.id}`, {
                method: 'PATCH',
                body: priceEditing
            })
            toast.add({ title: `Servicio ${description} actualizado` })
        }else{
           
            const response = await $fetch(`api/services/`, {
                method: 'POST',
                body: priceEditing
            })
            if (response){
              toast.add({ title: `Servicio ${description} creado` })
            }
            
        }
    } catch (error) {
        toast.add({ title: `Error al actualizar  el código ${code}` })
    }
    refresh()
}



</script>
