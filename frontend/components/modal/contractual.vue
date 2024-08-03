<template>
    <UModal>
        <UCard class="m-6">

            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                <h3 class="text-lg font-bold">Servicio {{ props?.fee.description }}</h3>
                <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                    <div>
                        <h3 class="text-lg font-bold">Evento</h3>
                        <p>1</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Valor</h3>
                        <p>{{ props?.fee.amount }}</p>
                    </div>
                    <div></div>
                </div>
                <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                    <div>
                        <h3 class="text-lg font-bold">Eventos Contrato</h3>
                        <p>{{ records.length }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Saldo Usado</h3>
                        <p>{{ amount_records }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Saldo  Proyectado</h3>
                        <p>{{  }}</p>
                    </div>
                </div>
            </div>
            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                <h3 class="text-lg font-bold">Contrato {{ props.fee.third_entity_full.name }} ${{
                    props.fee.policy_full.amount_total }}</h3>
                <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                    <div>
                        <h3 class="text-lg font-bold">Nombre</h3>
                        <p>{{ props?.fee.policy_full.name }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Valor</h3>
                        <p>{{ props?.fee.policy_full.name }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Tipo</h3>
                        <p>{{ props?.fee.policy_full.type_police_full.name }}</p>
                    </div>

                </div>
                <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                    <div>
                        <h3 class="text-lg font-bold">Inicio</h3>
                        <p>{{ props?.fee.policy_full.date_start }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Fin</h3>
                        <p>{{ props?.fee.policy_full.date_end }}</p>
                    </div>
                    <div>
                        <h3 class="text-lg font-bold">Pago</h3>
                        <p>{{ props?.fee.policy_full.payment_model_full.name }}</p>
                    </div>

                </div>
            </div>
            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                <h3 class="text-lg font-bold">Consumo</h3>
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
            <div class=" border-solid border-2 border-gray-200 rounded-lg p-2 mt-2">
                <h3 class="text-lg font-bold">Posible Consumo</h3>
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
const amount_records = ref('')
props.fee.policy_full.payment_model_full = await getCHOICE(props.fee.policy_full?.payment_model, 'PAYMENT_MODEL_CHOICES')
props.fee.policy_full.type_police_full = await getCHOICE(props.fee.policy_full?.type_police, 'TYPE_POLICE_CHOICES')

const recordsPolicy = async () => {
    const queryParams = {
        search: query.value,
        policy: props?.fee.policy,
    }

    const response = await $fetch<any>("api/records", {
        query: queryParams
    })
    records.value = response.results 
    amount_records.value = records.value.map((record: any) => record.fee_full.amount).reduce((a: any, b: any) => a + b, 0)
    console.log("RECORDSPOLICYS", records.value)  
}

onMounted(() => {
    recordsPolicy()
})

</script>
<style scoped></style>
