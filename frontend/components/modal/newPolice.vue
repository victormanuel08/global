<template>
    <UModal>
        <div class="border rounded m-4 " v-if="!isVehicle">
            <div class=" m-4 ">


                <h3>Crear Poliza {{ newTypePolice.name }} {{ props.typeT }}</h3>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4">
                    <div v-if="$props.typeT !== 'D'">
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
                        <UInput v-model="newDescriptionNumber" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Vehiculo: <span
                                @click="showModalVehicle('SE')">➕</span></label>
                        <SelectVehicle v-model="newVehicle" />
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
                    <div>
                        <Label class="block text-sm font-medium text-gray-700">Afectacion Inicial:</label>
                        <UInput v-model="newAmountAffection" />
                    </div>
                </div>

                <div class="flex items-center justify-center mt-4">
                    <span @click="createPolice">💾</span>
                </div>
            </div>
        </div>

        <div class="border rounded m-4 " v-if="isVehicle">
            <div class="m-4">
                <span @click="isVehicle = false">⏪</span>
                <h3>Crear Vehículo</h3>
                <div class="grid grid-cols-2 gap-2 md:grid-cols-2 mt-4">
                    <div class="m-2">
                        <label class="block text-sm font-medium text-gray-700">Placa:</label>
                        <UInput v-model="newVehiclePlate" placeholder="Placa" class="border rounded p-1 w-full" />
                    </div>
                    <div class="m-2">
                        <label class="block text-sm font-medium text-gray-700">Modelo / Movil:</label>
                        <UInput v-model="newVehicleBrand" placeholder="Modelo / Movil"
                            class="border rounded p-1 w-full" />
                    </div>
                </div>
                <div class="m-2">
                    <label class="block text-sm font-medium text-gray-700">Tipo:</label>
                    <SelectChoice :choiceType="'VEHICLE_TYPE_CHOICES'" v-model="newVehicleType"
                        class="border rounded p-1 w-full" />
                </div>
                <div class="flex items-center justify-center mt-4">
                    <span @click="createVehicle">💾</span>
                </div>
            </div>


        </div>

    </UModal>

</template>

<script lang="ts" setup>

const newTypePolice = ref({})
const newThirdEntity = ref({})
const newDescriptionNumber = ref('')
const newVehicle = ref({})
const newDateStart = ref({})
const newDateEnd = ref({})
const newAmountAffection = ref(0)
const newAmountTotal = ref(0)

const isVehicle = ref(false)
const newVehiclePlate = ref('')
const newVehicleBrand = ref('')
const newVehicleType = ref('')
const toast = useToast()

const createVehicle = async () => {
    const response = await $fetch<any>('api/vehicles/', {
        method: 'POST',
        body: {
            plate: newVehiclePlate.value,
            brand: newVehicleBrand.value,
            vehicle_type: newVehicleType.value.id
          
        }
    })
    //alert('Vehiculo creado, cerrar modal')
    toast.add({ title: 'Vehiculo creado' })
    isVehicle.value = false
    newVehicle.value = response
}


type Props = {
    third: object
    typeT: string
}

const props = defineProps<Props>()
watch(() => props.typeT, async () => {

    await validate()
})


const showModalVehicle = (type: string) => {
    //  alert('Crear Vehiculo')
    isVehicle.value = true
}


const createPolice = async () => {
    if (newTypePolice.value.id === "SE") {
        const year = await formatDateYYYY0101(newDateStart.value)
        const valueSOAT = await getVALUE('SE', year)
        if (valueSOAT.results && valueSOAT.results.length > 0) {
            const amount = valueSOAT.results[0].amount;
            newAmountTotal.value = amount;
        } else {
            alert('No se encontro el valor del SOAT en ese año debe agregar el valor en configuracion')
            return
        }

        newAmountTotal.value = valueSOAT.results[0].amount
        console.log('newAmountTotal', newAmountTotal.value)
    }
    const response = await $fetch<any>('api/polices/', {
        method: 'POST',
        body: {
            type_police: newTypePolice.value.id,
            payment_model: 'EV',
            third_entity: newThirdEntity.value.id,
            description: newDescriptionNumber?.value,
            amount_affection: newAmountAffection.value,
            amount_total: newAmountTotal.value,
            vehicle: newVehicle?.value.id,
            date_start: newDateStart.value,
            date_end: newDateEnd.value,
        }
    })
    console.log('PROPS', props)
    const third = await $fetch<any>(`api/thirds/${props.third.id}`);

    third['policys'].push(response.id)

    await $fetch<any>(`api/thirds/${props.third.id}/`, {
        method: 'PUT',
        body: third
    })
    alert('Poliza creada, cerrar modal')
}

const validate = async () => {
    if (props.typeT === 'C') {
        if (newTypePolice.value.id === "SE") {
            if (newThirdEntity.value = props.third) {
                newThirdEntity.value = ''
                newDescriptionNumber.value = ''
                newVehicle.value = ''
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
        newVehicle.value = ''

    }

}



</script>

<style></style>