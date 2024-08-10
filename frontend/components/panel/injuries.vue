<template>
    <h1>Lesiones</h1>
    <div class="container">
        <div class="grid grid-cols-2   lg:grid-cols-2  m-4">

            <div class="m-2" style="width: 450px; height: 500px; position: relative;">
                <img src="@/assets/img/body.PNG" alt="Imagen" v-if="record.third_patient_full?.sex !== 'F'" />
                <img src="@/assets/img/body2.PNG" alt="Imagen" v-else />
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

            <div class="m-2">
                <div class="m-2">
                    <label>Parte Principal:</label>
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
    </div>
</template>

<script lang="ts" setup>

const newInjurie = ref('')
const listInjuries = ref([] as injurie[])
const listInjuries2 = ref([] as any[])
const listBody = ref([] as any[])
const point = ref(0)




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
    point: number
}

const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)
    record.value = response
    console.log('RECORDobjetsFEETRECORD', record.value)   

    
    record.value.body_part_full = await getCHOICE(record.value.body , 'BODY_PART_CHOICES')
    record.value.body_part_side_full = await getCHOICE(record.value.body_side, 'BODY_PART_SIDE_CHOICES')
    if (record.value.list_injuries){
        listInjuries.value = JSON.parse(record.value.list_injuries)
    }
  
}

const saveInjuries = async (index: number, injuries: object[], body: any,injuries2:object[]) => {

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
    fetchRecord(modelValue.calendarEvent?.record.id);
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
    }else{
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
    background-color: #a70505;
    /* Color del círculo */
    border-radius: 50%;
    /* Hacerlo circular */
    color: #fff;
    /* Color del número */
    font-weight: bold;
    /* Grosor del número */
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
