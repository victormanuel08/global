<template>
    <USelectMenu v-model="modelValue" option-attribute="concat" :options="options" :searchable="true"
        v-model:query="query" :clearSearchOnClose="true" @click="clickHandler" :placeholder="'Accidentes'" >
    </USelectMenu>
</template>
<script setup lang="ts">


const options = ref<any[]>([])

const query = ref("")
const modelValue = defineModel<any>({ default: () => ({}) }) //Esto es para que el componente pue1da ser usado con v-model


type Props = {
    third?: string | number   
}

const props = withDefaults(defineProps<Props>(), {
    third: '',
})

const clickHandler = () => {    
    retrieveFromApi()
}

const retrieveFromApi = async () => {
    const queryParams = {
        search: query.value,
        third_patient: props.third,
        fee_full__policy_full__type_police: "SE",
        insurance: 1,
        date_origin: "1999-01-01",
    };

    try {
        const response = await $fetch<any>("api/scheduleds/", {
            query: queryParams,
        });

        // Agrega el objeto vacío al principio de la lista
        console.log('CITASASEGURADORA VIEJAS', response.results)
        options.value = [
            {         
                insurance: 0,       
                concat: "Sin Aseguradora",
            },            
            {
                insurance: 1,                
                concat: "Nuevo Caso Aseguradora",
            },
            ...response.results.map((scheduled: any) => ({
                ...scheduled,
                insurance: 1,     
                date_origin: scheduled.date,           
                concat: `${scheduled.date} ${scheduled.speciality_full.description} ${scheduled.fee_full?.service_full.description} ${scheduled.fee_full?.policy_full.name}`,
            })),
        ];
            

    } catch (error) {
        console.error("Error al obtener los datos de la API:", error);
    }
};



watch(
  [query, () => props.third],
  async ([newQuery, newThird], [oldQuery, oldThird]) => {
    if (oldThird !== newThird) {
      // Si la especialidad cambió, borramos el tercero que teníamos seleccionado
      modelValue.value = {};
    }
    // Llama a retrieveFromApi() aquí o realiza otras acciones necesarias
    retrieveFromApi();
  }
);

</script>

