<template>
    <ModalEditRecord :calendarEvent="calendarEvent" v-if="isOpen" />
    <div class="rounded-3xl bg-white mt-4 ml-4 mr-4 md:mt-2 md:ml-2 md:mr-2" v-else>
        <UCard class="m-4">
            <!-- <UButton @click="modalOpen.createSchedule = true">Nueva Programacion / Agendar</UButton> -->
            <div class="flex items-center justify-center border-solid m-4">
                <strong>AGENDAMIENTO DE CITAS GLOBAL SAFE IPS</strong>
            </div>
            <div class="flex flex-cols-4 justify-center border-solid mt-4 mb-4">
                <div>
                    <label class="font-bold">Paciente: <span @click="typeT = 'P', showModalThird('')">➕</span></label>
                    <SelectThird :third-type="'P'" class="border rounded p-1 w-64" v-model="newScheduledPatient"
                        @change="saveItem(selectedEventId, 'third_patient', newScheduledPatient.id)">
                    </SelectThird>
                </div>
                <div v-if="newScheduledPatient">
                    <label class="font-bold">
                        Polizas:<span @click="typeT = 'E', showModalPolice()">➕</span>
                    </label>
                    <SelectInsurance v-model="newScheduledInsurance" class="border rounded p-1 w-96"
                        :third="newScheduledPatient.id"
                        @change="saveItem(selectedEventId, 'insurance', newScheduledInsurance.id)"
                        :placeholder="'Aseguradora'">
                    </SelectInsurance>
                </div>
                <!--
                <div v-if="newScheduledInsurance.insurance === 1">
                    <label class="font-bold">Entidad</label>
                    <SelectThird v-model="newScheduledEntity" :third-type="'E'" class="border rounded p-1 w-64"
                        @change="saveItem(selectedEventId, 'third_entity', newScheduledEntity.id)">
                    </SelectThird>
                </div>
                -->
                <div v-if="newScheduledInsurance">
                    <label class="font-bold">Especialidad</label>
                    <SelectSpecialities v-model="newScheduledSpeciality"
                        :specialities="newScheduledInsurance.specialities" class="border rounded p-1 w-64"
                        @change="console.log(newScheduledSpeciality)">
                    </SelectSpecialities>
                </div>
                <div v-if="newScheduledSpeciality.code === '012'">
                    <label class="font-bold">Historia (Consultas)</label>
                    <SelectInsuranceHistory v-model="newScheduledInsuranceHistory" class="border rounded p-1 w-96"
                        :third="newScheduledPatient.id"
                        @change="saveItem(selectedEventId, 'insurance', newScheduledInsurance.id)"
                        :placeholder="'Aseguradora'" />
                </div>
            </div>

            <div class="flex grid-cols-4 justify-center border-solid mt-4 mb-4">
                <div v-if="newScheduledSpeciality">
                    <label class="font-bold">Servicios</label>
                    <SelectServices v-model="newScheduledService" :third="newScheduledEntity"
                        class="border rounded p-1 w-72" :specialities="newScheduledSpeciality"
                        :services="newScheduledInsurance.services"
                        @change="saveItem(selectedEventId, 'service', newScheduledService.id)">
                    </SelectServices>
                </div>
                <!--
                <div v-if="newScheduledService && newScheduledInsurance.insurance === 1">
                    <label class="font-bold">Contrato</label>
                    <div class="border rounded p-1 w-64">
                        <SelectFeed v-model="newScheduledFee" :third="newScheduledEntity"
                            :specialities="newScheduledSpeciality" :service="newScheduledService"
                            @change="saveItem(selectedEventId, 'fee', newScheduledFee.id)">
                        </SelectFeed>
                    </div>
                </div>
                -->
                <div v-if="newScheduledFee || newScheduledService">
                    <label class="font-bold">Medico</label>
                    <SelectThird class="border rounded p-1 w-64" :third-type="'M'"
                        :specialities="newScheduledSpeciality" v-model="newScheduledMedic"
                        @change="saveItem(selectedEventId, 'third_medic', newScheduledMedic.id)">
                    </SelectThird>
                </div>
                <div v-if="newScheduledMedic">
                    <label class="font-bold">Fecha</label>
                    <SelectOptionsDate v-model="newScheduledOptions" class="border rounded p-1 w-64"
                        :third="newScheduledMedic"
                        @change="saveItem(selectedEventId, 'date', newScheduledOptions.date)">
                    </SelectOptionsDate>
                </div>
                <div v-if="newScheduledMedic">
                    <label class="font-bold">Disponibilidad</label>
                    <USelectMenu v-model="newScheduledOptionsHours" class="border rounded p-1 w-64"
                        :options="rangehours" option-attribute="inter"
                        @change="saveItem(selectedEventId, 'time', newScheduledOptionsHours.time_start)"
                        :placeholder="'Hora'" v-if="newScheduledOptions" />
                </div>
                <div v-if="newScheduledOptionsHours">
                    <label class="font-bold">Accion</label>
                    <div>
                        <span v-if="isEdit" @click="clean()" class="p-4 cursor-pointer" title="Limpiar Campos">
                            🧹
                        </span>
                        <span v-else @click="createScheduled" class="p-4 cursor-pointer" title="Agendar Cita">
                            💾
                        </span>
                    </div>
                </div>
            </div>
            <FullCalendar :options="calendarOptions" />
        </UCard>
    </div>
    <ModalNewPolice :third="newScheduledPatient" :typeT="'C'" @close="handleModalClose" v-model="isPolice" />
    <ModalEditThird :typeT="typeT" v-model="isThird" />
