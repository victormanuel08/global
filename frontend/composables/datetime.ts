

export const getCurrentDate = () => {
  const date = new Date()
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  return `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`
}

export const getCurrentTime = () => {
  const date = new Date()
  const hours = date.getHours()
  const minutes = date.getMinutes()
  const seconds = date.getSeconds()
  return `${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}:${seconds < 10 ? '0' + seconds : seconds}`
}

export const formatDate = (date: string) => {
  const [year, month, day] = date.split('-')
  return `${day}/${month}/${year}`
}

export const formatDateYYYYMMDD = (date: string): string => {
  console.log(date);
  
  // Verificar si la fecha está en formato ISO
  if (date.includes('T')) {
    const parsedDate = new Date(date);
    const formattedYear = parsedDate.getFullYear();
    const formattedMonth = (parsedDate.getMonth() + 1).toString().padStart(2, '0');
    const formattedDay = parsedDate.getDate().toString().padStart(2, '0');
    return `${formattedYear}-${formattedMonth}-${formattedDay}`;
  }

  // Manejar fechas separadas por '/' o '-'
  const [day, month, year] = date.split(/[-\/]/);
  const parsedDate = new Date(Number(year), Number(month) - 1, Number(day));
  const formattedYear = parsedDate.getFullYear();
  const formattedMonth = (parsedDate.getMonth() + 1).toString().padStart(2, '0');
  const formattedDay = parsedDate.getDate().toString().padStart(2, '0');
  return `${formattedYear}-${formattedMonth}-${formattedDay}`;
};



export const formatDateYYYY0101 = (date: string): string => {
  const parsedDate = new Date(date);
  const year = parsedDate.getFullYear();
  return `${year}-01-01`;
};

export const formatDateHHMMSS = (date: string): string => {
  const parsedDate = new Date(date);
  const hours = parsedDate.getHours().toString().padStart(2, '0');
  const minutes = parsedDate.getMinutes().toString().padStart(2, '0');
  const seconds = parsedDate.getSeconds().toString().padStart(2, '0');
  return `${hours}:${minutes}:${seconds}`;
};

export const formatDateTime = (datetime: string) => {
  const options = {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    timeZoneName: 'short',
  };

  const formattedDateTime = new Date(datetime).toLocaleString('es-CO', options);
  return formattedDateTime;
};

//export const getCHOICE = async (value: string, choices: string) => {
//  if (!value) {
//    return [];
//  }
//  const response = await $fetch<any>(`api/api/choices/${choices}/${value}`);
//
//  return response;
//};

import { useCookie } from 'nuxt/app';

export const getCHOICE = async (value: string, choices: string) => {
  if (!value) {
    return [];
  }

  const storageKey = `choices_${choices}_${value}`;
  let storedData = localStorage.getItem(storageKey);

  console.log("Datos almacenados en localStorage:", storedData);

  if (!storedData) {
    const cookie = useCookie(storageKey);
    storedData = cookie.value ?? null;
    console.log("Datos obtenidos de la cookie:", storedData);
  }

  if (storedData) {
   
    return JSON.parse(storedData);
  }

  const response = await $fetch<any>(`api/api/choices/${choices}/${value}`);
  console.log("Datos obtenidos de la API:", response);

  localStorage.setItem(storageKey, JSON.stringify(response));
  const cookie = useCookie(storageKey);
  cookie.value = JSON.stringify(response);

  return response;
};



export const getBODYPART = async (value: number, choices: string, field: string) => {
  const response = await $fetch<any>(`/api/api/choices/${choices}/${value}/${field}`);

  return response;
};


export const getAddress = async (lat: string): Promise<string> => {
  const response = await $fetch<any>(`/api/geocode/?coordinates=${lat}`);
  const response2 = await $fetch<any>(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${newLocation.latitude}&lon=${newLocation.longitude}&zoom=18&addressdetails=1`)
  // address.value = response.display_name
  return response;
};


export const getVALUE = async (val: string, year: string) => {

  const response = await $fetch<any>(`/api/values/`, {
    method: 'GET',
    query: {
      value: val,
      year_date: year
    }

  });

  return response;
}



export const getuser = async (val: string) => {
  if (!val) {
    return null;
  }

  // Crear una clave de almacenamiento basada en el valor
  const storageKey = `user_${val}`;

  // Intentar obtener los datos almacenados desde el almacenamiento local
  let storedData = localStorage.getItem(storageKey);

  // Si los datos no están en el almacenamiento local, intentar obtenerlos desde la cookie
  if (!storedData) {
    const cookie = useCookie(storageKey);
    storedData = cookie.value ?? null;
  }

  // Si los datos están en el almacenamiento, devolverlos
  if (storedData) {
    return JSON.parse(storedData);
  }

  // Si no están en el almacenamiento, hacer la consulta
  const response = await $fetch<any>(`/api/user/`, {
    method: 'GET',
    query: {
      value: val,
    }
  });

  // Guardar los datos en el almacenamiento local y en la cookie
  localStorage.setItem(storageKey, JSON.stringify(response));
  const cookie = useCookie(storageKey);
  cookie.value = JSON.stringify(response);

  return response;
};


export const listDaysOptions = (date: any, enddate: any) => {
  const options = [];
  //console.log("listDayOprons control",date, enddate);
  const allDates = getDatesInRange(date, enddate);
  if (allDates.length > 0) {
    options.push({
      id: 0,
      name: 'TODOS LOS DÍAS',
      days: allDates.join(', ')
    });
  }

  const weekdays = ['Domingos', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábados'];
  for (let i = 0; i < weekdays.length; i++) {
    const dayName = weekdays[i];
    const dayDates = getWeekdayDatesInRange(date, enddate, i);
    if (dayDates.length > 0) {
      options.push({
        id: i + 1,
        name: dayName,
        days: dayDates.join(', ')
      });
    }
  }

  return options;
};

// Función para obtener fechas dentro del rango
const getDatesInRange = (startDate: any, endDate: any) => {
  const dates = [];
  //console.log("getDatesInRange control",startDate, endDate);
  const currentDate = new Date(startDate + 'T00:00:00');
  const endDate2 = new Date(endDate + 'T00:00:00');
  while (currentDate <= endDate2) {
    dates.push(currentDate.toLocaleDateString());
    currentDate.setDate(currentDate.getDate() + 1);
  }
  return dates;
};

// Función para obtener fechas específicas de un día de la semana dentro del rango
const getWeekdayDatesInRange = (startDate: any, endDate: any, weekdayIndex: any) => {
  const dates = [];
  //console.log("getWeekdayDatesInRange control",startDate, endDate, weekdayIndex);
  const currentDate = new Date(startDate + 'T00:00:00');
  const endDate2 = new Date(endDate + 'T00:00:00');
  while (currentDate <= endDate2) {
    if (currentDate.getDay() === weekdayIndex) {
      dates.push(currentDate.toLocaleDateString());
    }
    currentDate.setDate(currentDate.getDate() + 1);
  }
  return dates;
};


export const calculateAge = (dateString: string) => { 
  const birthDate = new Date(dateString);
  const today = new Date();

  let years = today.getFullYear() - birthDate.getFullYear();
  let months = today.getMonth() - birthDate.getMonth();
  let days = today.getDate() - birthDate.getDate();
  
  if (days < 0) {
    months--;
    days += new Date(today.getFullYear(), today.getMonth(), 0).getDate();
  }
  if (months < 0) {
    years--;
    months += 12;
  }

  return  years + " Años, " + months + " Meses y " + days + " dias";
};

