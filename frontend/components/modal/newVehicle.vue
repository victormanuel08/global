<template>
    <UModal>

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

const isvehicle = ref(false)



type Props = {
    third: object
    typeT: string
}

const props = defineProps<Props>()
watch(() => props.typeT, async () => {

    await validate()
})





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