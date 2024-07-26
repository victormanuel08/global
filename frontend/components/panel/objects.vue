<template>
    <div>
        <h1>Objetos</h1>
        <div class="grid grid-cols-5  md:grid-cols-5">
            <div>
                <UCheckbox 
                    v-model="record.obj" 
                    class="border rounded p-1" 
                    label="Presenta Objetos" 
                    @change="saveItem(record.id, 'obj', record.obj)"
                />
            </div>
            <div></div>
            <div></div>
            <div></div>
            <div></div>
        </div>

        <div class="grid grid-cols-1  md:grid-cols-1" v-if="record.obj" >
            <div>
                <label class="block text-sm font-medium text-gray-700">Descripcion Objetos:</label>
                <UTextarea
                    v-model="record.value_obj"
                    variant="outline"
                    placeholder="Descripcion de los Objetos"
                    @change="saveItem(record.id, 'value_obj', record.value_obj)"
                ></UTextarea>
            </div>
        </div>

        <div class="grid grid-cols-5  md:grid-cols-5" v-if="record.obj" >
            <div class="mr-2">
                <label class="block text-sm font-medium text-gray-700">Tercero Toma Objetos:</label>
                <SelectThird :third-type="'P'"  v-model="record.third_obj_full" @change="saveItem(record.id, 'third_obj', record.third_obj_full.id )">
                </SelectThird>
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Relacion con el Paciente:</label>             
                <SelectChoice :choiceType="'RELATIONSHIP_CHOICES'" v-model="record.relationship_obj_full" @change="saveItem(record.id, 'relationship_obj', record.relationship_obj_full.id )"/>
            </div>
            <div></div>
            <div></div>
            <div>
                <button @click="signedRecord()">
                    🖋️ Firmar aqui
                </button>
                <img :src="record.signed_obj" alt="Imagen Base64" width="60%" height="auto" v-if ="record.signed_obj"/>
                <strong>
                    <hr style="border: 1px solid black; font-weight: bold;">
                    <p>
                       {{ record.relationship_obj_full?.name }}.  {{ record.third_obj_full?.name }} {{ record.third_obj_full?.second_name }} {{ record.third_obj_full?.last_name }} {{ record.third_obj_full?.second_last_name }}
                    </p>
                </strong>
            </div>
        </div>
    </div>
    <ModalSign :record="record" @close="handleModalClose" v-model="isSing" :detail="detail" :typeThird="'signed_obj'" />
</template>

<script lang="ts" setup>

const isSing = ref(false)
const detail = ref(false)

const modelValue = defineProps({
    calendarEvent: Object,
})

const record = ref({} as any)


onMounted(() => {
    fetchRecord(modelValue.calendarEvent?.record.id)  
});



const fetchRecord = async (q: any) => {
    const response = await $fetch<any>("api/records/" + q)    
    record.value = response  
    console.log('RECORDobjets',record.value)
    record.value.relationship_obj_full = await getCHOICE(record.value.relationship_obj, 'RELATIONSHIP_CHOICES')
}

const signedRecord = async () => {
    isSing.value = true
}

const handleModalClose = (value: any) => {
    isSing.value = false
    fetchRecord(modelValue.calendarEvent?.record.id)  
}

const saveItem = async (index: number, field: string, value: string) => {
    const response = await $fetch(`api/records/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    fetchRecord(modelValue.calendarEvent?.record.id)  
};

</script>

<style></style>
