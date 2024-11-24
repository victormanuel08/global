<template>
    <div v-if="record.third_patient_full?.type_document !== 'AS'" class="mt-3">
        <h1>Antecedentes</h1>
        <div class="grid grid-cols-1 md:grid-cols-1 m-4">
            <div class="m-2 g-4">
                <label class="block text-sm font-medium w-full break-words">Alergias: {{
                    record.third_patient_full?.allergies }}. {{ newRecordAllergies }}</label>
                <UTextarea v-model="newRecordAllergies" variant="outline" style="height: 2em;" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium w-full break-words">Patologías: {{
                    record.third_patient_full?.pathologies }}. {{ newRecordPathologies }}</label>
                <UTextarea v-model="newRecordPathologies" variant="outline" style="height: 2em;" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium w-full break-words">Medicación: {{
                    record.third_patient_full?.medications }}. {{ newRecordMedications }}</label>
                <UTextarea v-model="newRecordMedications" variant="outline" style="height: 2em;" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium w-full break-words">Líquidos y Alimentos: {{
                    record.third_patient_full?.liquids_foods }}. {{ newRecordLiquidsFoods }}</label>
                <UTextarea v-model="newRecordLiquidsFoods" variant="outline" style="height: 2em;" />
            </div>
        </div>

        <div class="m-2 g-4">
            <UButton class="mt-2" variant="soft" block @click="saveHistory">Guardar Antecedentes</UButton>

        </div>

    </div>
    <h1>Lesiones</h1>
    <div class="container grid grid-cols-1   lg:grid-cols-2  m-4">
        <div style="overflow: auto;">
            <div class="grid-container2" style="width: 450px; height: 500px; position: relative;">
                <img src="@/assets/img/body.png" alt="Imagen" v-if="record.third_patient_full?.sex !== 'F'" />
                <img src="@/assets/img/body2.png" alt="Imagen" v-else />
                <div class="grid-container">
                    <div v-for="n in 192" :key="n" class="grid-item" @click="showRegion(n)">
                        <div v-for="(injurie, index) in listInjuries" :key="injurie.id">
                            <div class="square" v-if="injurie.point === n">
                                <div class="circle">
                                    {{ index + 1 }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <div class="m-2">
            <div>
                <label class="block text-sm font-medium text-gray-700">Descripcion del Procedimiento:</label>
                <UTextarea v-model="record.descript_procedures" variant="outline"
                    placeholder="Descripcion del Procedimiento"
                    @change="saveItem(record.id, 'descript_procedures', record.descript_procedures)"></UTextarea>
            </div>

            <div class="m-2">
                <label>Parte Principal:</label>
                <SelectChoice :choiceType="'BODY_PART_CHOICES'" v-model="record.body_part_full" />
            </div>
            <div v-if="record.body_part_full?.id === 'MI'" class="m-2">
                <label>Miembro Inferior: </label>
                <SelectChoice :choiceType="'BODY_PART_SIDE_CHOICES'" v-model="record.body_part_side_full" />
            </div>

            <div class="m-2" hidden>
                <UTextarea v-model="newInjurie" variant="outline" placeholder="Descripcion de la Lesion" />
            </div>
            <div class="m-2">
                <button
                    @click="createListInjuries(record.body_part_full, record.body_part_side_full, newInjurie, point, record.third_patient_full?.sex)">
                    ✅ Lesion
                </button>
            </div>
            <div v-if="listInjuries.length > 0" class="m-2">
                <div>
                    <label>Lesiones:</label>
                </div>
                <div v-for="(injurie, index) in listInjuries" :key="injurie.id">
                    <button @click="deleteInjury(injurie)">
                        ❌ {{ index + 1 }}
                    </button>
                    {{ injurie.body_part.name }} {{ injurie.point }}
                    <UTooltip :text="injurie.injurie" :shortcuts="['⌘', 'O']">
                        <span>👁️</span>
                    </UTooltip>
                </div>
                <div>
                    <button @click="saveInjuries(record.id, listInjuries, listBody, listInjuries2)">
                        💾 Listado Lesiones
                    </button>

                </div>
            </div>
        </div>
    </div>
    <PanelProcedures :calendarEvent="props.calendarEvent" />
    <div class="m-2">
        <label>Diagnostico Principal:</label>
        <SelectDiagnoses v-model="record.diagnosis_full"
            @change="saveItem(record.id, 'diagnosis', record.diagnosis_full?.id)" />
    </div>
    <div class="m-2">
        <label>{{ record.diagnosis_multi_full?.length || 0 }} Diagnosticos Secundarios:</label>

        <SelectDiagnosesMulti v-model="record.diagnosis_multi_full" @change="handleDiagnosesChange">
            <template #selected="{ selectedOptions }">
                <span v-if="selectedOptions.length == 0">Seleccionar Diagnósticos</span>
            </template>
        </SelectDiagnosesMulti>

    </div>


</template>

<script lang="ts" setup>
import html2canvas from 'html2canvas';
const newInjurie = ref('')
const listInjuries = ref([] as injurie[])
const listInjuries2 = ref([] as any[])
const listBody = ref([] as any[])
const point = ref(0)
const procedures_others = ref('')
const newServices = ref([] as number[]);

const selectedDiagnoses = ref<{ id: number }[]>([]);

const newRecordAllergies = ref('')
const newRecordPathologies = ref('')
const newRecordMedications = ref('')
const newRecordLiquidsFoods = ref('')

// const selectedDiagnoses = ref([]);

const handleDiagnosesChange = (value: any) => {
    record.value.diagnosis_multi_full = value;
    console.log('Valor seleccionado:', value);
    // Aquí puedes llamar a viewDiagnosesSecondaries si es necesario // 
    viewDiagnosesSecondaries(record.value.id);
};

const downloadImage = async () => {
    const element = document.querySelector('.grid-container2');
    const canvas = await html2canvas(element as HTMLElement);
    const dataURL = canvas.toDataURL();
    //const a = document.createElement('a');
    //a.href = dataURL;
    //a.download = 'lesiones.png';
    //a.click();
    canvas.toBlob((blob) => {
        if (blob) {
            saveImage(record.value.id, 'imgls', blob);
        }
    }, 'image/png');
};


const saveImage = async (index: number, field: string, blob: Blob) => {
    try {
        console.log("blob", blob)
        const file = new File([blob], 'HC-Lesiones-' + index + '.png', { type: 'image/png' });
        const formData = new FormData();
        formData.append(field, file);

        const response = await $fetch(`api/records/${index}/`, {
            method: 'PATCH',
            body: formData,
            headers: {
                "Content-Type": "multipart/form-data; boundary=----"
            },
        });

    } catch (error) {
        console.error('Error en la solicitud al servidor:', error);
    }
};

const viewDiagnosesSecondaries = async (value: any) => {
    selectedDiagnoses.value = record.value.diagnosis_multi_full;
    const diagnosisIds = selectedDiagnoses.value.map(diagnosis => diagnosis.id);
    console.log('diagnosisIds', diagnosisIds);
    try {
        const response = await $fetch(`api/records/${value}`, {
            method: 'PATCH', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ diagnosis_multiple: diagnosisIds }),
        });
        console.log('Response:', response);
    }
    catch (error) {
        console.error('Error al guardar los diagnósticos:', error);
    }
};