</template>

<script setup lang="ts">
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
import timeGridPlugin from '@fullcalendar/timegrid'




const newScheduledSpeciality = ref<any>('');
const isEdit = ref(false);
const isThird = ref(false);
const typeT = ref('')
const isPolice = ref(false)
const newScheduledMedic = ref<any>('');
const newScheduledOptions = ref<any>('');
const newScheduledOptionsHours = ref<any>('');
const newScheduledDate = ref<any>(getCurrentDate());
const newScheduledInsuranceHistory = ref<any>({});
const newScheduledTime = ref<any>(getCurrentTime());
const newScheduledPatient = ref<any>('');
const newScheduledInsurance = ref<any>(0);
const newScheduledRecord = ref<any>('');
const newScheduledEntity = ref<any>('');
const newScheduledService = ref<any>('');
const newScheduledFee = ref<any>('');
const query = ref('');
const rangehours = ref<any[]>([]);
const selectedEventId = ref<number>(0);
const originalScheduleds = ref<any[]>([]);
const calendarEvent = ref<any>({});
const calendarInitialView = ref('dayGridMonth');//timeGridDay);dayGridMonth
const isOpen = ref(false)
const eventsToShow = ref<any[]>([
]);


const showModalThird = (value: any) => {

    isThird.value = true

}

const calendarOptions = computed(() => ({
    plugins: [dayGridPlugin, interactionPlugin, timeGridPlugin],
    initialView: calendarInitialView.value,
    locale: 'es',
    headerToolbar: {
        left: 'prev,next',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay' // user can switch between the two
    },
    buttonText: {
        day: "Hoy",
        month: "Mes",
        week: "Semana",
        dayGridMonth: "Mes",
        timeGridWeek: "Semana",
        timeGridDay: "Día",
    },
    //location: "es-Es",
    events: eventsToShow.value,
    eventClick: function (info: any) {
        if (info.event.extendedProps.record) {
            newScheduledRecord.value = info.event.extendedProps.record;
            calendarEvent.value = info.event.extendedProps;
            console.log('calendarEvent', calendarEvent.value)
        } else {
            selectedEventId.value = info.event.extendedProps.scheduled;
            newScheduledPatient.value = info.event.extendedProps.patient;
            newScheduledSpeciality.value = info.event.extendedProps.speciality;
            newScheduledMedic.value = info.event.extendedProps.medic;
            newScheduledDate.value = info.event.extendedProps.date;
            newScheduledTime.value = info.event.extendedProps.time;
            //modalOpen.createSchedule = true;
            isEdit.value = true;
            alert("Puedes editar la cita");
        }
    },
}));

