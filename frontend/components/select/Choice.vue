<template>
    <USelectMenu 
      v-model="modelValue" 
      option-attribute="name" 
      :options="options" 
      :searchable="true"
      v-model:query="query" 
      :clearSearchOnClose="true" 
      @click="clickHandler"      
      
      >

        
    </USelectMenu>
</template>

<script setup lang="ts">

const modelValue = defineModel<any>({ default: () => ({}) })
const options = ref<any[]>([])

const choices = {
    TYPE_CHOICES: [] as choice[],
    BLOOD_CHOICES: [] as choice[],
    MATERNITY_PREGNANCY_CHOICES: [] as choice[],
    MATERNITY_CHOICES: [] as choice[],
    MATERNITY_EXTEND_CHOICES: [] as choice[],
    MATERNITY_COMPLEMENTARY_CHOICES: [] as choice[],
    MATERNITY_VIOLANCE_CHOICES: [] as choice[],
    ETNIAS_CHOICES: [] as choice[],
    SEX_CHOICES: [] as choice[],    
    STATUS_CHOICES: [] as choice[],
    OCCUPATION_CHOICES: [] as choice[],
    ZONE_CHOICES: [] as choice[],
    TYPE_DOCUMENT_CHOICES: [] as choice[],
    PRIORITY_CHOICES: [] as choice[],
    RELATIONSHIP_CHOICES: [] as choice[],
    EXTERNAL_CAUSE_CHOICES: [] as choice[],
    VEHICLE_TYPE_CHOICES: [] as choice[],
    GLASGOW_RO_CHOICES: [] as choice[],
    GLASGOW_RV_CHOICES: [] as choice[],
    GLASGOW_RM_CHOICES: [] as choice[],
    HALF_CHOICES: [] as choice[],
    BODY_PART_CHOICES: [] as choice[],
    BODY_PART_SIDE_CHOICES: [] as choice[],
} 
       
type choice = {
    id: number,
    name: string,
}
type Props = {
    choiceType: string
}
const props = withDefaults(defineProps<Props>(), {
    choiceType: ''
})

onMounted(() => {
    fetchChoices()
})

const fetchChoices = async () => {
  try {
    const response = await $fetch<any>('api/api/choices/');
    const { 
            TYPE_CHOICES,
            BLOOD_CHOICES,
            MATERNITY_CHOICES,
            MATERNITY_COMPLEMENTARY_CHOICES,
            MATERNITY_EXTEND_CHOICES,
            MATERNITY_PREGNANCY_CHOICES,
            MATERNITY_VIOLANCE_CHOICES,
            ETNIAS_CHOICES,
            SEX_CHOICES,            
            STATUS_CHOICES,
            OCCUPATION_CHOICES,
            ZONE_CHOICES,
            TYPE_DOCUMENT_CHOICES,
            PRIORITY_CHOICES,
            RELATIONSHIP_CHOICES,
            EXTERNAL_CAUSE_CHOICES,
            VEHICLE_TYPE_CHOICES,
            GLASGOW_RO_CHOICES,
            GLASGOW_RV_CHOICES,
            GLASGOW_RM_CHOICES,
            HALF_CHOICES,       
            BODY_PART_CHOICES,
            BODY_PART_SIDE_CHOICES,     
    } = response;

    const mapToChoice = (list: any[]): choice[] => {
      return list.map((item: any) => ({
        id: item[0],
        name: item[1],
      }));
    };
    choices.TYPE_CHOICES = mapToChoice(TYPE_CHOICES);
    choices.BLOOD_CHOICES = mapToChoice(BLOOD_CHOICES);
    choices.MATERNITY_CHOICES = mapToChoice(MATERNITY_CHOICES);
    choices.MATERNITY_COMPLEMENTARY_CHOICES = mapToChoice(MATERNITY_COMPLEMENTARY_CHOICES);
    choices.MATERNITY_EXTEND_CHOICES = mapToChoice(MATERNITY_EXTEND_CHOICES);
    choices.MATERNITY_PREGNANCY_CHOICES = mapToChoice(MATERNITY_PREGNANCY_CHOICES);
    choices.MATERNITY_VIOLANCE_CHOICES = mapToChoice(MATERNITY_VIOLANCE_CHOICES);
    choices.ETNIAS_CHOICES = mapToChoice(ETNIAS_CHOICES);
    choices.SEX_CHOICES = mapToChoice(SEX_CHOICES);
    choices.STATUS_CHOICES = mapToChoice(STATUS_CHOICES);
    choices.OCCUPATION_CHOICES = mapToChoice(OCCUPATION_CHOICES);
    choices.ZONE_CHOICES = mapToChoice(ZONE_CHOICES);
    choices.TYPE_DOCUMENT_CHOICES = mapToChoice(TYPE_DOCUMENT_CHOICES);
    choices.PRIORITY_CHOICES = mapToChoice(PRIORITY_CHOICES);
    choices.RELATIONSHIP_CHOICES = mapToChoice(RELATIONSHIP_CHOICES);
    choices.EXTERNAL_CAUSE_CHOICES = mapToChoice(EXTERNAL_CAUSE_CHOICES);
    choices.VEHICLE_TYPE_CHOICES = mapToChoice(VEHICLE_TYPE_CHOICES);
    choices.GLASGOW_RO_CHOICES = mapToChoice(GLASGOW_RO_CHOICES);
    choices.GLASGOW_RV_CHOICES = mapToChoice(GLASGOW_RV_CHOICES);
    choices.GLASGOW_RM_CHOICES = mapToChoice(GLASGOW_RM_CHOICES);
    choices.HALF_CHOICES = mapToChoice(HALF_CHOICES);    
    choices.BODY_PART_CHOICES = mapToChoice(BODY_PART_CHOICES);
    choices.BODY_PART_SIDE_CHOICES = mapToChoice(BODY_PART_SIDE_CHOICES);   
    options.value = choices[props.choiceType];
  } catch (error) {
    console.error('Error al cargar las opciones:', error);
  }
};
</script>

<style scoped></style>