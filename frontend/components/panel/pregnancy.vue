<template>
    <div>
        <h1>Informacion Feminas</h1>
        <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
            <div>
                <label class="block text-sm font-medium text-gray-700">Lactancia:</label>
               
                {{ record.maternity_full?.name }}     
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Amamantamiento Complemntario: </label>
                {{ record.maternity_complementary_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Amaamantamiento extendido: </label>   
                {{ record.maternity_extend_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Embarazo</label>
                {{ record.maternity_pregnancy_full?.name }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Violencia :</label>
                {{ record.maternity_violance_full?.name }}               
            </div>           
        </div>
    </div>
</template>

<script lang="ts" setup>

const modelValue = defineProps({
    calendarEvent: Object,    
})  

const record = ref<any>({})

onMounted(() => { 
    if (modelValue.calendarEvent?.patient) {        
        record.value = modelValue.calendarEvent?.patient       
    }else{
    record.value = modelValue.calendarEvent    
} 
})  

</script>
<style></style>