type Scheduled = {
    id: number
    date: string
    time: string
    insurance: number
    date_origin: string
    third_patient_full: {
        name: string
        second_name: string
        last_name: string
        second_last_name: string
    }
    confirmed: boolean
    speciality: number
    record: number
    third_medic_full: {
        id: number
        name: string
        second_name: string
        last_name: string
        second_last_name: string
    }
    speciality_full: {
        id: number
        description: string
    }
};

async function fetchScheduleds() {
    try {
        const queryParams = {
            search: query.value,
            speciality: newScheduledSpeciality.value ? newScheduledSpeciality.value.id : null,
            third_medic: newScheduledMedic.value ? newScheduledMedic.value.id : null,
            date: newScheduledDate.value ? newScheduledOptions.value.date : null
        }
        const response = await $fetch<any>("api/scheduleds", {
            query: queryParams,
        });
        eventsToShow.value = [];

        eventsToShow.value = response.results.map((scheduled: Scheduled) => ({
            title: scheduled.third_patient_full.name + ' ' + scheduled.third_patient_full.second_name + ' ' + scheduled.third_patient_full.last_name + ' ' + scheduled.third_patient_full.second_last_name,
            start: scheduled.date + "T" + scheduled.time + "-05:00",
            end: scheduled.date + "T" + scheduled.time + "-05:00",
            speciality: scheduled.speciality_full,
            medic: scheduled.third_medic_full,
            patient: scheduled.third_patient_full,
            scheduled: scheduled.id,
            record: scheduled.record,
            date: scheduled.date,
            time: scheduled.time,
            color: scheduled.confirmed ? 'green' : 'red',
        }));

    } catch (error) {
        console.error('Error al cargar los datos:', error);
    }
}

onMounted(() => {
    fetchScheduleds()
});

const clean = async () => {
    newScheduledDate.value = getCurrentDate();
    newScheduledTime.value = getCurrentTime();
    newScheduledSpeciality.value = '';
    newScheduledPatient.value = '';
    newScheduledMedic.value = '';
    newScheduledOptions.value = '';
    newScheduledOptionsHours.value = '';
    newScheduledInsurance.value = '';
    isEdit.value = false
    await fetchScheduleds();
    return;
}

const createScheduled = async () => {
    const message = confirm('¿Estás seguro de crear esta Cita?');
    if (!message) {
        clean();
    }

    try {

        const response = await $fetch('api/scheduleds/', {
            method: 'POST',
            body: {
                date: newScheduledOptions.value.date,
                time: newScheduledOptionsHours.value.time_start,
                speciality: newScheduledSpeciality.value.id, //???
                third_patient: newScheduledPatient.value.id,
                third_medic: newScheduledMedic.value.id,
                record: newScheduledInsuranceHistory.value?.record,
                confirmed: false,
                insurance: newScheduledInsurance.value.insurance,
                date_origin: newScheduledInsuranceHistory.value?.date_origin, // Se agrega el campo date_origin si lo tiene newScheduledInsurance
                third_entity: newScheduledInsuranceHistory.value?.third_entity,   /// ok
                service: newScheduledService.value?.id,
                fee: newScheduledFee.value?.id,
                policy: newScheduledInsurance.value?.id,   //???ok
            },
        });
        await fetchScheduleds();
        newScheduledDate.value = getCurrentDate();
        newScheduledTime.value = getCurrentTime();
        newScheduledSpeciality.value = '';
        newScheduledPatient.value = '';
        newScheduledMedic.value = '';
        newScheduledOptions.value = '';
        newScheduledOptionsHours.value = '';
        newScheduledInsurance.value = '';
        newScheduledEntity.value = '';
        newScheduledService.value = '';
        newScheduledFee.value = '';
    } catch (error) {
        console.error('Error al crear la cita:', error);
    }
};

