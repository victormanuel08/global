<template>
  <ModalEditRecordAmbulance :calendarEvent="thirdSelected" v-if="isAmbulance" />
  <div class="max-w-5xl mx-auto">

    <UCard class="m-3">
      <template #header>
        <div class="flex justify-between items-center">
          <h2 class="font-bold">Terceros</h2>
          <div class="flex gap-3 my-3">
            <input ref="fileInput" type="file" accept=".txt" @change="uploadListFile" class="hidden" />
            <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
              Cargar Archivo</UButton>
            <UInput v-model="search" placeholder="Buscar" />
            <UPagination v-model="pagination.page" :page-count="pagination.pageSize" :total="pagination.resultsCount" />
          </div>
        </div>
      </template>
      <div class="flex justify-center items-center">
        <h3 v-if="thirds.length === 0">No hay Tecreros</h3>
      </div>
      <div>

      </div>
      <div style="overflow: auto;">
        <table class="table-auto w-full permission-table">
          <thead>
            <tr>
              <th :class="ui.th">Identificacion</th>
              <th :class="ui.th">Nombre</th>
              <th :class="ui.th">Apellidos</th>
              <th :class="ui.th">Usuario</th>
              <th :class="ui.th">Acciones</th>
            </tr>
          </thead>
          <tbody>

            <tr v-for="(third, index) in thirds" :key="index">
              <td :class="ui.td" v-if="third.id != '2'">
                <div class="flex items-center justify-center">
                  {{ third.type_document }}
                  <UInput v-model="third.nit" @blur="saveItem(index, 'nit', third.nit)"
                    class="border rounded p-1 w-32" />
                </div>
              </td>
              <td :class="ui.td" v-if="third.id != '2'">
                <div class="flex items-center justify-center">
                  <UInput v-model="third.name" @blur="saveItem(index, 'name', third.name)"
                    :class="third.type_document === 'NI' ? 'border rounded p-1 w-64' : 'border rounded p-1 w-32'" />
                  <UInput v-model="third.second_name" @blur="saveItem(index, 'second_name', third.second_name)"
                    class="border rounded p-1 w-32" v-if="third.type_document !== 'NI'" />
                </div>
              </td>
              <td :class="ui.td" v-if="third.id != '2'">
                <div class="flex items-center justify-center">
                  <UInput v-model="third.last_name" @blur="saveItem(index, 'last_name', third.last_name)"
                    class="border rounded p-1 w-32" v-if="third.type_document !== 'NI'" />
                  <UInput v-model="third.second_last_name"
                    @blur="saveItem(index, 'second_last_name', third.second_last_name)" class="border rounded p-1 w-32"
                    v-if="third.type_document !== 'NI'" />
                </div>
              </td>
              <td :class="ui.td" v-if="third.id != '2'">
                <div class="flex items-center justify-center">
                  <SelectUsers class="border rounded p-1 w-32" v-model="third.user_full"
                    @change="saveItem(index, 'user', third.user_full.id)">
                  </SelectUsers>
                </div>

              </td>
              <td :class="ui.td" v-if="third.id != '2'">
                <div class="flex items-center justify-center">
                  <span @click="setPassword(third.user_full.id)" :class="ui.span" v-if="third.user_full?.id">🔑</span>
                  <span @click="signedThird(third)" :class="ui.span">🖊️</span>
                  <span @click="showModalThird(third)" :class="ui.span" v-if="third.id != '2'">📝</span>
                  <span @click="deleteThird(third.id)" :class="ui.span" v-if="third.id != '2'">🗑️</span>
                </div>
              </td>
            </tr>
            <tr>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectChoice :choiceType="'TYPE_DOCUMENT_CHOICES'" v-model="newThirdDocument"
                    class="border rounded p-1 w-32" />
                </div>
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdNit" placeholder="Identificacion" class="border rounded p-1 w-32" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdName" placeholder="Nombre" class="border rounded p-1 w-64" />
                </div>
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdSecondName" placeholder="Segundo Nombre" class="border rounded p-1 w-64" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdLastName" placeholder="Apellido" class="border rounded p-1 w-64" />
                </div>
                <div class="flex items-center justify-center">
                  <UInput v-model="newThirdSecondLastName" placeholder="Segundo Apellido"
                    class="border rounded p-1 w-64" />
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <SelectUsers class="border rounded p-1 w-32" v-model="newThirdUser">
                  </SelectUsers>
                </div>
              </td>
              <td :class="ui.td">
                <div class="flex items-center justify-center">
                  <span @click="createThird" :class="ui.span">💾</span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </UCard>

  </div>
  <ModalEditThird :third="thirdSelected" :typeT="'P'" v-model="isThird" @update:modelValue="modalClosedHandler" />
  <ModalSign  @close="handleModalClose" v-model="isSing"  :third="third" :typeThird="'signed'" />
    
