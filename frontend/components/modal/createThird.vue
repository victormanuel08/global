<template>
    <UModal :third="third" :close="close">
        <div class="border rounded m-4 ">
            <div class=" m-4 ">
                <h3><strong>Nombre:</strong> {{ props.third?.name }} {{ props.third?.second_name }} {{
                    props.third?.last_name }} {{ props.third?.second_last_name }}</h3>
                <h3><strong>Identificacion: </strong>{{ props.third?.nit }}</h3>
                <h3><strong>Usuario: </strong>{{ props.third?.user }}</h3>
                <div class="grid grid-cols-2 gap-4 md:grid-cols-1 mt-4">

                    <div>
                        <label class="block text-sm font-medium text-gray-700">Tipo:</label>
                        <SelectChoice :choiceType="'TYPE_CHOICES'" v-model="thirdSelected.type_full"
                            @change="saveItem(thirdSelected.id, 'type', thirdSelected.type_full.id)" />
                    </div>
                    <div v-if="thirdSelected.type_full?.id === 'M'">
                        <label class="block text-sm font-medium text-gray-700">Especialidad:</label>
                        <SelectSpecialities v-model="thirdSelected.speciality_full"
                            @change="saveItem(thirdSelected.id, 'speciality', thirdSelected.speciality_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Ciudad Natal:</label>
                        <SelectCities v-model="thirdSelected.city_birth_full"
                            @change="saveItem(thirdSelected.id, 'city_birth', thirdSelected.city_birth_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Fecha Nacimiento:</label>
                        <UInput type="date" v-model="thirdSelected.date_birth"
                            @change="saveItem(thirdSelected.id, 'date_birth', thirdSelected.date_birth)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Ciudad actual:</label>
                        <SelectCities v-model="thirdSelected.city_full"
                            @change="saveItem(thirdSelected.id, 'city', thirdSelected.city_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Sexo:</label>
                        <SelectChoice :choiceType="'SEX_CHOICES'" v-model="thirdSelected.sex_full"
                            @change="saveItem(thirdSelected.id, 'sex', thirdSelected.sex_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Tipo Sangre:</label>
                        <SelectChoice :choiceType="'BLOOD_CHOICES'" v-model="thirdSelected.blood_full"
                            @change="saveItem(thirdSelected.id, 'blood_type', thirdSelected.blood_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Etnia:</label>
                        <SelectChoice :choiceType="'ETNIAS_CHOICES'" v-model="thirdSelected.etnia_full"
                            @change="saveItem(thirdSelected.id, 'ethnicity', thirdSelected.etnia_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Zona:</label>
                        <SelectChoice :choiceType="'ZONE_CHOICES'" v-model="thirdSelected.zone_full"
                            @change="saveItem(thirdSelected.id, 'zone', thirdSelected.zone_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Ocupacion2:</label>
                        <SelectChoice :choiceType="'OCCUPATION_CHOICES'" v-model="thirdSelected.occupation_full"
                            @change="saveItem(thirdSelected.id, 'occupation', thirdSelected.occupation_full.id)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Profesion:</label>
                        <<UInput v-model="thirdSelected.profesion"
                            @change="saveItem(thirdSelected.id, 'profesion', thirdSelected.profesion)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Telefono:</label>
                        <UInput v-model="thirdSelected.phone"
                            @change="saveItem(thirdSelected.id, 'phone', thirdSelected.phone)" />
                    </div>

                </div>
                <div class="mt-4" v-if="thirdSelected.sex_full?.id === 'F'">
                    <h3>Maternidad</h3>
                    <div class="grid grid-cols-3 gap-4 md:grid-cols-3">
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Periodo de Lactancia:</label>
                            <SelectChoice :choiceType="'MATERNITY_CHOICES'" v-model="thirdSelected.maternity_full"
                                @change="saveItem(thirdSelected.id, 'maternity_breasfeeding', thirdSelected.maternity_full.id)" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Complementaria:</label>
                            <SelectChoice :choiceType="'MATERNITY_COMPLEMENTARY_CHOICES'"
                                v-model="thirdSelected.maternity_complementary_full"
                                @change="saveItem(thirdSelected.id, 'maternity_breasfeeding_complementary', thirdSelected.maternity_complementary_full.id)" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Extendida:</label>
                            <SelectChoice :choiceType="'MATERNITY_EXTEND_CHOICES'"
                                v-model="thirdSelected.maternity_extend_full"
                                @change="saveItem(thirdSelected.id, 'maternity_breasfeeding_extend', thirdSelected.maternity_extend_full.id)" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Embarazo:</label>
                            <SelectChoice :choiceType="'MATERNITY_PREGNANCY_CHOICES'"
                                v-model="thirdSelected.maternity_pregnancy_full"
                                @change="saveItem(thirdSelected.id, 'maternity_pregnancy', thirdSelected.maternity_pregnancy_full.id)" />
                        </div>
                        <div>
                            <label class="block text-sm font-medium text-gray-700">Violencia:</label>
                            <SelectChoice :choiceType="'MATERNITY_VIOLANCE_CHOICES'"
                                v-model="thirdSelected.maternity_violance_full"
                                @change="saveItem(thirdSelected.id, 'maternity_violence', thirdSelected.maternity_violance_full.id)" />
                        </div>
                    </div>
                </div>
                <div class="grid grid-cols-1 gap-4 md:grid-cols-1 mt-4">
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Correo:</label>
                        <UInput v-model="thirdSelected.email"
                            @change="saveItem(thirdSelected.id, 'email', thirdSelected.email)" />
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700">Direccion:</label>
                        <UInput v-model="thirdSelected.address"
                            @change="saveItem(thirdSelected.id, 'address', thirdSelected.address)" />
                    </div>
                </div>
            </div>
        </div>
    </UModal>
