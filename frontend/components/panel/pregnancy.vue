<template>
    <div>
        <h1>Informacion Paciente</h1>
        <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
            <div>
                <label class="block text-sm font-medium text-gray-700">Lactancia:</label>
                {{ convertChoice(record.maternity_breasfeeding, maternity_list) }}             
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Amamantamiento Complemntario: </label>
                {{ convertChoice(record.maternity_breasfeeding_complementary, maternity_complementary_list) }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Amaamantamiento extendido: </label>   
                {{convertChoice(record.maternity_breasfeeding_extend, maternity_extend_list) }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Embarazo</label>
               {{ convertChoice(record.maternity_pregnancy, maternity_pregnancy_list) }}
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Violencia :</label>
               {{ convertChoice(record.maternity_violence, maternity_violence_list) }}
               
            </div>           
        </div>
    </div>
</template>

<script lang="ts" setup>

const modelValue = defineProps({
    calendarEvent: Object,    
})  
const maternity_list = ref<any[]>([])
const maternity_complementary_list = ref<any[]>([])
const maternity_extend_list = ref<any[]>([])
const maternity_pregnancy_list = ref<any[]>([])
const maternity_violence_list = ref<any[]>([])

const record = ref<any>({})
onMounted(() => {
    fetchChoices()
    record.value = modelValue.calendarEvent?.patient    
    console.log("RECORD", record)
    
})  
const fetchChoices = async () => {
  const response = await $fetch<any>('api/api/choices/') 
  maternity_list.value = response.MATERNITY_CHOICES
  maternity_complementary_list.value = response.MATERNITY_COMPLEMENTARY_CHOICES
  maternity_extend_list.value = response.MATERNITY_EXTEND_CHOICES
  maternity_pregnancy_list.value = response.MATERNITY_PREGNANCY_CHOICES
  maternity_violence_list.value = response.MATERNITY_VIOLANCE_CHOICES
  console.log("CHOICES", response)

}

const convertChoice = (value: string | number, list: any[]) => {
    try {
        if (value === null) {
            return '';
        }
        const stringValue = String(value); 
        const choice = list.find((item) => item[0] === stringValue);
        return choice ? choice[1] : stringValue;
    } catch (error) {
        console.error('Error al cargar las opciones:', error);
    }
};



</script>
<style></style>