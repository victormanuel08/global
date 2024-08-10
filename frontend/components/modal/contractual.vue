<template>
    <UModal>
        <UCard class="m-6">

            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                
                <div class="felx flex-auto gap-4 ">  
                    <h3 class="text-lg font-bold"> <p :style="{ color: props.fee?.policy_full?.amount_total < (amount_records + props.fee?.amount) ? 'red' : 'black' }">Servicio {{ props.fee?.description }} ${{ props.fee?.amount }}</p></h3>                                   
                </div>

            </div>
            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                <h3 class="text-lg font-bold">Contrato {{ props.fee?.third_entity_full?.name }} </h3>
                <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                    <div>
                        <h3 class="text-lg font-bold">Nombre</h3>
                        <p>{{ props.fee.policy_full?.name }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Valor</h3>
                        <p :style="{ color: props.fee?.policy_full?.amount_total < amount_records ? 'red' : 'black' }">{{ props?.fee.policy_full?.amount_total }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Tipo</h3>
                        <p>{{ police?.name}}</p>
                    </div>

                </div>
                <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                    <div>
                        <h3 class="text-lg font-bold">Inicio</h3>
                        <p>{{ props.fee?.policy_full?.date_start }}</p>
                        <UInput type="date" v-if="!props.fee?.policy_full?.date_start"/>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Fin</h3>
                        <p>{{ props.fee?.policy_full?.date_end }}</p>
                        <UInput type="date" v-if="!props.fee?.policy_full?.date_end"/>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Pago</h3>
                        <p>{{  payment?.name }}</p>
                    </div>

                </div>
            </div>
            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2" >
                <h3 class="text-lg font-bold">Consumo Historias Medicas</h3>
                <div class="grid grid-cols-2 gap-4 md:grid-cols-2">
                    <div>
                        <h3 class="text-lg font-bold">Eventos</h3>{{records?.length }}
                        
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Valor: $</h3>{{ amount_records }}
                        
                    </div>
                </div>
            </div>
            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                <h3 class="text-lg font-bold">Posible Consumo Citas Agendadas</h3>
                <div class="grid grid-cols-2 gap-4 md:grid-cols-2">
                    <div>
                        <h3 class="text-lg font-bold">Eventos</h3>
                        <p>{{  }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Valor</h3>
                        <p>{{  }}</p>
                    </div>
                </div>
            </div>
        </UCard>
    </UModal>
</template>
<script setup lang="ts">

type Props = {
    fee: any
}


const props = defineProps<Props>()
const records = ref<any[]>([])
const query = ref<any>("")
const amount_records = ref(0)
const payment = ref({}as any)
const police = ref({}as any)


// payment.value = await getCHOICE(props.fee.policy_full?.payment_model, 'PAYMENT_MODEL_CHOICES')
// police.value =   await getCHOICE(props.fee.policy_full?.type_police, 'TYPE_POLICE_CHOICES')

watch(() => props.fee, async (newVal, oldVal) => {
    console.log("PROPS", props.fee)
    if (props.fee.description==='Contrato SOAT') {
        return
    }else{
        payment.value = await getCHOICE(newVal.policy_full?.payment_model, 'PAYMENT_MODEL_CHOICES')
    police.value =   await getCHOICE(newVal.policy_full?.type_police, 'TYPE_POLICE_CHOICES')
    await recordsPolicy()
    }

})

const recordsPolicy = async () => {
    const queryParams = {
        search: query.value,
        policy: props?.fee.policy,
    }

    const response = await $fetch<any>("api/records", {
        query: queryParams
    })
    records.value = response.results 
    //amount_records.value = records.value.map((record:any) => record.fee_full.amount).reduce((a:any, b:any) => a + b, 0);
    amount_records.value = records.value.map((record) => record.fee_full?.amount).map(Number).reduce((a, b) => a + b, 0);
    console.log("RECORDSPOLICYS", records.value)  
}


</script>
<style scoped></style>
