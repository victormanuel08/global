<template>
    <UModal>
        <div class="border rounded m-4 ">
            <div class=" m-4 ">
                <span :onClick="clear">🧹 Limpiar Campos</span>
                <div v-if="thirdSelected?.id > 0">
                    <h3><strong>Nombre:</strong> {{ thirdSelected?.name }} {{ thirdSelected?.second_name }} {{
                        thirdSelected?.last_name }} {{ thirdSelected?.second_last_name }}</h3>
                    <h3><strong>Identificacion: </strong>{{ thirdSelected?.nit }}</h3>
                    <span v-if="thirdSelected?.type_document != 'NI'">
                        <h3><strong>Edad: </strong>{{ calculateAge(thirdSelected?.date_birth) }}</h3>
                    </span>
                    <h3 v-if="thirdSelected?.user"><strong>Usuario: </strong>{{ thirdSelected?.user }}</h3>

                </div>
                <div v-else>
                    <h3>Crear Tercero {{ props.typeT }} {{ props.typeTA }} </h3>
                    <Label class="block text-sm font-medium text-gray-700">Identificacion:</label>
                    <div class="grid grid-cols-1 gap-2 md:grid-cols-2 mt-4">
                        <div>
                            <UInput v-model="newThirdNit" placeholder="Identificacion" />
                        </div>
                        <div>
                            <SelectChoice :choiceType="'TYPE_DOCUMENT_CHOICES'" v-model="newThirdDocument"
                                @change="validateNit()" />
                        </div>
                    </div>
                    <div class="grid grid-cols-1 gap-2 md:grid-cols-2 mt-4" v-if="newThirdDocument?.id !== 'NI'">
                        <div>
                            <Label class="block text-sm font-medium text-gray-700">Genero:</label>
                            <SelectChoice :choiceType="'SEX_CHOICES'" v-model="newThirdSex" />
                        </div>
                    </div>
                    <div v-if="!thirdSelected?.id || props.typeTA === 'A'"
                        :class="newThirdDocument?.id === 'NI' ? 'grid grid-cols-1 gap-2 md:grid-cols-1' : 'grid grid-cols-1 gap-2 md:grid-cols-2'">

                        <!--
                    <div
                        :class="newThirdDocument?.id === 'NI' ? 'grid grid-cols-1 gap-2 md:grid-cols-1' : 'grid grid-cols-4 gap-2 md:grid-cols-4'">
                    -->
                        <label class="block text-sm font-medium text-gray-700">Nombre Completo:</label>
                        <div></div>
                        <div>
                            <UInput v-model="newThirdName"
                                :placeholder="newThirdDocument?.id === 'NI' ? 'Razón Social' : 'Primer Nombre'" />
                        </div>
                        <div>
                            <UInput v-model="newThirdSecondName" placeholder="Segundo Nombre"
                                v-if="newThirdDocument?.id !== 'NI'" />
                        </div>
                        <div>
                            <UInput v-model="newThirdLastName" placeholder="Primer Apellido"
                                v-if="newThirdDocument?.id !== 'NI'" />
                        </div>
                        <div>
                            <UInput v-model="newThirdSecondLastName" placeholder="Segundo Apellido"
                                v-if="newThirdDocument?.id !== 'NI'" />
                        </div>
                    </div>
                    <div class="grid grid-cols-1 gap-2 md:grid-cols-2 mt-4" v-if="newThirdDocument?.id !== 'NI'">
                        <div hidden>
                            <Label class="block text-sm font-medium text-gray-700">Tipo Sangre:</label>
                            <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="newThirdBlood" />
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700">Estado:</label>
                            <SelectChoice :choiceType="'STATUS_CHOICES'" v-model="newThirdSelectedStatus_full" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Fecha Nacimiento:</label>
                            <UInput type="date" v-model="newThirdSelectedDate_birth" />
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700">Ocupacion:</label>
                            <SelectChoice :choiceType="'OCCUPATION_CHOICES'"
                                v-model="newThirdSelectedOccupation_full" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Profesion:</label>
                            <UInput  v-model="newThirdSelectedProfesion" />
                        </div>
                    </div>

                </div>
                <div v-if="!thirdSelected?.id">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                        <UInput v-model="newThirdSelectedAddress" />
                    </div>
                </div>
                <div class="grid grid-cols-1 gap-2 md:grid-cols-2 mt-4" v-if="newThirdDocument?.id !== 'NI'">
                    <div v-if="thirdSelected.type_full?.id === 'M' || props.typeT === 'M'"  >
                        <label class="block text-sm font-medium text-gray-700">Especialidad:</label>
                        <SelectSpecialities v-model="thirdSelected.speciality_full"
                            @change="saveItem(thirdSelected.id, 'speciality', thirdSelected.speciality_full.id)" />
                    </div>
                    <div v-if="thirdSelected.type_full?.id === 'M' || props.typeT === 'M'" >
                        <label class="block text-sm font-medium text-gray-700">T.P.:</label>
                        <UInput v-model="thirdSelected.tp"
                            @change="saveItem(thirdSelected.id, 'tp', thirdSelected.tp)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Telefono:</label>
                        <UInput v-model="newThirdSelectedPhone" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Zona:</label>
                        <SelectChoice :choiceType="'ZONE_CHOICES'" v-model="newthirdSelectedZone_full" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Ciudad actual:</label>
                        <SelectCities v-model="newThirdSelectedCity_full" />
                    </div>
                </div>


                <div v-if="!thirdSelected?.id">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Correo:</label>
                        <UInput v-model="newThirdSelectedEmail" />
                    </div>
                </div>

                <div v-if="!thirdSelected?.id">
                    <div class="flex items-center justify-center mt-4">
                        <span @click="createNewThird">💾</span>
                    </div>
                </div>

            </div>
            <div class="grid grid-cols-2 gap-4 md:grid-cols-2 m-4"
                v-if="thirdSelected?.id > 0 && thirdSelected?.nit !== '222222222222'">
                <div>
                    <label class="block text-sm font-medium text-gray-700">Tipo:</label>
                    <SelectChoice :choiceType="'TYPE_CHOICES'" v-model="thirdSelected.type_full"
                        @change="saveItem(thirdSelected.id, 'type', thirdSelected.type_full.id)" />
                </div>


            </div>
            <div class="grid grid-cols-2 gap-4 md:grid-cols-2 m-4"
                v-if="thirdSelected?.id > 0 && thirdSelected?.type_document !== 'NI' && thirdSelected?.type_document !== 'AS'">
                <div v-if="thirdSelected.type_full?.id === 'M' || props.typeT === 'M'">
                    <label class="block text-sm font-medium text-gray-700">Especialidad:</label>
                    <SelectSpecialities v-model="thirdSelected.speciality_full"
                        @change="saveItem(thirdSelected.id, 'speciality', thirdSelected.speciality_full.id)" />
                </div>
                <div v-if="thirdSelected.type_full?.id === 'M' || props.typeT === 'M'">
                    <label class="block text-sm font-medium text-gray-700">T.P.:</label>
                    <UInput v-model="thirdSelected.tp" @change="saveItem(thirdSelected.id, 'tp', thirdSelected.tp)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Sexo:</label>
                    <SelectChoice :choiceType="'SEX_CHOICES'" v-model="thirdSelected.sex_full"
                        @change="saveItem(thirdSelected.id, 'sex', thirdSelected.sex_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Ciudad Natal:</label>
                    <SelectCities v-model="thirdSelected.city_birth_full"
                        @change="saveItem(thirdSelected.id, 'city_birth', thirdSelected.city_birth_full.id)" />
                </div>


                <div>
                    <label class="block text-sm font-medium text-gray-700">Tipo Sangre:</label>
                    <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="thirdSelected.blood_full"
                        @change="saveItem(thirdSelected.id, 'blood_type', thirdSelected.blood_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Etnia:</label>
                    <SelectChoice :choiceType="'ETNIAS_CHOICES'" v-model="thirdSelected.etnia_full"
                        @change="saveItem(thirdSelected.id, 'ethnicity', thirdSelected.etnia_full.id)" />
                </div>


                <div>
                    <label class="block text-sm font-medium text-gray-700">Vehiculo:</label>
                    <SelectVehicle v-model="thirdSelected.vehicle_full"
                        @change="saveItem(thirdSelected.id, 'vehicle', thirdSelected.vehicle_full.id)" />
                </div>



            </div>
            <div class="mt-4" v-if="thirdSelected.sex_full?.id === 'F' && thirdSelected?.id > 0">
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
                        <SelectChoice :choiceType="'MATERNITY_EXTEND_CHOICES'"
                            v-model="thirdSelected.maternity_extend_full"
                            @change="saveItem(thirdSelected.id, 'maternity_breasfeeding_extend', thirdSelected.maternity_extend_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Embarazo:</label>
                        <SelectChoice :choiceType="'MATERNITY_PREGNANCY_CHOICES'"
                            v-model="thirdSelected.maternity_pregnancy_full"
                            @change="saveItem(thirdSelected.id, 'maternity_pregnancy', thirdSelected.maternity_pregnancy_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Violencia:</label>
                        <SelectChoice :choiceType="'MATERNITY_VIOLANCE_CHOICES'"
                            v-model="thirdSelected.maternity_violance_full"
                            @change="saveItem(thirdSelected.id, 'maternity_violence', thirdSelected.maternity_violance_full.id)" />
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-1 gap-4 md:grid-cols-1 m-4"
                v-if="thirdSelected?.id > 0 && thirdSelected?.nit !== '222222222222'">
                <div v-if="thirdSelected?.type_document != 'NI'">
                    <label>
                        {{ newthirdSelectedPolices?.length || 0 }} Planes Complemtarios de Salud:
                    </label>
                    <SelectInsuranceMulti v-model="newthirdSelectedPolices" :third="thirdSelected.id"
                        @change="saveItems(thirdSelected.id, newthirdSelectedPolices)" :placeholder="'Paquetes'">
                    </SelectInsuranceMulti>

                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Correo:</label>
                    <UInput v-model="thirdSelected.email"
                        @change="saveItem(thirdSelected.id, 'email', thirdSelected.email)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                    <UInput v-model="thirdSelected.address"
                        @change="saveItem(thirdSelected.id, 'address', thirdSelected.address)" />
                </div>
            </div>
        </div>
    </UModal>

