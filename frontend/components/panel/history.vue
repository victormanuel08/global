<template>
    <div>
        <h1>Antecedentes</h1>
        <div class="grid grid-cols-2  md:grid-cols-2 m-4">
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Alergias:</label>                
                <UTextarea  
                    v-model="record.allergies" 
                    variant="outline"                     
                    @change="saveItem('allergies',record.allergies)"/>
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Patologias:</label>                
                <UTextarea  
                    v-model="record.pathologies" 
                    variant="outline"                    
                    @change="saveItem('pathologies',record.pathologies)"/>
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium">Madecacion:</label>                
                <UTextarea  
                    v-model="record.medications" 
                    variant="outline"                
                    @change="saveItem('medications',record.medications)"/>
            </div>
            <div class="m-2 g-4">
                <label class="block text-sm font-medium text-gray-700">Liquidos y Alimentos:</label>                
                <UTextarea  
                    v-model="record.liquids_foods" 
                    variant="outline"                
                    @change="saveItem('liquids_foods',record.liquids_foods)"/>
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

const saveItem = async (field: string, value: string) => {
  const response = await $fetch(`api/thirds/${record.value.id}`, {
    method: 'PATCH',
    body: JSON.stringify({
      [field]: value,
    }),
  });
   
};

</script>
<style></style>