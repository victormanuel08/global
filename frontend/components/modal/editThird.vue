<template>
    <UModal @close="modalClosedHandler(thirdSelected)">
        <div class="border rounded m-4 ">
            <div class=" m-4 ">
                <div v-if="thirdSelected?.id > 0">
                    <h3><strong>Nombre:</strong> {{ thirdSelected?.name }} {{ thirdSelected?.second_name }} {{
                        thirdSelected?.last_name }} {{ thirdSelected?.second_last_name }}</h3>
                    <h3><strong>Identificacion: </strong>{{ thirdSelected?.nit }}</h3>
                    <h3><strong>Usuario: </strong>{{ thirdSelected?.user }}</h3>

                </div>
                <div v-else>
                    <h3>Crear Tercero {{ props.typeT }}</h3>
                    <div class="mt-4">
                        <Label class="block text-sm font-medium text-gray-700">Identificacion:</label>
                        <div class="grid grid-cols-2 gap-2 md:grid-cols-2 ">
                            <UInput v-model="newThirdNit" placeholder="Identificacion" />
                            <SelectChoice :choiceType="'TYPE_DOCUMENT_CHOICES'" v-model="newThirdDocument"
                                @change="validateNit" />
                        </div>
                    </div>
                    <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4" v-if="newThirdDocument?.id !== 'NI'">
                        <div>
                            <Label class="block text-sm font-medium text-gray-700">Genero:</label>
                            <SelectChoice :choiceType="'SEX_CHOICES'" v-model="newThirdSex" />
                        </div>
                        <div>
                            <Label class="block text-sm font-medium text-gray-700">Tipo Sangre:</label>
                            <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="newThirdBlood" />
                        </div>
                    </div>
                </div>
                <div v-if="!thirdSelected?.id" class="mt-4">
                    <label class="block text-sm font-medium text-gray-700">Nombre Completo:</label>
                    <div
                        :class="newThirdDocument?.id === 'NI' ? 'grid grid-cols-1 gap-2 md:grid-cols-1' : 'grid grid-cols-4 gap-2 md:grid-cols-4'">
                        <UInput v-model="newThirdName"
                            :placeholder="newThirdDocument?.id === 'NI' ? 'Razón Social' : 'Primer Nombre'" />
                        <UInput v-model="newThirdSecondName" placeholder="Segundo Nombre"
                            v-if="newThirdDocument?.id !== 'NI'" />
                        <UInput v-model="newThirdLastName" placeholder="Primer Apellido"
                            v-if="newThirdDocument?.id !== 'NI'" />
                        <UInput v-model="newThirdSecondLastName" placeholder="Segundo Apellido"
                            v-if="newThirdDocument?.id !== 'NI'" />
                    </div>
                    <div class="flex items-center justify-center mt-4">
                        <span @click="createThird">💾</span>
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-3 gap-4 md:grid-cols-3 mt-4"
                v-if="thirdSelected?.id > 0 && newThirdDocument?.id !== 'NI'">
                <div>
                    <label class="block text-sm font-medium text-gray-700">Tipo:</label>
                    <SelectChoice :choiceType="'TYPE_CHOICES'" v-model="thirdSelected.type_full"
                        @change="saveItem(thirdSelected.id, 'type', thirdSelected.type_full.id)" />
                </div>
                <div v-if="thirdSelected.type_full?.id === 'M'">
                    <label class="block text-sm font-medium text-gray-700">Especialidad:</label>
                    <SelectSpecialities v-model="thirdSelected.speciality_full"
                        @change="saveItem(thirdSelected.id, 'speciality', thirdSelected.speciality_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Ciudad Natal:</label>
                    <SelectCities v-model="thirdSelected.city_birth_full"
                        @change="saveItem(thirdSelected.id, 'city_birth', thirdSelected.city_birth_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Fecha Nacimiento:</label>
                    <UInput type="date" v-model="thirdSelected.date_birth"
                        @change="saveItem(thirdSelected.id, 'date_birth', thirdSelected.date_birth)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Ciudad actual:</label>
                    <SelectCities v-model="thirdSelected.city_full"
                        @change="saveItem(thirdSelected.id, 'city', thirdSelected.city_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Sexo:</label>
                    <SelectChoice :choiceType="'SEX_CHOICES'" v-model="thirdSelected.sex_full"
                        @change="saveItem(thirdSelected.id, 'sex', thirdSelected.sex_full.id)" />
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
                    <label class="block text-sm font-medium text-gray-700">Zona:</label>
                    <SelectChoice :choiceType="'ZONE_CHOICES'" v-model="thirdSelected.zone_full"
                        @change="saveItem(thirdSelected.id, 'zone', thirdSelected.zone_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Ocupacion:</label>
                    <SelectChoice :choiceType="'OCCUPATION_CHOICES'" v-model="thirdSelected.occupation_full"
                        @change="saveItem(thirdSelected.id, 'occupation', thirdSelected.occupation_full.id)" />
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700">Telefono:</label>
                    <UInput v-model="thirdSelected.phone"
                        @change="saveItem(thirdSelected.id, 'phone', thirdSelected.phone)" />
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
            <div class="grid grid-cols-1 gap-4 md:grid-cols-1 mt-4" v-if="thirdSelected?.id > 0">
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

