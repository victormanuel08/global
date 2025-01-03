<template>
  <div class="grid grid-cols-2 gap-4 md:grid-cols-4 m-4">
    <!--
    <div>
      <label class="block text-sm font-medium text-gray-700">Tipo Documento:</label>
      <SelectChoice :choiceType="'TYPE_DOCUMENT_CHOICES'" v-model="thirdSelected.type_document_full"
        @change="saveItem(thirdSelected.id, 'type_document', thirdSelected.type_document_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
      <UInput v-model="thirdSelected.nit" @change="saveItem(thirdSelected.id, 'nit', thirdSelected.nit)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Sexo:</label>
      <SelectChoice :choiceType="'SEX_CHOICES'" v-model="thirdSelected.sex_full"
        @change="saveItem(thirdSelected.id, 'sex', thirdSelected.sex_full.id)" />
    </div>
    -->

    <div>
      <label class="block text-sm font-medium text-gray-700">Nombre:</label>
      <UInput v-model="thirdSelected.name" @change="saveItem(thirdSelected.id, 'name', thirdSelected.name)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Segundo Nombre:</label>
      <UInput v-model="thirdSelected.second_name"
        @change="saveItem(thirdSelected.id, 'second_name', thirdSelected.second_name)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Apellido:</label>
      <UInput v-model="thirdSelected.last_name"
        @change="saveItem(thirdSelected.id, 'last_name', thirdSelected.last_name)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Segundo Apellido:</label>
      <UInput v-model="thirdSelected.second_last_name"
        @change="saveItem(thirdSelected.id, 'second_last_name', thirdSelected.second_last_name)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Zona:{{ thirdSelected.zone_full }}</label>
      <SelectChoice :choiceType="'ZONE_CHOICES'" v-model="thirdSelected.zone_full"
        @change="saveItem(thirdSelected.id, 'zone', thirdSelected.zone_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Ciudad Residencia:</label>
      <SelectCities v-model="thirdSelected.city_full"
        @change="saveItem(thirdSelected.id, 'city', thirdSelected.city_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Ciudad Nacimiento:</label>
      <SelectCities v-model="thirdSelected.city_birth_full"
        @change="saveItem(thirdSelected.id, 'city_birth', thirdSelected.city_birth_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Edad: {{ calculateAge(thirdSelected.date_birth) }}</label>
      <UInput type="date" v-model="thirdSelected.date_birth"
        @change="saveItem(thirdSelected.id, 'date_birth', thirdSelected.date_birth)" />
    </div>



    <div>
      <label class="block text-sm font-medium text-gray-700">Telefono:</label>
      <UInput v-model="thirdSelected.phone" @change="saveItem(thirdSelected.id, 'phone', thirdSelected.phone)" />
    </div>
    <!--
    <div>
      <label class="block text-sm font-medium text-gray-700">Tipo Persona:</label>
      <SelectChoice :choiceType="'TYPE_CHOICES'" v-model="thirdSelected.type_full"
        @change="saveItem(thirdSelected.id, 'type', thirdSelected.type_full.id)" />
    </div>


    <div>
      <label class="block text-sm font-medium text-gray-700">Ocupacion:</label>
      <SelectChoice :choiceType="'OCCUPATION_CHOICES'" v-model="thirdSelected.occupation_full"
        @change="saveItem(thirdSelected.id, 'occupation', thirdSelected.occupation_full.id)" />
    </div>
    -->
    <div v-if="thirdSelected.type_full?.id === 'M'">
      <label class="block text-sm font-medium text-gray-700">Especialidad:</label>
      <SelectSpecialities v-model="thirdSelected.speciality_full"
        @change="saveItem(thirdSelected.id, 'speciality', thirdSelected.speciality_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Profesion:</label>
      <UInput v-model="thirdSelected.profesion"
        @change="saveItem(thirdSelected.id, 'profesion', thirdSelected.profesion)" />
    </div>
    <div v-if="thirdSelected.type_full?.id === 'M'">
      <label class="block text-sm font-medium text-gray-700">T.P.:</label>
      <UInput v-model="thirdSelected.tp" @change="saveItem(thirdSelected.id, 'tp', thirdSelected.tp)" />
    </div>



    <div>
      <label class="block text-sm font-medium text-gray-700">Etnia:</label>
      <SelectChoice :choiceType="'ETNIAS_CHOICES'" v-model="thirdSelected.etnia_full"
        @change="saveItem(thirdSelected.id, 'ethnicity', thirdSelected.etnia_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Tipo Sangre:</label>
      <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="thirdSelected.blood_full"
        @change="saveItem(thirdSelected.id, 'blood_type', thirdSelected.blood_full.id)" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700">Estado Civil:</label>
      <SelectChoice :choiceType="'STATUS_CHOICES'" v-model="thirdSelected.status_full"
        @change="saveItem(thirdSelected.id, 'status', thirdSelected.status_full.id)" />
    </div>


    <div>
      <label class="block text-sm font-medium text-gray-700">Vehiculo:</label>
      <SelectVehicle v-model="thirdSelected.vehicle_full"
        @change="saveItem(thirdSelected.id, 'vehicle', thirdSelected.vehicle_full.id)" />
    </div>

    <div>
      <label class="block text-sm font-medium text-gray-700">Email:</label>
      <UInput v-model="thirdSelected.email" @change="saveItem(thirdSelected.id, 'email', thirdSelected.email)" />
    </div>
    <div>
      
      <label class="block text-sm font-medium text-gray-700">Direccion:</label>
      <UInput v-model="thirdSelected.address"
        @change="saveItem(thirdSelected.id, 'address', thirdSelected.address)" />
    </div>
    <div>

      <UButton variant= 'soft' @click="setPassword(thirdSelected.id)" class="w-full">Cambiar Contraseña</UButton>
    </div>
    <!--
    <div v-if="thirdSelected?.type_document != 'NI'">
      <label>
        {{ newthirdSelectedPolices?.length || 0 }} Planes Complemtarios de Salud:
      </label>
      <SelectInsuranceMulti v-model="newthirdSelectedPolices" :third="thirdSelected.id"
        @change="saveItems(thirdSelected.id, newthirdSelectedPolices)" :placeholder="'Paquetes'">
      </SelectInsuranceMulti>
    </div>
  </div>
 
  <div class="mt-4" v-if="thirdSelected.sex_full?.id === 'F'">
    <h3>Maternidad</h3>
    <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
      <div>
        <label class="block text-sm font-medium text-gray-700">Periodo de Lactancia:</label>
        <SelectChoice :choiceType="'MATERNITY_CHOICES'" v-model="thirdSelected.maternity_full"
          @change="saveItem(thirdSelected.id, 'maternity_breasfeeding', thirdSelected.maternity_full.id)" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">Complementaria:</label>
        <SelectChoice :choiceType="'MATERNITY_COMPLEMENTARY_CHOICES'"
          v-model="thirdSelected.maternity_complementary_full"
          @change="saveItem(thirdSelected.id, 'maternity_breasfeeding_complementary', thirdSelected.maternity_complementary_full.id)" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">Extendida:</label>
        <SelectChoice :choiceType="'MATERNITY_EXTEND_CHOICES'" v-model="thirdSelected.maternity_extend_full"
          @change="saveItem(thirdSelected.id, 'maternity_breasfeeding_extend', thirdSelected.maternity_extend_full.id)" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">Embarazo:</label>
        <SelectChoice :choiceType="'MATERNITY_PREGNANCY_CHOICES'" v-model="thirdSelected.maternity_pregnancy_full"
          @change="saveItem(thirdSelected.id, 'maternity_pregnancy', thirdSelected.maternity_pregnancy_full.id)" />
      </div>
      <div>
        <label class="block text-sm font-medium text-gray-700">Violencia:</label>
        <SelectChoice :choiceType="'MATERNITY_VIOLANCE_CHOICES'" v-model="thirdSelected.maternity_violance_full"
          @change="saveItem(thirdSelected.id, 'maternity_violence', thirdSelected.maternity_violance_full.id)" />
      </div>
    </div>
     -->
  </div>