</template>


<script setup lang="ts">

import Swal from 'sweetalert2';



const newThirdDocument = ref({})
const newThirdNit = ref('')
const newThirdName = ref('')
const newThirdSecondName = ref('')
const newThirdLastName = ref('')
const newThirdSecondLastName = ref('')
const newThirdType = ref('')
const newThirdSex = ref('')
const newThirdBlood = ref('')
const blood_list = ref({})
const etnias_list = ref({})
const sex_list = ref({})
const newThirdUser = ref({})
const maternity_breasfeeding_list = ref({})
const maternity_breastfeeding_complementary_list = ref({})
const maternity_breastfeeding_extend_list = ref({})
const maternity_pregnancy_list = ref({})
const maternity_violence_list = ref({})
const type_list = ref({})
const isThird = ref(false)
const isAmbulance = ref(false)
const thirdSelected = ref({})
const user_full = ref({})
const isSing = ref(false)
const third = ref({} as any)

const close = defineEmits(['close'])

const {
  data: thirds,
  pagination,
  search,
  pending,
  refresh
} = usePaginatedFetch<any>("/api/thirds/");





const fetchChoices = async () => {
  const response = await $fetch<any>('api/api/choices/')

  blood_list.value = response.BLOOD_CHOICES
  etnias_list.value = response.ETNIAS_CHOICES
  maternity_breasfeeding_list.value = response.MATERNITY_BREASTFEEDING_CHOICES
  maternity_breastfeeding_complementary_list.value = response.MATERNITY_BREASTFEEDING_COMPLEMENTARY_CHOICES
  maternity_breastfeeding_extend_list.value = response.MATERNITY_BREASTFEEDING_EXTEND_CHOICES
  maternity_pregnancy_list.value = response.MATERNITY_PREGNANCY_CHOICES
  maternity_violence_list.value = response.MATERNITY_VIOLENCE_CHOICES
  type_list.value = response.TYPE_CHOICES
  sex_list.value = response.SEX_CHOICES


}

const deleteThird = async (id: number) => {
  const message = confirm('¿Estás seguro de eliminar este Tercero?')
  if (message) {
    const response = await $fetch(`api/thirds/${id}/`, {
      method: 'DELETE'
    })
    refresh()
  }
}

