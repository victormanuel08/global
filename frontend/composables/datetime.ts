

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

  export const getCHOICE = async (value: string, choices: string) => {
    if (!value) {
      return [];
    }
    const response = await $fetch<any>(`api/api/choices/${choices}/${value}`);

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
      
      const response = await $fetch<any>(`/api/user/`, {
        method: 'GET',
        query: {
          value: val,
        }
  
      });
  
      return response;
    }

  export const listDaysOptions = (date: any, enddate: any) => {
    const options = [];

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