</template>

<script lang="ts" setup>

const thirdSelected = ref({} as Third[])

type Props = {
    third: any
}

const props = defineProps<Props>()

const close = defineEmits(['close'])

watch(() => props.third, async (value: any) => {
    thirdSelected.value = value
    thirdSelected.value.type_full = await getCHOICE(value.type, 'TYPE_CHOICES')
    thirdSelected.value.sex_full = await getCHOICE(value.sex, "SEX_CHOICES")
    thirdSelected.value.blood_full = await getCHOICE(value.blood_type, "BLOOD_CHOICES")
    thirdSelected.value.etnia_full = await getCHOICE(value.ethnicity, "ETNIAS_CHOICES")
    thirdSelected.value.zone_full = await getCHOICE(value.zone, "ZONE_CHOICES")
    thirdSelected.value.status_full = await getCHOICE(value.status, "STATUS_CHOICES")
    thirdSelected.value.occupation_full = await getCHOICE(value.occupation, "OCCUPATION_CHOICES")
    thirdSelected.value.maternity_full = await getCHOICE(value.maternity_breasfeeding, "MATERNITY_CHOICES")
    thirdSelected.value.maternity_complementary_full = await getCHOICE(value.maternity_breasfeeding_complementary, "MATERNITY_COMPLEMENTARY_CHOICES")
    thirdSelected.value.maternity_extend_full = await getCHOICE(value.maternity_breasfeeding_extend, "MATERNITY_EXTEND_CHOICES")
    thirdSelected.value.maternity_pregnancy_full = await getCHOICE(value.maternity_pregnancy, "MATERNITY_PREGNANCY_CHOICES")
    thirdSelected.value.maternity_violance_full = await getCHOICE(value.maternity_violence, "MATERNITY_VIOLANCE_CHOICES")
    console.log('watch1', thirdSelected.value)
})

const autorized = ref(false)

const saveItem = async (index: number, field: string, value: string) => {
    autorized.value = await validatePermissions('thirds', 'change');
    if (!autorized.value) return
    const response = await $fetch(`api/thirds/${index}`, {
        method: 'PATCH',
        body: JSON.stringify({
            [field]: value,
        }),
    });
    console.log('saveItem', response)
};

</script>

<style></style>