</template>
<script lang="ts" setup>

import { useThirdObject } from '~/stores/thirds';



const toast = useToast()
const newthirdSelectedPolices = ref([])
const thirdSelected = ref({} as Third);
const newThirdDocument = ref({})
const newThirdNit = ref('')
const newThirdName = ref('')
const newThirdSecondName = ref('')
const newThirdLastName = ref('')
const newThirdSecondLastName = ref('')
const newThirdBlood = ref({})
const newThirdSex = ref({})
const newThirdType = ref('')
const isPolice = ref(false)
const newThirdSelectedStatus_full = ref({})
const newThirdSelectedDate_birth = ref('')
const newThirdSelectedOccupation_full = ref({})
const newThirdSelectedAddress =  ref('')
const newThirdSelectedPhone =  ref('')
const newthirdSelectedZone_full = ref({})
const newThirdSelectedCity_full = ref({})
const newThirdSelectedEmail =  ref('')
const newThirdSelectedProfesion =  ref('')
const emit = defineEmits();

const showModalPolice = () => {
    isPolice.value = true
}

const handleModalClose = async (value: any) => {
    isPolice.value = false
}

type Props = {
    third?: object
    typeT?: string
    typeTA?: string
}

const props = defineProps<Props>()

const typeThird = ref(props.typeT)

