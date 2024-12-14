<template>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-6 mt-4">
        <div class="mr-2" v-if="record.third_medic_full?.speciality_full.code === 'AMB'">
            <label class="block text-sm font-medium text-gray-700">Prioridad:</label>
            <SelectChoice :choiceType="'PRIORITY_CHOICES'" v-model="record.priority_full"
                @change="saveItem(record.id, 'priority', record.priority_full.id), console.log(record.priority_full)"
                :style="record.priority_full?.id === 'R' ? 'background-color: red' : record.priority_full?.id === 'Y' ? 'background-color: yellow' : record.priority_full?.id === 'G' ? 'background-color: green' : record.priority_full?.id === 'W' ? 'background-color: white' : 'background-color: black'"
                :color="record.priority_full?.id === 'R' ? 'background-color: red' : record.priority_full?.id === 'Y' ? 'background-color: yellow' : record.priority_full?.id === 'G' ? 'background-color: green' : record.priority_full?.id === 'W' ? 'background-color: white' : 'background-color: black'">
            </SelectChoice>
        </div>
        <div class="mr-2" v-if="record.third_medic_full?.speciality_full.code === 'AMB'">
            <label class="block text-sm font-medium text-gray-700">Causa Externa:</label>
            <SelectChoice :choiceType="'EXTERNAL_CAUSE_CHOICES'" v-model="record.external_cause_full"
                @change="saveItem(record.id, 'external_cause', record.external_cause_full.id)" />
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Seleccion Paciente: <span @click="showModalThirdAmbulance('')"
                    >➕</span><span
                    @click="showModalThirdAmbulance(record.third_patient_full)"
                    v-if="record.third_patient_full?.nit !== '222222222222'">🖊️</span></label>


            <SelectThird :placeholder="'Tercero'" :third-type="'P'" v-model="record.third_patient_full"
                @change="saveItem(record.id, 'third_patient', record.third_patient_full.id)"
                />
        
            
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Identificacion Temporal</label>
            <UInput v-model="record.number_report_id" placeholder="TI. Reporte Clinica"
                @change="saveItem(record.id, 'number_report_id', record.number_report_id)" />
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Acompañante: <span
                    @click="showModalThirdAmbulanceBuddy('')">➕</span></label>
            <SelectThird :placeholder="'Tercero'" :third-type="'P'" v-model="record.third_buddy_full"
                @change="saveItem(record.id, 'third_buddy', record.third_buddy_full?.id)" />
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Relacion con el Paciente:</label>
            <SelectChoice :choiceType="'RELATIONSHIP_CHOICES'" v-model="record.relationship_full"
                @change="saveItem(record.id, 'relationship', record.relationship_full.id)" />
        </div>

    </div>

    <h1>Informacion Paciente </h1>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-4" v-if="record.third_patient_full?.type_document == 'AS'">
        <div>
            <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
            {{ record.third_patient_full?.nit }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Nombre: </label>
            {{ record.third_patient_full?.name }} {{ record.third_patient_full?.second_name }} {{
                record.third_patient_full?.last_name }} {{ record.third_patient_full?.second_last_name }}
        </div>

    </div>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-4" v-if="record.third_patient_full?.type_document !== 'AS'">
        <div>
            <label class="block text-sm font-medium text-gray-700">Identificacion:</label>
            {{ record.third_patient_full?.nit }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Nombre: </label>
            {{ record.third_patient_full?.name }} {{ record.third_patient_full?.second_name }} {{
                record.third_patient_full?.last_name }} {{ record.third_patient_full?.second_last_name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Fecha de Nacimiento</label>
            {{ record.third_patient_full?.city_birth_full?.name }} - {{ record.third_patient_full?.date_birth }} ({{
                calculateAge(record.third_patient_full?.date_birth) }} )
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Telefono:</label>
            {{ record.third_patient_full?.phone }}

        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Etnia: </label>
            {{ record.third_patient_full?.etnia_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Tipo de Sangre</label>
            {{ record.third_patient_full?.blood_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Sexo: </label>
            {{ record.third_patient_full?.sex_full?.name }}
        </div>
        <div v-if="record.third_patient_full?.sex_full?.id == 'F'">
            <label class="block text-sm font-medium text-gray-700">Amamantamiento Complemntario: </label>
            {{ record.maternity_complementary_full?.name }}
        </div>
        <div v-if="record.third_patient_full?.sex_full?.id == 'F'">
            <label class="block text-sm font-medium text-gray-700">Amamantamiento extendido: </label>
            {{ record.third_patient_full?.maternity_extend_full?.name }}
        </div>
        <div v-if="record.third_patient_full?.sex_full?.id =='F'">
            <label class="block text-sm font-medium text-gray-700">Embarazo</label>
            {{ record.third_patient_full?.maternity_pregnancy_full?.name }}
        </div>
        <div v-if="record.third_patient_full?.sex_full?.id == 'F'">
            <label class="block text-sm font-medium text-gray-700">Violencia :</label>
            {{ record.third_patient_full?.maternity_violance_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Zona: </label>
            {{ record.third_patient_full?.zone_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Ocupacion: </label>
            {{ record.third_patient_full?.occupation_full?.name }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Profesion: </label>
            {{ record.third_patient_full?.occupation_full?.profesion }}
        </div>

    </div>
    <div class="grid grid-cols-1 gap-4 md:grid-cols-2 mt-4" v-if="record.third_patient_full?.type_document !== 'AS'">
        <div>
            <label class="block text-sm font-medium text-gray-700">Direccion:</label>
            {{ record.third_patient_full?.address }}
        </div>
        <div>
            <label class="block text-sm font-medium text-gray-700">Email:</label>
            {{ record.third_patient_full?.email }}
        </div>
    </div>

    <div v-if="record.third_patient_full?.type_document !== 'AS'" class="mt-3" hidden>
        <h1>Antecedentes</h1>
        <div class="grid grid-cols-1  md:grid-cols-2 m-4">
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Alergias: {{ record.third_patient_full?.allergies }}. {{
                    newRecordAllergies
                    }}</label>
                <UTextarea v-model="newRecordAllergies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Patologias: {{ record.third_patient_full?.pathologies }}.
                    {{ newRecordPathologies
                    }}</label>
                <UTextarea v-model="newRecordPathologies" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Medicacion:{{ record.third_patient_full?.medications }}. {{
                    newRecordMedications }}
                </label>
                <UTextarea v-model="newRecordMedications" variant="outline" />
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium text-gray-700">Liquidos y Alimentos: {{
                    record.third_patient_full?.liquids_foods }}.
                    {{ newRecordLiquidsFoods }}</label>
                <UTextarea v-model="newRecordLiquidsFoods" variant="outline" />
            </div>

        </div>
        <div class="m-2 g-4">
            <UButton class="mt-2" variant="soft" block @click="saveHistory">Guardar</UButton>

        </div>

    </div>
    <ModalEditThirdAmbulance 
      :third="thirdSelectedThird" 
      :typeT="'P'" 
      v-model="isThird" 
      @thirdCreated="handleThirdCreated" 
      @update:isThird="handleModalClose" 
    />
    <ModalEditThirdAmbulanceBuddy 
        :third="thirdSelectedThird" 
        :typeT="'P'" 
        v-model="isThirdBuddy" 
        @thirdCreated="handleThirdCreated" 
        @update:isThird="handleModalClose" 
     />

</template>

<script lang="ts" setup>

const isThird = ref(false)
const thirdSelectedThird = ref<any>({})
const newRecordAllergies = ref('')
const newRecordPathologies = ref('')
const newRecordMedications = ref('')
const newRecordLiquidsFoods = ref('')
const isThirdBuddy = ref(false)
const typeT = ref('')
const typeTT = ref('')
const toast = useToast()

interface Choice {
    id: string;
    name: string;
}

interface ThirdPatient {
    id: number;
    nit: string;
    name: string;
    second_name?: string;
    last_name: string;
    second_last_name?: string;
    type_document: string;
    type_document_full?: Choice;
    type_full?: Choice;
    sex: string;
    sex_full?: Choice;
    blood_type: string;
    blood_full?: Choice;
    ethnicity: string;
    etnia_full?: Choice;
    zone: string;
    zone_full?: Choice;
    occupation: string;
    occupation_full?: Choice;
    maternity_breasfeeding?: string;
    maternity_full?: Choice;
    maternity_breasfeeding_complementary?: string;
    maternity_complementary_full?: Choice;
    maternity_breasfeeding_extend?: string;
    maternity_extend_full?: Choice;
    maternity_pregnancy?: string;
    maternity_pregnancy_full?: Choice;
    maternity_violence?: string;
    maternity_violance_full?: Choice;
    date_birth?: string;
    city_birth_full?: { name: string };
    phone?: string;
    address?: string;
    email?: string;
    allergies?: string;
    pathologies?: string;
    medications?: string;
    liquids_foods?: string;
}

interface Record {
    id: number;
    third_patient_full: ThirdPatient;
    third_medic_full?: { speciality_full?: { code: string } };
    priority_full?: Choice;
    priority?: string;
    external_cause_full?: Choice;
    relationship_full?: Choice;
    number_report_id?: string;
    third_buddy_full?: ThirdPatient;
}

const createdThird = ref<ThirdPatient | null>(null);


const props = defineProps({
    calendarEvent: Object,
})

const record = ref<any>({})

const fetchRecord = async (q: any) => {
    if (!q) return
    const response = await $fetch<any>("api/records/" + q)
    record.value = response
    record.value.priority_full = await getCHOICE(response.priority, 'PRIORITY_CHOICES')
    record.value.external_cause_full = await getCHOICE(response.external_cause, 'EXTERNAL_CAUSE_CHOICES')
    record.value.relationship_full = await getCHOICE(response.relationship, 'RELATIONSHIP_CHOICES')
}

onMounted(async () => {
    await fetchProps();
    record.value = props.calendarEvent;
    if (props.calendarEvent) {
        await fetchRecord(props.calendarEvent.id);
    }
});

watch(() => props.calendarEvent, async (newVal) => {
    if (newVal) {
        await fetchProps();  // Recarga los `choices` cuando `calendarEvent` cambia
        record.value = newVal;
    }
});

watch(record, (newRecord) => {
    // Si el record cambia, actualiza los `choices`
    fetchProps();
});


const showModalThirdAmbulance = (value: any) => {
    thirdSelectedThird.value = value
    isThird.value = true
    typeT.value = 'P'
    typeTT.value = 'Paciente'
}

const showModalThirdAmbulanceBuddy = (value: any) => {
    thirdSelectedThird.value = value
    isThirdBuddy.value = true
    typeTT.value = 'Acompañante'
}

const handleModalClose = () => {
    isThird.value = false;  // Cerrar la modal
    isThirdBuddy.value = false;  // Cerrar la modal
    fetchRecord(record.value.id);  // Recargar el registro
};


const handleThirdCreated = (newThird: any) => {
  createdThird.value = newThird; // Aquí puedes manejar el tercero creado (por ejemplo, mostrarlo en una lista)
  console.log('Nuevo tercero creado:', createdThird.value);
  if (typeTT.value =='Paciente') {
    record.value.third_patient_full = newThird;
    saveItem(record.value.id, 'third_patient', newThird.id);
    toast.add({ title: `Paciente Actulizado` });
  }else if (typeTT.value =='Acompañante') {
    record.value.third_buddy_full = newThird;
    saveItem(record.value.id, 'third_buddy', newThird.id);
    toast.add({ title: `Acompañante  actulizado` });
  }
  fetchRecord(record.value.id);
  
};

const fetchProps = async () => {

    props.calendarEvent.third_patient_full.type_full = await getCHOICE(props.calendarEvent.third_patient_full.type, 'TYPE_CHOICES')
    props.calendarEvent.third_patient_full.sex_full = await getCHOICE(props.calendarEvent.third_patient_full.sex, "SEX_CHOICES")
    props.calendarEvent.third_patient_full.blood_full = await getCHOICE(props.calendarEvent.third_patient_full.blood_type, "BLOOD_CHOICES")
    props.calendarEvent.third_patient_full.etnia_full = await getCHOICE(props.calendarEvent.third_patient_full.ethnicity, "ETNIAS_CHOICES")
    props.calendarEvent.third_patient_full.zone_full = await getCHOICE(props.calendarEvent.third_patient_full.zone, "ZONE_CHOICES")
    props.calendarEvent.third_patient_full.occupation_full = await getCHOICE(props.calendarEvent.third_patient_full.occupation, "OCCUPATION_CHOICES")
    props.calendarEvent.third_patient_full.maternity_full = await getCHOICE(props.calendarEvent.third_patient_full.maternity_breasfeeding, "MATERNITY_CHOICES")
    props.calendarEvent.third_patient_full.maternity_complementary_full = await getCHOICE(props.calendarEvent.third_patient_full.maternity_breasfeeding_complementary, "MATERNITY_COMPLEMENTARY_CHOICES")
    props.calendarEvent.third_patient_full.maternity_extend_full = await getCHOICE(props.calendarEvent.third_patient_full.maternity_breasfeeding_extend, "MATERNITY_EXTEND_CHOICES")
    props.calendarEvent.third_patient_full.maternity_pregnancy_full = await getCHOICE(props.calendarEvent.third_patient_full.maternity_pregnancy, "MATERNITY_PREGNANCY_CHOICES")
    props.calendarEvent.third_patient_full.maternity_violance_full = await getCHOICE(props.calendarEvent.third_patient_full.maternity_violence, "MATERNITY_VIOLANCE_CHOICES")
    props.calendarEvent.third_patient_full.type_document_full = await getCHOICE(props.calendarEvent.third_patient_full.type_document, "TYPE_DOCUMENT_CHOICES")
    props.calendarEvent.priority_full = await getCHOICE(props.calendarEvent.priority, "PRIORITY_CHOICES")
    props.calendarEvent.relationship_full = await getCHOICE(props.calendarEvent.relationship, "RELATIONSHIP_CHOICES")
    props.calendarEvent.external_cause_full = await getCHOICE(props.calendarEvent.external_cause, "EXTERNAL_CAUSE_CHOICES")

}


const saveItem = async (index: number, field: string, value: string) => {

    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    if (field === 'third_patient') {
        toast.add({ title: `Paciente Actulizado` });
        props.calendarEvent.third_patient_full = response.third_patient_full
        props.calendarEvent.third_patient = response.third_patient
    }


};

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

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}



</script>

<style scoped>
p {
    font-size: 8px;
}
</style>
