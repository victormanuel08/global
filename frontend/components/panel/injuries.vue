<template>
    <div>
        <h1>Lesiones</h1>

        <div class="grid grid-cols-4 gap-4 md:grid-cols-4 m-4">
            <div>
                <label class="block text-sm font-medium text-gray-700">Parte Principal: </label>
                <SelectChoice :choiceType="'BODY_PART_CHOICES'" v-model="record.glasgow_rv_full"
                @change="saveItem(record.id, 'body', record.body_part.id)" />
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Miembro Inferior: </label>
                <SelectChoice :choiceType="'BODY_PART_SIDE_CHOICES'" v-model="record.glasgow_rv_full"
                @change="saveItem(record.id, 'body', record.body_part_side.id)" />
            </div>     
        </div>
    </div>  
</template>

<script lang="ts" setup>



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
    record.value.body_full = await getCHOICE(record.value.body, 'BODY_PART_CHOICES')
    record.value.body_side_full = await getCHOICE(record.value.body, 'BODY_PART_SIDE_CHOICES')
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