const query = ref("")

const clear = () => {
    thirdSelected.value = ''
}

watch(() => props.third, async (value: any) => {
    if (value) {
        newThirdNit.value = ''
        newThirdDocument.value = ''
        propEvent(value)
    }
})

watch(() => props.typeT, async (value: any) => {
    newThirdType.value = await getCHOICE(value, 'TYPE_CHOICES')
    if (value === 'E' || value === 'C') {
        newThirdDocument.value = await getCHOICE('NI', 'TYPE_DOCUMENT_CHOICES')
    } else {
        newThirdDocument.value = await getCHOICE('CC', 'TYPE_DOCUMENT_CHOICES')
    }
    newThirdType.value = await getCHOICE(value, 'TYPE_CHOICES')
})

const propEvent = async (value: any) => {
    thirdSelected.value = value
    thirdSelected.value.type_full = await getCHOICE(value.type, 'TYPE_CHOICES')
    thirdSelected.value.sex_full = await getCHOICE(value.sex, "SEX_CHOICES")
    thirdSelected.value.blood_full = await getCHOICE(value.blood_type, "BLOOD_CHOICES")
    thirdSelected.value.etnia_full = await getCHOICE(value.ethnicity, "ETNIAS_CHOICES")
    thirdSelected.value.zone_full = await getCHOICE(value.zone, "ZONE_CHOICES")
    thirdSelected.value.occupation_full = await getCHOICE(value.occupation, "OCCUPATION_CHOICES")
    thirdSelected.value.status_full = await getCHOICE(value.status, "STATUS_CHOICES")
    thirdSelected.value.maternity_full = await getCHOICE(value.maternity_breasfeeding, "MATERNITY_CHOICES")
    thirdSelected.value.maternity_complementary_full = await getCHOICE(value.maternity_breasfeeding_complementary, "MATERNITY_COMPLEMENTARY_CHOICES")
    thirdSelected.value.maternity_extend_full = await getCHOICE(value.maternity_breasfeeding_extend, "MATERNITY_EXTEND_CHOICES")
    thirdSelected.value.maternity_pregnancy_full = await getCHOICE(value.maternity_pregnancy, "MATERNITY_PREGNANCY_CHOICES")
    thirdSelected.value.maternity_violance_full = await getCHOICE(value.maternity_violence, "MATERNITY_VIOLANCE_CHOICES")
    thirdSelected.value.type_document_full = await getCHOICE(value.type_document, "TYPE_DOCUMENT_CHOICES")
    thirdSelected.value.status_full = await getCHOICE(value.state, "STATUS_CHOICES")
    thirdSelected.value.occupation_full = await getCHOICE(value.occupation, "OCCUPATION_CHOICES")
    thirdSelected.value.zone_full = await getCHOICE(value.zone, "ZONE_CHOICES")
    typeThird.value = props.typeT
}

