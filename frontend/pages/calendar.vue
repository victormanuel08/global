<template>
    <ModalEditRecord :calendarEvent="calendarEvent" v-if="isOpen" />
    <div class="rounded-3xl bg-white mt-4 ml-4 mr-4 md:mt-2 md:ml-2 md:mr-2" v-else>
        <UCard class="m-4">
            <!-- <UButton @click="modalOpen.createSchedule = true">Nueva Programacion / Agendar</UButton> -->
            <div class="flex items-center justify-center border-solid m-4">
                <strong>AGENDAMIENTO DE CITAS GLOBAL SAFE IPS</strong>
            </div>
            <div class="flex items-center justify-center border-solid">

                <SelectThird 
                    :third-type="'P'" 
                    class="border rounded p-1 w-28" 
                    v-model="newScheduledPatient"
                    @change="saveItem(selectedEventId, 'third_patient', newScheduledPatient.id)" >
                </SelectThird>

                <SelectInsurance
                    v-model="newScheduledInsurance" class="border rounded p-1 w-60"
                    :third="newScheduledPatient.id"
                    @change="saveItem(selectedEventId, 'insurance', newScheduledInsurance.id)"
                    v-if="newScheduledPatient"
                    :placeholder="'Aseguradora'"
                >
                </SelectInsurance>
                <SelectSpecialities 
                    v-model="newScheduledSpeciality" 
                    class="border rounded p-1 w-60"
                    @change="saveItem(selectedEventId, 'speciality', newScheduledSpeciality.id)"  
                    v-if="newScheduledInsurance"                 
                >
                </SelectSpecialities>
                <SelectThird 
                    class="border rounded p-1 w-28" 
                    :third-type="'M'" 
                    :specialities="newScheduledSpeciality"
                    v-model="newScheduledMedic"
                    @change="saveItem(selectedEventId, 'third_medic', newScheduledMedic.id)"
                    v-if="newScheduledSpeciality"
                >
                </SelectThird>
                <SelectOptionsDate 
                    v-model="newScheduledOptions" 
                    class="border rounded p-1 w-80"
                    :third="newScheduledMedic" 
                    @change="saveItem(selectedEventId, 'date', newScheduledOptions.date)"
                >
                </SelectOptionsDate>
                <USelectMenu 
                    v-model="newScheduledOptionsHours" 
                    class="border rounded p-1 w-40" 
                    :class="{
                      'border rounded p-1 w-56': newScheduledSpeciality.code === '012',
                      'border rounded p-1 w-40': newScheduledSpeciality.code !== '012'
                    }"
                    :options="rangehours"
                    option-attribute="inter"
                    @change="saveItem(selectedEventId, 'time', newScheduledOptionsHours.time_start)" 
                    :placeholder="'Hora'"
                    v-if = "newScheduledOptions"
                />
                <span v-if="isEdit" @click="clean()" class="p-4 cursor-pointer" title="Limpiar Campos">
                    🧹
                </span>   
                <span v-else @click="createScheduled" class="p-4 cursor-pointer" title="Agendar Cita">
                    💾
                </span>
            </div>         
            <FullCalendar :options="calendarOptions" />
        </UCard>
    </div>
    
</template>

<script setup lang="ts">
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
import timeGridPlugin from '@fullcalendar/timegrid'



const newScheduledSpeciality = ref<any>('');
const isEdit = ref(false);
const newScheduledMedic = ref<any>('');
const newScheduledOptions = ref<any>('');
const newScheduledOptionsHours = ref<any>('');
const newScheduledDate = ref<any>(getCurrentDate());
const newScheduledTime = ref<any>(getCurrentTime());
const newScheduledPatient = ref<any>('');
const newScheduledInsurance = ref<any>(0);
const newScheduledRecord = ref<any>('');
const query = ref('');
const rangehours = ref<any[]>([]);
const selectedEventId = ref<number>(0);
const originalScheduleds = ref<any[]>([]);
const calendarEvent = ref<any>({});
const calendarInitialView = ref('dayGridMonth');//timeGridDay);dayGridMonth
const isOpen = ref(false)
const eventsToShow = ref<any[]>([
]);

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
            editRecord(calendarEvent.value)
        }else{
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
            record:scheduled.record,
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
                speciality: newScheduledSpeciality.value.id,
                third_patient: newScheduledPatient.value.id,
                third_medic: newScheduledMedic.value.id,
                confirmed: false,
                insurance: newScheduledInsurance.value.insurance,
                date_origin: newScheduledInsurance.value?.date, // Se agrega el campo date_origin si lo tiene newScheduledInsurance
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
        console.log("rangos", newVal.rangetime)
        calendarInitialView.value = "timeGridDay";
        console.log("calendar", calendarOptions.value)

        await fetchScheduleds();    
        
        if (newScheduledOptionsHours.value.overflow > 0) {
            const timeList = eventsToShow.value.map(item => item.time);
            console.log ('timelist', timeList)
            newVal.rangetime = newVal.rangetime.filter(item => !timeList.includes(item.time_start));
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
            console.log('calendarInitialView', newView)
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
    
    console.log('watch1', calendarEvent.value)    
    isOpen.value = true;
    console.log('calendarEvent', calendarEvent.value)
};



</script>

<style></style>