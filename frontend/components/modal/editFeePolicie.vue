<template>

    <div class="max-w-5xl mx-auto">
        <UCard class="my-2">
            <template #header>
                <div class="flex justify-between items-center">
                    <h2 class="font-bold">Tarifas {{ props.calendarEvent?.description }} - {{
                        props.calendarEvent?.third_entity_full?.name }}</h2>
                    <div class="flex gap-3 my-3">
                        <input ref="fileInput" type="file" accept=".txt" @change="uploadListFile" class="hidden" />
                        <UButton variant="soft" @click="triggerFileInput" class="round-button large-icon">
                            Cargar Archivo</UButton>
                        <UInput v-model="search" placeholder="Buscar" />
                        <UPagination v-model="pagination.page" :page-count="pagination.pageSize"
                            :total="pagination.resultsCount" />
                    </div>
                </div>
            </template>
            <div class="flex justify-center items-center">
                <h3 v-if="fees.length === 0">No hay Tarifas para el Contrato </h3>
            </div>
            <div style="overflow: auto;">
                <table class="table-auto w-full permission-table">
                    <thead>
                        <tr>
                            <th :class="ui.th">Especialidad</th>
                            <th :class="ui.th">Servicio</th>
                            <th :class="ui.th">Valor</th>
                            <th :class="ui.th">Acciones</th>

                        </tr>
                    </thead>
                    <tbody>

                        <tr v-for="(fee, index) in fees" :key="index">
                            <td :class="ui.td">
                                <div class="grid grid-flow-row justify-left">
                                    <span>{{ fee.service_full.speciality_full.description }}</span>
                                </div>
                            </td>

                            <td :class="ui.td">
                                <div class="grid grid-flow-row justify-left">
                                    <span>{{ fee.service_full.description }}</span>
                                </div>
                            </td>


                            <td :class="ui.td">
                                <div class="grid grid-flow-row justify-center">
                                    {{ fee.amount }}

                                </div>
                            </td>



                            <td :class="ui.td">
                                <div class="flex items-center justify-center">

                                    <span @click="deleteFees(fee.id)" :class="ui.span">🗑️</span>
                                </div>
                            </td>
                        </tr>

                        <tr>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-left">
                                    <span>
                                        <SelectSpecialities v-model="newFeeSpeciality" class="border rounded p-1" />
                                    </span>
                                </div>
                            </td>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-left">
                                    <span>
                                        <SelectServices v-model="newFeeService" :specialities="newFeeSpeciality"
                                            class="border rounded p-1" />
                                    </span>
                                </div>
                            </td>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-left">
                                    <UInput v-model="newFeeAmount" placeholder="$ Total" class="border rounded p-1" />
                                </div>
                            </td>
                            <td :class="ui.td">
                                <div class="grid grid-rows justify-center">
                                    <span @click="createFee" :class="ui.span">
                                        💾
                                    </span>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

        </UCard>
    </div>

</template>

<script lang="ts" setup>
const props = defineProps({
    calendarEvent: Object,
})

const newFeeSpeciality = ref<any>({})
const newFeeService = ref<any>({})
const newFeeAmount = ref('0')


const {
    data: fees,
    pagination,
    search,
    pending,
    refresh
} = usePaginatedFetch<any>(`/api/fees/?search&policy=${props.calendarEvent?.id}`);




const deleteFees = async (id: number) => {
    const message = confirm('¿Estás seguro de eliminar esta Tarifa?')
    if (message) {
        const response = await $fetch(`api/fees/${id}/`, {
            method: 'DELETE'
        })
        refresh()
    }
}

onMounted(() => {
    refresh()
})

const createFee = async () => {
    const response = await $fetch<any>("/api/fees/", {
        method: "POST",
        body: {
            specialities: newFeeSpeciality.value.id,
            service: newFeeService.value.id,
            amount: newFeeAmount.value,
            third_entity: props.calendarEvent?.third_entity_full.id
        }
    });

    if (response) {

        const policiesResponse = await $fetch<any>(`api/polices/${props.calendarEvent?.id}`, {
            method: "GET"
        });

        if (policiesResponse) {
            const updatedFees = [...policiesResponse.fees, response.id];
            await $fetch(`api/polices/${props.calendarEvent?.id}`, {
                method: "PATCH",
                body: {
                    fees: updatedFees
                }
            });
        }

        fees.value.push(response);
        newFeeSpeciality.value = {};
        newFeeService.value = {};
        newFeeAmount.value = '0';
    }
};


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
    console.log("Archivo seleccionado:", file);

    const formData = new FormData();
    formData.append('file', file);

    if (!confirm("¿Estás seguro de cargar la lista de Servicios? Esto sobrescribirá y borrará los Servicios del Contrato actuales.")) {
        return;
    }

    const polices: { results: any[] } = await $fetch(`api/fees/?policy=${props.calendarEvent?.id}`, {
        method: 'GET'
    })

    for (const fee of polices.results) {
        const response = await $fetch(`api/fees/${fee.id}`, {
            method: 'DELETE'
        })
    }

    const reader = new FileReader();
    reader.onload = async (e) => {
        const text = e.target?.result as string;
        const lines = text.split('\n');
        for (const line of lines) {
            console.log("line", line);
            //toast.add({ title: "line: " + line });
            // entidad,specialidad,service,polici,amount
            const [code, amount] = line.split(',');

            toast.add({ title: "Code: " + code + " Amount: " + amount });

            const service: { results: any[] } = await $fetch(`api/services/?code=${code}`, {
                method: 'GET'
            })

            const policyId = props.calendarEvent?.id;
            const serviceId = service.results[0]?.id;
            const specialityId = service.results[0]?.speciality;
            const third_entityId = props.calendarEvent?.third_entity_full.id;

            await updatePolicesList(policyId, serviceId, specialityId, third_entityId, parseFloat(amount));

        }
        toast.add({ title: "Lista de Servicios actualizada" });
        fileInput.value = null;
    };
    reader.readAsText(file);
};



const updatePolicesList = async (policyId: number, serviceId: number, specialityId: number, thirdEntityId: number, amount: number) => {
    try {


        const priceEditing = {
            policy: policyId,
            service: serviceId,
            specialities: specialityId,
            third_entity: thirdEntityId,
            amount: amount
        }

        const response = await $fetch(`api/fees/`, {
            method: 'POST',
            body: priceEditing
        })
        if (response) {
            toast.add({ title: `Servicio  creado` })
        }

    } catch (error) {
        toast.add({ title: `Error al actualizar` })
    }
    refresh()
}



</script>