const record = ref({} as any)

const props = defineProps({
    calendarEvent: Object,
})


const saveHistory = async () => {
    try {
        const response = await $fetch(`api/thirds/${record.value.third_patient_full.id}`, {
            method: 'PATCH',
            body: JSON.stringify({
                allergies: record?.value.third_patient_full?.allergies + '. ' + newRecordAllergies?.value,
                pathologies: record?.value.third_patient_full?.pathologies + '. ' + newRecordPathologies?.value,
                medications: record?.value.third_patient_full?.medications + '. ' + newRecordMedications?.value,
                liquids_foods: record?.value.third_patient_full?.liquids_foods + '. ' + newRecordLiquidsFoods?.value
            })
        });
        fetchRecord(record.value.id);
        if (response) {
            newRecordAllergies.value = '';
            newRecordPathologies.value = '';
            newRecordMedications.value = '';
            newRecordLiquidsFoods.value = '';
        }
    } catch (error: any) {
        const errorMessage = error.message || 'Error desconocido';
    }
};

onMounted(() => {
    fetchRecord(props.calendarEvent?.id)
    console.log('DMF', record.value.diagnosis_multi_full)
    selectedDiagnoses.value = record.value.diagnosis_multi_full
    // handleDiagnosesChange(record.value.diagnosis_multi)
});

type injurie = {
    body_part: object,
    injurie: string
    point: number
}

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    record.value = response
    console.log('RECORDobjetsFEETRECORD', record.value)


    record.value.body_part_full = await getCHOICE(record.value.body, 'BODY_PART_CHOICES')
    record.value.body_part_side_full = await getCHOICE(record.value.body_side, 'BODY_PART_SIDE_CHOICES')
    if (record.value.list_injuries) {
        listInjuries.value = JSON.parse(record.value.list_injuries)
    }

}