const saveItem = async (index: number, field: string, value: string) => {
  const third = thirds.value[index];

  third[field] = value;
  if (field === 'user' && value) {
    const response: { results: any[] } = await $fetch(`api/thirds/`, {
      method: 'GET',
      query: {
        user: value
      }
    });

    if (response.results.length > 0 && response.results[0].id !== third.id) {
      
      toast.add({ title: "El usuario ya esta asignado" });
      refresh();
      return
    }
  }
  const response = await $fetch(`api/thirds/${third.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });

  refresh();
};

const createThird = async () => {

  const message = confirm('¿Estás seguro de crear este Tercero?')

  if (!message) {
    newThirdDocument.value = ''
    newThirdNit.value = ''
    newThirdName.value = ''
    newThirdSecondName.value = ''
    newThirdLastName.value = ''
    newThirdSecondLastName.value = ''
    newThirdType.value = ''
    newThirdSex.value = ''
    newThirdBlood.value = ''
    newThirdUser.value = ''
    refresh();
    return
  }

  const response = await $fetch('api/thirds/', {
    method: 'POST',
    body: {
      type_document: newThirdDocument.value.id,
      nit: newThirdNit.value,
      name: newThirdName.value,
      second_name: newThirdSecondName.value,
      last_name: newThirdLastName.value,
      second_last_name: newThirdSecondLastName.value,
      type: newThirdType.value,
      blood_type: newThirdBlood.value,
      sex: newThirdSex.value,
      user: newThirdUser.value.id

    },
  })
  refresh();
  newThirdDocument.value = ''
  newThirdNit.value = ''
  newThirdName.value = ''
  newThirdSecondName.value = ''
  newThirdLastName.value = ''
  newThirdSecondLastName.value = ''
  newThirdType.value = ''
  newThirdSex.value = ''
  newThirdBlood.value = ''
}

onMounted(() => {
  window.onload = function () {
    window.scrollTo(0, 0);
  };
  refresh();
  fetchChoices()
})

const showModalThird = (value: any) => {
  thirdSelected.value = value

  isThird.value = true
}

const showModalRecordAmbulance = (value: any) => {
  thirdSelected.value = value

  isAmbulance.value = true
}

watch(() => close, () => {
  isThird.value = false
  isAmbulance.value = false

})

const modalClosedHandler = (value: any) => {
  if (!value) { // Si el valor es false, significa que la modal se ha cerrado
    // alert('close')
    refresh();
  }
}


const ui = {
  td: 'p-1 border',
  th: 'p-2 border',
  check: 'align-center justify-center',
  span: 'cursor-pointer'
}



const fileInput = ref<HTMLInputElement | null>(null)
const toast = useToast()
const triggerFileInput = () => {
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

  if (!confirm("¿Estás seguro de cargar la lista de Terceros? Esta acción no se puede deshacer.")) {
    return;
  }

  const reader = new FileReader();
  reader.onload = async (e) => {
    const text = e.target?.result as string;
    const lines = text.split('\n');
    for (const line of lines) {
   
      let [type_document, nit, name, second_name, last_name, second_last_name, date_birth, year_old, sex, email, phone, address, type, maternity_pregnancy, maternity_breasfeeding, maternity_breasfeeding_extend, maternity_breasfeeding_complementary, maternity_violence, ethnicity, blood_type, status, occupation, zone, allergies, pathologies, medications, liquids_foods, created_at, updated_at, city_id, city_birth_id, speciality_id, user_id, vehicle_id] = line.split(',');
      
      if (!email) {
        toast.add({ title: "No se ha encontrado el email: " + email + " se pondrá un valor por defecto" });
        email = last_name + name + "@gmail.com";
      }
      toast.add({ title: "Type-Nit: " + type + nit });

      try {
        const user: { results: any[] } = await $fetch(`api/auth/users/?username=${type}${nit}`, {
          method: 'GET'
        });
        toast.add({ title: "Nit: " + nit });

        const userId = user.results[0]?.id ?? 0;
        if (userId === 0) {
          toast.add({ title: "No se ha encontrado el Usuario : " + type + nit });
          const responseUser: { id: number } = await $fetch('api/auth/users/', {
            method: 'POST',
            body: {
              username: type + nit,
              is_active: 1,
              is_staff: 0,
              is_superuser: 0,
              email: email,
              first_name: name + " " + second_name,
              last_name: last_name + " " + second_last_name,
              password: nit
            }
          });
          if (responseUser) {
            toast.add({ title: "Usuario creado: " + type + nit });
            const response = await $fetch('api/thirds/', {
              method: 'POST',
              body: {
                type_document: type_document,
                nit: nit,
                name: name,
                second_name: second_name,
                last_name: last_name,
                second_last_name: second_last_name,
                date_birth: date_birth ? date_birth : "1950-01-01",
                year_old: null,
                sex: sex,
                email: email,
                phone: phone,
                address: address,
                type: type,
                maternity_pregnancy: maternity_pregnancy,
                maternity_breasfeeding: maternity_breasfeeding,
                maternity_breasfeeding_extend: maternity_breasfeeding_extend,
                maternity_breasfeeding_complementary: maternity_breasfeeding_complementary,
                maternity_violence: maternity_violence,
                ethnicity: ethnicity,
                blood_type: blood_type,
                status: status,
                occupation: occupation,
                zone: zone,
                allergies: allergies,
                pathologies: pathologies,
                medications: medications,
                liquids_foods: liquids_foods,
                city: parseInt(city_id),
                city_birth: parseInt(city_birth_id),
                speciality: parseInt(speciality_id),
                user: responseUser.id,
                vehicle: parseInt(vehicle_id)
              },
            });
            if (response) {
              toast.add({ title: "Tercero creado: " + name });
              await $fetch(`api/auth/users/${responseUser.id}/set_password/`, {
                method: 'PATCH',
                body: {
                  new_password: nit
                }
              });
              toast.add({ title: "Contraseña establecida para: " + type + nit });
            }
            continue;
          }
        } else {
          toast.add({ title: "Usuario encontrado: " + user.results[0]?.username });
          const responseThirds: { results: any[] } = await $fetch(`api/thirds/?nit=${nit}`, {
            method: 'GET'
          });
          if (responseThirds.results.length > 0) {
            const third = responseThirds.results[0];
            const response = await $fetch(`api/thirds/${third.id}`, {
              method: 'PATCH',
              body: {
                type_document: type_document,
                nit: nit,
                name: name,
                second_name: second_name,
                last_name: last_name,
                second_last_name: second_last_name,
                date_birth: date_birth ? date_birth : "1950-01-01",
                year_old: null,
                sex: sex,
                email: email,
                phone: phone,
                address: address,
                type: type,
                maternity_pregnancy: maternity_pregnancy,
                maternity_breasfeeding: maternity_breasfeeding,
                maternity_breasfeeding_extend: maternity_breasfeeding_extend,
                maternity_breasfeeding_complementary: maternity_breasfeeding_complementary,
                maternity_violence: maternity_violence,
                ethnicity: ethnicity,
                blood_type: blood_type,
                status: status,
                occupation: occupation,
                zone: zone,
                allergies: allergies,
                pathologies: pathologies,
                medications: medications,
                liquids_foods: liquids_foods,
                city: parseInt(city_id),
                city_birth: parseInt(city_birth_id),
                speciality: parseInt(speciality_id),
                user: userId,
                vehicle: parseInt(vehicle_id)
              },
            });
            if (response) {
              toast.add({ title: "Tercero actualizado: " + name });
              await $fetch(`api/auth/users/${userId}/set_password/`, {
                method: 'PATCH',
                body: {
                  new_password: nit
                }
              });
              toast.add({ title: "Contraseña establecida para: " + type + nit });
            }
          } else {
            const response = await $fetch('api/thirds/', {
              method: 'POST',
              body: {
                type_document: type_document,
                nit: nit,
                name: name,
                second_name: second_name,
                last_name: last_name,
                second_last_name: second_last_name,
                date_birth: date_birth ? date_birth : "1950-01-01",
                year_old: null,
                sex: sex,
                email: email,
                phone: phone,
                address: address,
                type: type,
                maternity_pregnancy: maternity_pregnancy,
                maternity_breasfeeding: maternity_breasfeeding,
                maternity_breasfeeding_extend: maternity_breasfeeding_extend,
                maternity_breasfeeding_complementary: maternity_breasfeeding_complementary,
                maternity_violence: maternity_violence,
                ethnicity: ethnicity,
                blood_type: blood_type,
                status: status,
                occupation: occupation,
                zone: zone,
                allergies: allergies,
                pathologies: pathologies,
                medications: medications,
                liquids_foods: liquids_foods,
                city: parseInt(city_id),
                city_birth: parseInt(city_birth_id),
                speciality: parseInt(speciality_id),
                user: userId,
                vehicle: parseInt(vehicle_id)
              },
            });
          }
        }
      } catch (error) {
        console.error("Error procesando la línea:", line, error);
        toast.add({ title: "Error procesando la línea: " + line });
      }
    }
    toast.add({ title: "Lista de Terceros actualizada" });
    fileInput.value = null;
  };
  reader.readAsText(file);
};

const handleModalClose = (value: any) => {
  if (!value) {
    isSing.value = false
    refresh();
  }
}

const signedThird = (value: any) => {
  third.value = value.id
  isSing.value = true
}



const setPassword = async (id: number) => {
  // Mostrar un input usando SweetAlert2
  const { value: newPassword } = await Swal.fire({
    title: 'Establecer nueva contraseña',
    input: 'password',  // Tipo de input para una contraseña
    inputLabel: 'Ingresa la nueva contraseña',
    inputPlaceholder: 'Contraseña',
    showCancelButton: true,
    confirmButtonText: 'Establecer',
    cancelButtonText: 'Cancelar',
    inputValidator: (value) => {
      if (!value) {
        return 'Por favor ingresa una contraseña'; // Validación para asegurarse de que no esté vacío
      }
    }
  });

  // Si el usuario no canceló y proporcionó una contraseña
  if (newPassword) {
    // Enviar la nueva contraseña al endpoint
    try {
      const response = await $fetch(`api/thirds/${id}/set_password/`, {
        method: 'PATCH',
        body: {
          new_password: newPassword  // Usar la contraseña proporcionada
        }
      });

      if (response) {
        // Mostrar un mensaje de éxito con SweetAlert2
        Swal.fire('Contraseña establecida', 'La contraseña se ha actualizado correctamente.', 'success');
      }
    } catch (error) {
      // Mostrar un mensaje de error si algo salió mal
      Swal.fire('Error', 'Hubo un problema al establecer la contraseña.', 'error');
    }
  }
};



</script>