const saveItem = async (index: number, field: string, value: string) => {
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

const validateNit = async () => {
    const queryParams = {
        search: query.value,
        nit: newThirdNit?.value,
        type_document: newThirdDocument.value.id
    }

    if (newThirdNit.value !== '') {
        const response = await $fetch<any>("api/thirds", {
            query: queryParams
        })

        if (response.results.length > 0) {
            propEvent(response.results[0])
            toast.add({ title: `El tercero ya existe` });
            // Emitir el tercero creado y cerrar la modal
            emit('thirdCreated', response.results[0]);  // Emitir el tercero creado
            emit('update:isThird', false);   // Cerrar la modal
        }
    } else {
        alert('El campo de identificacion no puede estar vacio')
    }
}



const createNewThird = async () => {
    const message = confirm('¿Estás seguro de crear este Tercero?');

    if (!message) {
        newThirdDocument.value = '';
        newThirdNit.value = '';
        newThirdName.value = '';
        newThirdSecondName.value = '';
        newThirdLastName.value = '';
        newThirdSecondLastName.value = '';
        typeThird.value = '';
        newThirdSex.value = '';
        newThirdBlood.value = '';
        newThirdSelectedStatus_full.value = '';
        newThirdSelectedDate_birth.value = '';
        newThirdSelectedOccupation_full.value = '';
        newThirdSelectedAddress.value = '';
        newThirdSelectedPhone.value = '';
        newthirdSelectedZone_full.value = '';
        newThirdSelectedCity_full.value = '';
        newThirdSelectedEmail.value = '';
        return;
    }

    if (typeThird.value === 'E' || typeThird.value === 'C') {
        newThirdDocument.value.id = 'NI';
        newThirdType.value = await getCHOICE(typeThird.value, 'TYPE_CHOICES');
    }

    validateNit();

    const consult: { results: any[] } = await $fetch('api/thirds/', {
        query: {
            nit: newThirdNit.value,
            type_document: newThirdDocument.value.id
        }
    });

    if (consult.results.length > 0) {
   
        toast.add({ title: `El tercero ya existe` });
            // Emitir el tercero creado y cerrar la modal
        emit('thirdCreated', consult.results[0]);  // Emitir el tercero creado
        emit('update:isThird', false);   // Cerrar la modal
        
    }
    if (newThirdSelectedDate_birth.value === '' && newThirdDocument.value.id !== 'NI') {
        alert('La fecha de nacimiento no puede estar vacia');
        return;
    }
    if (newThirdSelectedDate_birth.value === '' && newThirdDocument.value.id === 'NI') {
        newThirdSelectedDate_birth.value = '1900-01-01'
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
            type: newThirdType.value.id,
            blood_type: newThirdBlood.value.id,
            sex: newThirdSex.value.id,
            status: newThirdSelectedStatus_full.value.id,            
            occupation: newThirdSelectedOccupation_full.value.id,
            profesion: newThirdSelectedProfesion.value,
            address: newThirdSelectedAddress.value,
            phone: newThirdSelectedPhone.value,
            zone: newthirdSelectedZone_full.value.id,
            city: newThirdSelectedCity_full.value.id,
            email: newThirdSelectedEmail.value,
            date_birth: newThirdSelectedDate_birth.value
        }
    });

    // Limpiar los valores después de crear el tercero
    newThirdDocument.value = '';
    newThirdNit.value = '';
    newThirdName.value = '';
    newThirdSecondName.value = '';
    newThirdLastName.value = '';
    newThirdSecondLastName.value = '';

    toast.add({ title: `Tercero creado` });

    // Emitir el tercero creado y cerrar la modal
    emit('thirdCreated', response);  // Emitir el tercero creado
    emit('update:isThird', false);   // Cerrar la modal
};



onMounted(async () => {
    console.log('third?¿', thirdSelected.value)
    if (props.typeT === 'E' || props.typeT === 'C') {
        newThirdDocument.value = await getCHOICE('NI', 'TYPE_DOCUMENT_CHOICES')
    } else {
        newThirdDocument.value = await getCHOICE('CC', 'TYPE_DOCUMENT_CHOICES')
        newThirdSex.value = await getCHOICE('M', 'SEX_CHOICES')
    }

    newThirdType.value = await getCHOICE(props.typeT, 'TYPE_CHOICES')
})

</script>

<style></style>