const saveInjuries = async (index: number, injuries: object[], body: any, injuries2: object[]) => {

    let newConcatInjuries = '';

    for (const injury of injuries) {
        newConcatInjuries += `${injury.body_part.name}  ${injury.injurie}\n`;

    }

    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            body: body,
            injuries: newConcatInjuries,
            list_injuries: JSON.stringify(injuries)
        }),
    });
    fetchRecord(props.calendarEvent?.id);
    alert('Lesiones guardadas correctamente')
    downloadImage();
};

const cleanFields = async () => {
    newInjurie.value = ''
    record.value.body_part_full = []
    record.value.body_part_side_full = []
    point.value = 0
}

const createListInjuries = async (body_part: any, body_part_side: any, injurie: string, point: number, sex: string) => {
    let pointStart
    if (body_part.id === 'MI' && !body_part_side.id) {
        return alert('Seleccione una parte del cuerpo')
    }
    if (body_part.id === 'MI' && body_part_side.id) {
        pointStart = await getCHOICE(body_part_side?.id, 'BODY_PART_SIDE_CHOICES');
        console.log('pointStart1', pointStart)
    } else {
        pointStart = await getCHOICE(body_part?.id, 'BODY_PART_CHOICES');
        console.log('pointStart2', pointStart)
    }

    if (!point) {

        if (sex === 'F') {
            const valoresFemeninos = pointStart.female.split(',').map(Number);
            point = Math.min(...valoresFemeninos);
            console.log('pointF', point)
        } else if (sex === 'M') {
            const valoresMasculinos = pointStart.male.split(',').map(Number);
            point = Math.min(...valoresMasculinos);
            console.log('pointM', point)
        }
    }
    if (body_part_side.id) {
        listInjuries.value.push({ body_part: body_part_side, injurie: injurie, point: point });
        listBody.value.push(body_part_side.id);
        console.log('body_part_side1', listInjuries.value)
        console.log('body_part_side1', listBody.value)
    } else {
        listInjuries.value.push({ body_part: body_part, injurie: injurie, point: point });
        listBody.value.push(body_part.id);
        console.log('body_part_side2', listInjuries.value)
        console.log('body_part_side2', listBody.value)
    }

    cleanFields();
    alert('Lesion agregada correctamente, recuerde grabar usando el boton salvar para guardar los cambios')
};


const deleteInjury = async (injuryToDelete: any) => {
    listInjuries.value = listInjuries.value.filter((item: any) => item !== injuryToDelete);
    listBody.value = listBody.value.filter((item: any) => item !== injuryToDelete.body_part.id);
};

const showRegion = async (n: number) => {
    record.value.body_part_full = await getBODYPART(n, 'BODY_PART_CHOICES', record.value.third_patient_full?.sex);
    record.value.body_part_side_full = await getBODYPART(n, 'BODY_PART_SIDE_CHOICES', record.value.third_patient_full?.sex);
    point.value = n
    console.log('pointshowregion', point.value)

}



const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    retrieveFromApi(index)

};



const retrieveFromApi = async (q: any) => {
    const response = await $fetch<any>("api/records/" + props.calendarEvent?.id)
    record.value = response
}

const saveServices = async () => {
    console.log('Guardando', newServices.value + ' ' + procedures_others.value);
    const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}/`, {
        method: 'Patch',
        body: JSON.stringify({
            service: newServices?.value,
            procedures_others: procedures_others?.value
        })
    });
    console.log('Respuesta:', response);
};

</script>
<style>
.image-container {
    width: 200px;
    height: auto;
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: repeat(16, 1fr);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

}

.grid-container2 {}

.grid-item {
    /* border: 1px solid #ccc;*/

}

.square {
    position: relative;
    width: 100%;
    height: 100%;
    /* border: 1px solid #ccc;*/
}

.circle {
    position: absolute;
    top: 10%;
    /* Centrar verticalmente */
    left: 50%;
    /* Centrar horizontalmente */
    transform: translate(-50%, 25%);
    /* Ajustar al centro */
    width: 20px;
    /* Tamaño del círculo */
    height: 20px;
    background-color: #d41616;
    /* Color del círculo */
    border-radius: 50%;
    /* Hacerlo circular */
    color: #f9f9f9;
    /* Color del número */
    font-weight: bold;
    /* Grosor del número */
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
