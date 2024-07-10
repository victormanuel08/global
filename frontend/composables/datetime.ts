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
  const parsedDate = new Date(date);
  const year = parsedDate.getFullYear();
  const month = (parsedDate.getMonth() + 1).toString().padStart(2, '0');
  const day = parsedDate.getDate().toString().padStart(2, '0');
  return `${year}-${month}-${day}`;
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



export const rangeHours = (time: number, quota: number, start: string, end:string) => {
  // Validar la entrada validateInput(time, quota, start, end);  
  const hours = [];
  let currentHour = start; // Inicializar con la hora de inicio

  for (let i = 0; i < time; i++) {
    // Agregar la hora actual al arreglo
    hours.push({
      id: i + 1, // Usar índice + 1 como ID
      name: currentHour,
    });

    // Calcular la siguiente hora
    const [hour, minutes] = currentHour.split(':');
    const nextHour = parseInt(hour, 10) + 1;
    currentHour = `${nextHour}:${minutes}`;

    // Si llegamos a la hora de finalización, detener el bucle
    if (currentHour === end) {
      break;
    }
  }

  return hours;
};


export const listDaysOptions = (date: any, enddate: any) => {
  const options = [];
  console.log('fechas', date, enddate)
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
