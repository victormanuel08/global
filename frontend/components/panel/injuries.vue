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
                <img src="@/assets/img/body.png" alt="Imagen" v-else />
                <div class="grid-container" :class="{ transparent: isSaving }">
                    <div v-for="n in 768" :key="n" class="grid-item" :class="{ hideContent: isSaving }"
                        @click="showRegion(n)">
                        {{ n }}
                        <div v-for="(injurie, index) in listInjuries" :key="injurie.id">
                            <div class="square" v-if="injurie.point === n">
                                <div class="circle">{{ index + 1 }}</div>
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
                    @click="createListInjuries(record.body_part_full, record.body_part_side_full, newInjurie, point, 'M')">
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
import Swal from 'sweetalert2';

const toast = useToast();
const newInjurie = ref('')
const listInjuries = ref([] as injurie[])
const listInjuries2 = ref([] as any[])
const listBody = ref([] as any[])
const point = ref(0)
const procedures_others = ref('')
const newServices = ref([] as number[]);

const isSaving = ref(false);

const selectedDiagnoses = ref<{ id: number }[]>([]);

const newRecordAllergies = ref('Niega alergias')
const newRecordPathologies = ref('Niega patologías')
const newRecordMedications = ref('Niega medicación')
const newRecordLiquidsFoods = ref('Niega líquidos y alimentos')

// const selectedDiagnoses = ref([]);

const handleDiagnosesChange = (value: any) => {
    record.value.diagnosis_multi_full = value;

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
        //console.error('Error en la solicitud al servidor:', error);
        toast.add({ title: 'Error', description: 'Error al guardar la imagen' });
    }
};