const { thirdObject } = useThirdObject();


const thirdSelected = ref({} as Third);
const newThirdDocument = ref({})
const newThirdNit = ref('')
const newThirdName = ref('')
const newThirdSecondName = ref('')
const newThirdLastName = ref('')
const newThirdSecondLastName = ref('')
const newThirdBlood = ref({})
const newThirdSex = ref({})



type Props = {
    third: object
    typeT: string

}

const props = defineProps<Props>()

const typeThird = ref(props.typeT)

const query = ref("")




watch(() => props.third, async (value: any) => {
    if (value) {
        newThirdNit.value = ''
        newThirdDocument.value = ''
        propEvent(value)
    }
})

if (typeThird.value === 'E' || typeThird.value === 'C') {
    newThirdDocument.value = await getCHOICE('NI', 'TYPE_DOCUMENT_CHOICES')
}


const propEvent = async (value: any) => {
    thirdSelected.value = value
    thirdSelected.value.type_full = await getCHOICE(value.type, 'TYPE_CHOICES')
    thirdSelected.value.sex_full = await getCHOICE(value.sex, "SEX_CHOICES")
    thirdSelected.value.blood_full = await getCHOICE(value.blood_type, "BLOOD_CHOICES")
    thirdSelected.value.etnia_full = await getCHOICE(value.ethnicity, "ETNIAS_CHOICES")
    thirdSelected.value.zone_full = await getCHOICE(value.zone, "ZONE_CHOICES")
    thirdSelected.value.occupation_full = await getCHOICE(value.occupation, "OCCUPATION_CHOICES")
    thirdSelected.value.maternity_full = await getCHOICE(value.maternity_breasfeeding, "MATERNITY_CHOICES")
    thirdSelected.value.maternity_complementary_full = await getCHOICE(value.maternity_breasfeeding_complementary, "MATERNITY_COMPLEMENTARY_CHOICES")
    thirdSelected.value.maternity_extend_full = await getCHOICE(value.maternity_breasfeeding_extend, "MATERNITY_EXTEND_CHOICES")
    thirdSelected.value.maternity_pregnancy_full = await getCHOICE(value.maternity_pregnancy, "MATERNITY_PREGNANCY_CHOICES")
    thirdSelected.value.maternity_violance_full = await getCHOICE(value.maternity_violence, "MATERNITY_VIOLANCE_CHOICES")
    thirdSelected.value.type_document_full = await getCHOICE(value.type_document, "TYPE_DOCUMENT_CHOICES")
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

const validateNit = async () => {

    const queryParams = {
        search: query.value,
        nit: newThirdNit.value,
        type_document: newThirdDocument.value.id
    }
    const response = await $fetch<any>("api/thirds", {
        query: queryParams
    })
    if (response.results.length > 0) {
        propEvent(response.results[0])
    }

}

const createThird = async () => {

    const message = confirm('¿Estás seguro de crear este Tercero?')

    if (!message) {
        newThirdDocument.value = ''
        newThirdNit.value = ''
        newThirdName.value = ''
        newThirdSecondName.value = ''
        newThirdLastName.value = ''
        newThirdSecondLastName.value = ''
        typeThird.value = ''
        newThirdSex.value = ''
        newThirdBlood.value = ''

        return
    }
    if (typeThird.value === 'E') {
        newThirdDocument.value.id = 'NI'
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
            type: typeThird.value,
            blood_type: newThirdBlood.value.id,
            sex: newThirdSex.value.id
        },
    })

    validateNit()

}


const modalClosedHandler = (thirdSelected: any) => {
 
    thirdObject.value = thirdSelected
}


</script>

<style></style>