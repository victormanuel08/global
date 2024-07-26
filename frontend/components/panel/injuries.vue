<template>
    <h1>Lesiones</h1>
    <div class="container">
        <div class="grid grid-cols-2   lg:grid-cols-2  m-4">

            <div class="m-2" style="width: 450px; height: 500px; position: relative;">                
                <img src="@/assets/img/body.PNG" alt="Imagen" v-if="record.body_part_full?.id !== 'MI'" />
                <img src="@/assets/img/body2.PNG" alt="Imagen" v-if="record.body_part_full?.id === 'MI'" />
                <div class="grid-container">
                    <div v-for="n in 192" :key="n" class="grid-item" @click="showRegion(n)">{{ n }}</div>
                </div>
            </div>

            <div class="m-2">
                <div class="m-2">
                    <label>Parte Principal: </label>
                    <SelectChoice :choiceType="'BODY_PART_CHOICES'" v-model="record.body_part_full" />
                </div>
                <div v-if="record.body_part_full?.id === 'MI'" class="m-2">
                    <label>Miembro Inferior: </label>
                    <SelectChoice :choiceType="'BODY_PART_SIDE_CHOICES'" v-model="record.body_part_side_full" />
                </div>
                <div class="m-2">
                    <UTextarea v-model="newInjurie" variant="outline" placeholder="Descripcion de la Lesion" />
                </div>
                <div class="m-2">
                    <button @click="createListInjuries(record.body_part_full, record.body_part_side_full, newInjurie)">
                        ✅ Lesion
                    </button>
                </div>
                <div v-if="listInjuries.length > 0" class="m-2">
                    <div>
                        <label>Lesiones:</label>
                    </div>
                    <div v-for="injurie in listInjuries" :key="injurie.id">
                        <button @click="deleteInjury(injurie)">
                            ❌
                        </button>
                        {{ injurie.body_part.name }}
                        <UTooltip :text="injurie.injurie" :shortcuts="['⌘', 'O']">
                            <span>👁️</span>
                        </UTooltip>
                    </div>
                    <div>
                        <button @click="saveInjuries(record.id, listInjuries, listBody)">
                            💾 Listado Lesiones
                        </button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script lang="ts" setup>

const newInjurie = ref('')
const listInjuries = ref([] as injurie[])
const listBody = ref([] as any[])


const record = ref({} as any)

const modelValue = defineProps({
    calendarEvent: Object,
})

onMounted(() => {
    fetchRecord(modelValue.calendarEvent?.record.id)
});

type injurie = {
    body_part: object,
    injurie: string
}

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    record.value = response
    console.log('RECORDobjets', record.value)
    record.value.body_part_full = await getCHOICE(record.value.body, 'BODY_PART_CHOICES')
    record.value.body_part_side_full = await getCHOICE(record.value.body_side, 'BODY_PART_SIDE_CHOICES')
}

const saveInjuries = async (index: number, injuries: object[], body: any) => {
    let newConcatInjuries = '';
    for (const injury of injuries) {
        newConcatInjuries += `${injury.body_part.name}  ${injury.injurie}\n`;
    }

    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            body: body,
            injuries: newConcatInjuries,
        }),
    });
    fetchRecord(modelValue.calendarEvent?.record.id);
};

const cleanFields = async () => {
    newInjurie.value = ''
    record.value.body_part_full = []
    record.value.body_part_side_full = []
}

const createListInjuries = async (body_part: any, body_part_side: any, injurie: string) => {
    if (body_part_side.id) {
        listInjuries.value.push({ body_part: body_part_side, injurie: injurie })
        listBody.value.push(body_part_side.id);
    } else {
        listInjuries.value.push({ body_part: body_part, injurie: injurie })
        listBody.value.push(body_part.id);
    }
    cleanFields();
}

const deleteInjury = async (injuryToDelete: any) => {
    listInjuries.value = listInjuries.value.filter((item: any) => item !== injuryToDelete);
    listBody.value = listBody.value.filter((item: any) => item !== injuryToDelete.body_part.id);
};

const showRegion = async (n: number) => {    
    
    console.log(await getBODYPART(n,'BODY_PART_CHOICES','male'));
    record.value.body_part_full = await getBODYPART(n,'BODY_PART_CHOICES','male');
}

</script>

<style>
.image-container {
    width: 200px;
    /* Ajusta el ancho según tus necesidades */
    height: auto;
    /* Esto mantendrá la proporción original de la imagen */

}

.grid-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    /* 6 columnas */
    grid-template-rows: repeat(16, 1fr);
    /* 2 filas */
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* Otros estilos para la cuadrícula si es necesario */
}

.grid-item {
    /* Estilos para cada celda de la cuadrícula */
    border: 1px solid #ccc;
    /* Borde para visualizar las celdas */
}
</style>