const viewDiagnosesSecondaries = async (value: any) => {
    selectedDiagnoses.value = record.value.diagnosis_multi_full;
    const diagnosisIds = selectedDiagnoses.value.map(diagnosis => diagnosis.id);

    try {
        const response = await $fetch(`api/records/${value}`, {
            method: 'PATCH', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ diagnosis_multiple: diagnosisIds }),
        });

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
        const body: { allergies?: string; pathologies?: string; medications?: string; liquids_foods?: string } = {};
        // Combinar los antecedentes actuales con los nuevos y si no hay, no enviar nada solo envia lo que se modifica
        if (record?.value.third_patient_full?.allergies || newRecordAllergies?.value) {
            body.allergies = [
                record?.value.third_patient_full?.allergies,
                newRecordAllergies?.value
            ].filter(Boolean).join('. ');
        }

        if (record?.value.third_patient_full?.pathologies || newRecordPathologies?.value) {
            body.pathologies = [
                record?.value.third_patient_full?.pathologies,
                newRecordPathologies?.value
            ].filter(Boolean).join('. ');
        }

        if (record?.value.third_patient_full?.medications || newRecordMedications?.value) {
            body.medications = [
                record?.value.third_patient_full?.medications,
                newRecordMedications?.value
            ].filter(Boolean).join('. ');
        }

        if (record?.value.third_patient_full?.liquids_foods || newRecordLiquidsFoods?.value) {
            body.liquids_foods = [
                record?.value.third_patient_full?.liquids_foods,
                newRecordLiquidsFoods?.value
            ].filter(Boolean).join('. ');
        }

        const response = await $fetch(`api/thirds/${record.value.third_patient_full.id}`, {
            method: 'PATCH',
            body: JSON.stringify(body),
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



    record.value.body_part_full = await getCHOICE(record.value.body, 'BODY_PART_CHOICES')
    record.value.body_part_side_full = await getCHOICE(record.value.body_side, 'BODY_PART_SIDE_CHOICES')
    if (record.value.list_injuries) {
        listInjuries.value = JSON.parse(record.value.list_injuries)
    }

}

const saveInjuries = async (
    index: number,
    injuries: object[],
    body: any,
    injuries2: object[]
) => {
    try {
        // Cambiar el estado para activar las clases
        isSaving.value = true;

        // Procesar las lesiones
        let newConcatInjuries = "";
        for (const injury of injuries) {
            newConcatInjuries += `${injury.body_part.name}  ${injury.injurie}\n`;
        }

        // Guardar los datos en el servidor
        const response = await $fetch(`api/records/${index}`, {
            method: "PATCH",
            body: JSON.stringify({
                body: body,
                injuries: newConcatInjuries,
                list_injuries: JSON.stringify(injuries),
            }),
        });

        // Simular el tiempo de guardado si es necesario
        await fetchRecord(props.calendarEvent?.id);

        Swal.fire({
            title: '¡Éxito!',
            text: 'Lesiones guardadas correctamente',
            icon: 'success',
            confirmButtonText: 'Aceptar'
        });
        downloadImage();
    } catch (error) {
        //console.error("Error al guardar las lesiones:", error);


        Swal.fire({
            title: '¡Érror!',
            text: 'Hubo un problema al guardar las lesiones',
            icon: 'error',
            confirmButtonText: 'Aceptar'
        });
    } finally {
        // Restaurar el estado al finalizar
        isSaving.value = false;
    }
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
        return toast.add({ title: 'Error', description: 'Debe seleccionar un miembro inferior' });
    }
    if (body_part.id === 'MI' && body_part_side.id) {
        pointStart = await getCHOICE(body_part_side?.id, 'BODY_PART_SIDE_CHOICES');

    } else {
        pointStart = await getCHOICE(body_part?.id, 'BODY_PART_CHOICES');

    }

    if (!point) {

        if (sex === 'F') {
            const valoresFemeninos = pointStart.female.split(',').map(Number);
            point = Math.min(...valoresFemeninos);

        } else if (sex === 'M') {
            const valoresMasculinos = pointStart.male.split(',').map(Number);
            point = Math.min(...valoresMasculinos);

        }
    }
    if (body_part_side.id) {
        listInjuries.value.push({ body_part: body_part_side, injurie: injurie, point: point });
        listBody.value.push(body_part_side.id);

    } else {
        listInjuries.value.push({ body_part: body_part, injurie: injurie, point: point });
        listBody.value.push(body_part.id);

    }

    cleanFields();

    Swal.fire({
        title: '¡Éxito!',
        text: 'Lesión agregada correctamente, recuerde grabar usando el botón salvar para guardar los cambios',
        icon: 'success',
        confirmButtonText: 'Aceptar'
    });
};


const deleteInjury = async (injuryToDelete: any) => {
    listInjuries.value = listInjuries.value.filter((item: any) => item !== injuryToDelete);
    listBody.value = listBody.value.filter((item: any) => item !== injuryToDelete.body_part.id);
};

const showRegion = async (n: number) => {


    point.value = n
    record.value.body_part_full = await getBODYPART(n, 'BODY_PART_CHOICES', 'M');
    record.value.body_part_side_full = await getBODYPART(n, 'BODY_PART_SIDE_CHOICES', 'M');


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

    const response = await $fetch<any>(`api/records/${props.calendarEvent?.id}/`, {
        method: 'Patch',
        body: JSON.stringify({
            service: newServices?.value,
            procedures_others: procedures_others?.value
        })
    });

};

</script>

<style>
/* Estilo por defecto de la cuadrícula */
.grid-container {
    display: grid;
    grid-template-columns: repeat(24, 0.5fr);
    grid-template-rows: repeat(32, 0.5fr);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.grid-item {
    position: relative;
    border: 1px solid #ccc;
    /* Borde visible */
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: xx-small;
}

/* Clase para hacer transparente el texto y ocultar el borde */
.grid-container.transparent .grid-item {
    border: none;
    /* Quita el borde */
}

.grid-item.hideContent {
    color: transparent;
    /* Hace el texto invisible */
}

.square {
    width: 50%;
    height: 50%;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid #ccc;
}

.circle {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-100%, -50%);
    width: 20px;
    height: 20px;
    background-color: #d41616;
    border-radius: 50%;
    color: #f9f9f9;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>