
export default function useGeoLocation() {
    // Asegúrate de inicializar location como null
    const location: { latitude: number | null; longitude: number | null } = {
        latitude: null,
        longitude: null,
    };

    // Luego, en tu función getLocation, asigna los valores correctamente:
    const getLocation = async () => {
        try {
            if (navigator.geolocation) {
                const position = await new Promise<GeolocationPosition>((resolve, reject) => {
                    navigator.geolocation.getCurrentPosition(resolve, reject);
                });

                location.latitude = position.coords.latitude;
                location.longitude = position.coords.longitude;
            } else {
                console.error('Geolocalización no está disponible en este navegador.');
            }
        } catch (err) {
            if (err instanceof Error) {
                // 'err' es de tipo 'Error'
                //console.error('Error al obtener la ubicación:', err.message);
                //toast.add({title: 'Error al obtener la ubicación ', description: err.message})
            } else {
                console.error('Error desconocido:', err);
            }
        }
        onMounted(() => {
            getLocation();
        });

        return {
            location,
            getLocation,
        };

    };
}

// Finalmente, devuelve location y getLocation desde tu función:


