<template>
    <UModal>
        <div class="border rounded m-4 ">
            <div class=" m-4 ">


                <h3>Crear Poliza {{ newTypePolice.name }}</h3>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4">
                    <div v-if="$props.typeT !=='D'">
                        <Label class="block text-sm font-medium text-gray-700">Tipo Poliza:</label>
                        <SelectChoice :choiceType="'TYPE_POLICE_CHOICES'" v-model="newTypePolice" @change="validate" />
                    </div>
                    <div v-if="newTypePolice.id === 'SE'">
                        <Label class="block text-sm font-medium text-gray-700">Entidad:</label>
                        <SelectThird v-model="newThirdEntity" :third-type="'E'" :third="props.third"
                            :police-type="newTypePolice.id" class="border rounded p-1">
                        </SelectThird>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4" v-if="newTypePolice.id === 'SE'">

                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Numero:</label>
                        <SelectChoice :choiceType="'TYPE_POLICE_CHOICES'" v-model="newDescriptionNumber"
                            @change="validate" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Vehiculo: <span
                                @click="showModalVehicle('SE')">➕</span></label>
                        <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="newVehicle" />
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4" v-if="newTypePolice.id === 'SE'">
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Fecha Inicio:</label>
                        <UInput type="date" v-model="newDateStart" />
                    </div>
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Fecha Fin:</label>
                        <UInput type="date" v-model="newDateEnd" />
                    </div>
                </div>

                <div class="flex items-center justify-center mt-4">
                    <span @click="createPolice">💾</span>
                </div>
            </div>
        </div>
    </UModal>
</template>

<script lang="ts" setup>

const newTypePolice = ref({})
const newThirdEntity = ref({})
const newDescriptionNumber = ref({})
const newVehicle = ref({})
const newDateStart = ref({})
const newDateEnd = ref({})

const isvehicle = ref(false)



type Props = {
    third: object
    typeT: string
}

const props = defineProps<Props>()

const createPolice = async () => {


    const response = await $fetch<any>('api/polices/', {
        method: 'POST',
        body: {
            type_police: newTypePolice.value.id,
            payment_model: 'EV',
            third_entity: newThirdEntity.value.id,
            description: newDescriptionNumber.value,
            vehicle: newVehicle?.value.id,
            date_start: newDateStart.value,
            date_end: newDateEnd.value,
        }
    })
    const third = await $fetch<any>(`api/thirds/${props.third.id}`);

    third['policys'].push(response.id)

    await $fetch<any>(`api/thirds/${props.third.id}/`, {
        method: 'PUT',
        body: third
    })
    alert('Poliza creada, cerrar modal')
}

const validate = async() => {
    if (props.typeT === 'C') {
        if (newTypePolice.value.id === "SE") {
            if (newThirdEntity.value = props.third) {
                newThirdEntity.value = ''
                newDescriptionNumber.value = ''
            }
        } else if (newTypePolice.value.id === "PA") {
            newThirdEntity.value = props.third
            newDescriptionNumber.value = props.third?.nit
            newDateStart.value = getCurrentDate()
            newDateEnd.value = formatDateYYYYMMDD('2050-12-31')
        } else {
            alert('Solo puede crear polizas Particular y Soat')
            newTypePolice.value = ''
            newThirdEntity.value = ''
            newDescriptionNumber.value = ''
            newVehicle.value = ''
            newDateStart.value = ''
            newDateEnd.value = ''
        }
    } else if (props.typeT === 'D') {
        newTypePolice.value = await getCHOICE('SE', 'TYPE_POLICE_CHOICES')

        newThirdEntity.value = ''
        newDescriptionNumber.value = ''

    } 
}

</script>

<style></style>