</template>
<script lang="ts" setup>

import Swal from 'sweetalert2';
const toast = useToast()
const emit = defineEmits();

const newthirdSelectedPolices = ref([])
const thirdSelected = ref({} as Third);
const authUserStorage = ref(useAuthUserStorage());
type Third = {
  id: number;
  type: string;
  type_full: any;
  type_document: string;
  type_document_full: any;
  nit: string;
  name: string;
  second_name: string;
  last_name: string;
  second_last_name: string;
  date_birth: string;
  year_old: string;
  sex_full: object;
  city_full: any;
  city_birth_full: any;
  speciality_full: any;
  vehicle_full: any;
  maternity_full: any;
  maternity_complementary_full: any;
  maternity_extend_full: any;
  maternity_pregnancy_full: any;
  maternity_violance_full: any;
  blood_full: any;
  etnia_full: any;
  zone_full: any;
  occupation_full: any;
  status_full: any;
  email: string;
  phone: string;
  profesion: string;
  tp: string;
}

const loadChoices = async () => {
  const value = thirdSelected.value as Third;
  const choices = await Promise.all([
    getCHOICE(value.type, 'TYPE_CHOICES'),
    getCHOICE(value.sex, 'SEX_CHOICES'),
    getCHOICE(value.blood_type, 'BLOOD_CHOICES'),
    getCHOICE(value.ethnicity, 'ETNIAS_CHOICES'),
    getCHOICE(value.zone, 'ZONE_CHOICES'),
    getCHOICE(value.occupation, 'OCCUPATION_CHOICES'),
    getCHOICE(value.status, 'STATUS_CHOICES'),
    getCHOICE(value.maternity_breasfeeding, 'MATERNITY_CHOICES'),
    getCHOICE(value.maternity_breasfeeding_complementary, 'MATERNITY_COMPLEMENTARY_CHOICES'),
    getCHOICE(value.maternity_breasfeeding_extend, 'MATERNITY_EXTEND_CHOICES'),
    getCHOICE(value.maternity_pregnancy, 'MATERNITY_PREGNANCY_CHOICES'),
    getCHOICE(value.maternity_violence, 'MATERNITY_VIOLANCE_CHOICES'),
    getCHOICE(value.type_document, 'TYPE_DOCUMENT_CHOICES'),
  ]);

  thirdSelected.value = {
    ...thirdSelected.value,
    type_full: choices[0],
    sex_full: choices[1],
    blood_full: choices[2],
    etnia_full: choices[3],
    zone_full: choices[4],
    occupation_full: choices[5],
    status_full: choices[6],
    maternity_full: choices[7],
    maternity_complementary_full: choices[8],
    maternity_extend_full: choices[9],
    maternity_pregnancy_full: choices[10],
    maternity_violance_full: choices[11],
    type_document_full: choices[12],
  };
};

await   loadChoices();
alert(JSON.stringify(thirdSelected.value))

const saveItem = async (index: number, field: string, value: string) => {
  authUserStorage.value.third[field] =  value;
  const response = await $fetch(`api/thirds/${index}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
};

const saveItems = async (index: number, injuries: object[]) => {
  try {
    const response = await $fetch<any>(`api/thirds/${index}`);
    const existingPolicys = response.policys;
    const newPolicyIds = injuries.map((policy: any) => policy.id);
    const updatedPolicys = [...new Set([...existingPolicys, ...newPolicyIds])];
    const updatedPolicys2 = updatedPolicys.filter((item) => item !== undefined);

    await $fetch(`api/thirds/${index}`, {
      method: 'PATCH',
      body: JSON.stringify({
        policys: updatedPolicys2,
      }),
    });

    toast.add({ title: `Policys actualizados` });
  } catch (error) {
    toast.add({ title: `Error al actualizar los policys` });
  }
};

onMounted(() => {
  loadChoices();
  thirdSelected.value = authUserStorage.value.third as Third;
});


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

<style></style>
