<template>
    <UModal :third="third" :third2="thirdSelected">
        <div class="border rounded m-4 ">
            <div class=" m-4 ">


                <h3>Crear Poliza</h3>
                <div class="mt-4">
                    <Label class="block text-sm font-medium text-gray-700">Numero:</label>
                    <div class="grid grid-cols-2 gap-2 md:grid-cols-2 ">
                        <UInput v-model="newThirdNit" placeholder="Identificacion" />
                        <SelectChoice :choiceType="'TYPE_DOCUMENT_CHOICES'" v-model="newThirdDocument"
                            @change="validateNit" />
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4" v-if="newThirdDocument?.id !== 'NI'">
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Tipo Poliza:</label>
                        <SelectChoice :choiceType="'SEX_CHOICES'" v-model="newThirdSex" />
                    </div>
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Tipo Pago:</label>
                        <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="newThirdBlood" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Vehiculo: <span @click="showModalVehicle('SE')">➕</span></label>
                        <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="newThirdBlood" />
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4">
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Fecha Inicio:</label>
                        <SelectChoice :choiceType="'SEX_CHOICES'" v-model="newThirdSex" />
                    </div>
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Fecha Fin:</label>
                        <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="newThirdBlood" />
                    </div>
                </div>

                <div class="flex items-center justify-center mt-4">
                    <span @click="createThird">💾</span>
                </div>
            </div>
        </div>
    </UModal>
</template>

<script lang="ts" setup>

const thirdSelected = ref({} as Third[])
const newThirdDocument = ref({})
const newThirdNit = ref('')
const newThirdName = ref('')
const newThirdSecondName = ref('')
const newThirdLastName = ref('')
const newThirdSecondLastName = ref('')
const newThirdBlood = ref({})
const newThirdSex = ref({})

const isvehicle = ref(false)



type Props = {
    third: object
    typeT: string
}

const props = defineProps<Props>()

const typeThird = ref(props.typeT)

const query = ref("")

const showModalVehicle = (value: string) => {
    isvehicle.value = true
    console.log('showModalVehicle', value)
}

watch(() => props.third, async (value: any) => {
    if (value) {
        propEvent(value)
    }
})



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

    console.log('watch1', thirdSelected.value)

}

const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/thirds/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    console.log('saveItem', response)
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
    console.log('createThird', newThirdDocument.value)
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

    newThirdDocument.value = ''
    newThirdNit.value = ''
    newThirdName.value = ''
    newThirdSecondName.value = ''
    newThirdLastName.value = ''
    newThirdSecondLastName.value = ''
    typeThird.value = ''
    newThirdSex.value = ''
    newThirdBlood.value = ''
}


</script>

<style></style>