const ui = {
    td: 'p-1 border',
    th: 'p-2 border',
    check: 'align-center justify-center',
    span: 'cursor-pointer'
}

watch(newScheduledOptions, async (newVal, oldVal) => {
    calendarInitialView.value = "timeGridDay";
    if (newVal) {
        //await fetchScheduleds();  

        calendarInitialView.value = "timeGridDay";


        await fetchScheduleds();

        if (newScheduledOptionsHours.value.overflow > 0) {
            const timeList = eventsToShow.value.map(item => item.time);

            newVal.rangetime = newVal.rangetime.filter((item: any) => !timeList.includes(item.time_start));
        }
        rangehours.value = newVal.rangetime
    } else {
        newScheduledOptionsHours.value = {}; // Vacía el arreglo si newScheduledOptions no tiene selección
    }
});

watch(
    [newScheduledSpeciality, newScheduledMedic],
    async ([newSpecialityVal, newMedicVal], [oldSpecialityVal, oldMedicVal]) => {
        if (newSpecialityVal || newMedicVal) {
            await fetchScheduleds();
        }
    }
);

watch(calendarInitialView,
    async (newView, oldView) => {
        if (newView) {

            await fetchScheduleds();
        }
    }
);


const saveItem = async (index: number, field: string, value: string) => {
    if (isEdit.value) {
        try {
            const apiUrl = `api/scheduleds/${index}`;
            const response = await $fetch(apiUrl, {
                method: 'PATCH',
                body: JSON.stringify({
                    [field]: value,
                }),
            });
            if (field == 'time') {
                clean();
            }
            alert("Se realizó el cambio exitosamente");
        } catch (error) {
            console.error('Error al actualizar el elemento:', error);
        }
        await fetchScheduleds();
    }
};

const editRecord = async (record: any) => {
    alert(`Puedes Hacer Evolucion de la Consulta Original`)
    calendarEvent.value = record;
    calendarEvent.value.patient.type_full = await getCHOICE(calendarEvent.value.patient.type, 'TYPE_CHOICES')
    calendarEvent.value.patient.sex_full = await getCHOICE(calendarEvent.value.patient.sex, "SEX_CHOICES")
    calendarEvent.value.patient.blood_full = await getCHOICE(calendarEvent.value.patient.blood_type, "BLOOD_CHOICES")
    calendarEvent.value.patient.etnia_full = await getCHOICE(calendarEvent.value.patient.ethnicity, "ETNIAS_CHOICES")
    calendarEvent.value.patient.zone_full = await getCHOICE(calendarEvent.value.patient.zone, "ZONE_CHOICES")
    calendarEvent.value.patient.occupation_full = await getCHOICE(calendarEvent.value.patient.occupation, "OCCUPATION_CHOICES")
    calendarEvent.value.patient.maternity_full = await getCHOICE(calendarEvent.value.patient.maternity_breasfeeding, "MATERNITY_CHOICES")
    calendarEvent.value.patient.maternity_complementary_full = await getCHOICE(calendarEvent.value.patient.maternity_breasfeeding_complementary, "MATERNITY_COMPLEMENTARY_CHOICES")
    calendarEvent.value.patient.maternity_extend_full = await getCHOICE(calendarEvent.value.patient.maternity_breasfeeding_extend, "MATERNITY_EXTEND_CHOICES")
    calendarEvent.value.patient.maternity_pregnancy_full = await getCHOICE(calendarEvent.value.patient.maternity_pregnancy, "MATERNITY_PREGNANCY_CHOICES")
    calendarEvent.value.patient.maternity_violance_full = await getCHOICE(calendarEvent.value.patient.maternity_violence, "MATERNITY_VIOLANCE_CHOICES")


    isOpen.value = true;

};

const showModalPolice = () => {

    isPolice.value = true
}

const handleModalClose = async (value: any) => {

    isPolice.value = false
    await fetchScheduleds()
}

</script>

<style></style>