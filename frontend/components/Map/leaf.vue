<template>
    <div>
        <!-- Contenedor del mapa -->
        <div ref="map" class="map-container"></div>

        <!-- Modal para agregar accidente -->
        <div v-if="showModal" class="modal-overlay">
            <div class="modal-content">
                <h2>Agregar Accidente</h2>
                
                <!-- Formulario para agregar accidente -->
                <form @submit.prevent="handleAddAccident">
                    <!-- Tipo de Vehículo -->
                    <div class="form-group">
                        <label for="vehicle-type">Tipo de Vehículo:</label>
                        <select id="vehicle-type" v-model="accidentForm.vehicle_type">
                            <option v-for="(label, key) in vehicleTypeChoices" :key="key" :value="key">
                                {{ label }}
                            </option>
                        </select>
                    </div>

                    <!-- Medio -->
                    <div class="form-group">
                        <label for="half">Medio:</label>
                        <select id="half" v-model="accidentForm.half">
                            <option v-for="(label, key) in halfChoices" :key="key" :value="key">
                                {{ label }}
                            </option>
                        </select>
                    </div>

                    <!-- Causa Externa -->
                    <div class="form-group">
                        <label for="external-cause">Causa Externa:</label>
                        <select id="external-cause" v-model="accidentForm.external_cause">
                            <option v-for="(label, key) in externalCauseChoices" :key="key" :value="key">
                                {{ label }}
                            </option>
                        </select>
                    </div>

                    <!-- Descripción -->
                    <div class="form-group">
                        <label for="description">Descripción:</label>
                        <input type="text" id="description" v-model="accidentForm.description"
                            placeholder="Descripción del accidente" />
                    </div>

                    <!-- Acciones del modal -->
                    <div class="modal-actions">
                        <button type="submit">Aceptar</button>
                        <button type="button" @click="closeModal">Cancelar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import L from 'leaflet';

const map = ref<HTMLElement | null>(null);
const showModal = ref(false);
const accidentForm = ref({
    latitude: 0,
    longitude: 0,
    vehicle_type: '',
    half: '',
    external_cause: '',
    description: '',
});

const accidents = ref<any[]>([]);
const vehicles = ref<any[]>([]);
const accidentMarkers: L.Marker[] = [];
const vehicleMarkers: L.Marker[] = [];

// Opciones para los select
const vehicleTypeChoices = {    
    AU: 'AUTOMÓVIL',
    MO: 'MOTO',
    CA: 'CAMIONETA',
    BU: 'BUS',
    OT: 'OTRO',
};
const halfChoices = {
    TE: 'TELEFÓNICO',
    RA: 'RADIO',
    PE: 'PERSONAL',
    OB: 'OBSERVADO',
};
const externalCauseChoices = {
    GE: 'ENF GENERAL',
    CA: 'ACCIDENTE COMÚN',
    TA: 'ACCIDENTE DE TRÁNSITO',
    AG: 'LESIÓN POR AGRESIÓN',
    AU: 'LESIÓN AUTOINFLIGIDA',
    LA: 'ACCIDENTE LABORAL',
    RB: 'ACCIDENTE RÁBICO',
    OT: 'OTRO',
};

// Función para mostrar la modal con coordenadas
const openModal = (lat: number, lng: number) => {
    accidentForm.value.latitude = parseFloat(lat.toFixed(6)); 
    accidentForm.value.longitude = parseFloat(lng.toFixed(6)); 
    showModal.value = true;
};

const closeModal = () => {
    showModal.value = false;
};

// Manejar el envío del formulario
const handleAddAccident = async () => {
  try {
    const response = await fetch('/api/accidents/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(accidentForm.value),
    });

    if (response.ok) {
      const newAccident = await response.json();
      //console.log('Accidente agregado:', newAccident);

      // Agregar el nuevo accidente al arreglo de accidentes
      accidents.value.push(newAccident);

      // Obtener las coordenadas del accidente
      const lat = parseFloat(newAccident.latitude);
      const lng = parseFloat(newAccident.longitude);

      // Verificar si el mapa ya está inicializado
      const myMap = map.value && (map.value as HTMLElement).__leafletMap;

      if (myMap && !isNaN(lat) && !isNaN(lng)) {
        // Agregar el marcador de este accidente en el mapa
        const marker = L.marker([lat, lng]).addTo(myMap)
          .bindPopup(`
            <strong>Descripción:</strong> ${newAccident.description || 'N.A.'}<br>
            <strong>Tipo de vehículo:</strong> ${vehicleTypeChoices[newAccident.vehicle_type] || 'N.A.'}<br>
            <strong>Medio:</strong> ${halfChoices[newAccident.half] || 'N.A.'}<br>
            <strong>Causa Externa:</strong> ${externalCauseChoices[newAccident.external_cause] || 'N.A.'}
          `);
        
        // Agregar el marcador a la lista de marcadores
        accidentMarkers.push(marker);
      }

      closeModal(); // Cerrar la modal después de agregar el accidente
    } else {
      console.error('Error al agregar accidente:', await response.text());
    }
  } catch (error) {
    console.error('Error en la solicitud:', error);
  }
};

// Obtener los accidentes
const fetchAccidents = async () => {
    try {
        const response = await fetch('/api/accidents/allday/');
        const data = await response.json();
        accidents.value = data;
    } catch (error) {
        console.error('Error al obtener accidentes:', error);
    }
};

// Obtener los vehículos
const fetchVehicles = async () => {
    try {
        const response = await fetch('/api/vehicles/?vehicle_type=AM');
        const data = await response.json();
        vehicles.value = data.results;
    } catch (error) {
        console.error('Error al obtener vehículos:', error);
    }
};

// Añadir accidentes al mapa
const addAccidentsToMap = (myMap: L.Map) => {
    accidents.value.forEach(accident => {
        const lat = parseFloat(accident.latitude);
        const lng = parseFloat(accident.longitude);
        if (!isNaN(lat) && !isNaN(lng)) {
            // Traducción de los valores
            const vehicleType = vehicleTypeChoices[accident.vehicle_type] || 'N.A.';
            const half = halfChoices[accident.half] || 'N.A.';
            const externalCause = externalCauseChoices[accident.external_cause] || 'N.A.';
            
            // Crear el marcador con la información traducida
            const marker = L.marker([lat, lng]).addTo(myMap)
                .bindPopup(`
                    <strong>Descripción:</strong> ${accident.description || 'N.A.'}<br>
                    <strong>Tipo de vehículo:</strong> ${vehicleType}<br>
                    <strong>Medio:</strong> ${half}<br>
                    <strong>Causa Externa:</strong> ${externalCause}
                `);
            accidentMarkers.push(marker);
        }
    });
};

// Añadir vehículos al mapa
const addVehiclesToMap = (myMap: L.Map) => {
    vehicles.value.forEach(vehicle => {
        const lat = parseFloat(vehicle.latitude);
        const lng = parseFloat(vehicle.longitude);
        if (!isNaN(lat) && !isNaN(lng)) {
            const marker = L.marker([lat, lng], {
                icon: L.icon({
                    iconUrl: 'https://img.icons8.com/ios/452/ambulance.png',
                    iconSize: [32, 32],
                    iconAnchor: [16, 32],
                })
            }).addTo(myMap)
                .bindPopup(`
            <strong>Movil:</strong> ${vehicle.placamovil || 'N.A.'}
          `);
            vehicleMarkers.push(marker);
        }
    });
};

// Limpiar los marcadores del mapa
const clearMarkers = () => {
    accidentMarkers.forEach(marker => marker.remove());
    accidentMarkers.length = 0;

    vehicleMarkers.forEach(marker => marker.remove());
    vehicleMarkers.length = 0;
};

// Inicializar el mapa
const initMap = (container: HTMLElement) => {
    const myMap = L.map(container, {
        center: [7.8898, -72.5078],
        zoom: 13,
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(myMap);

    myMap.on('contextmenu', (e: any) => {
        const { lat, lng } = e.latlng;
        alert(`Coordenadas: ${lat}, ${lng}`);
        openModal(lat, lng);
    });

    return myMap;
};

// Actualizar posiciones cada 60 segundos
const updatePositions = (myMap: L.Map) => {
    setInterval(async () => {
        await fetchAccidents();
        await fetchVehicles();
        clearMarkers();
        addAccidentsToMap(myMap);
        addVehiclesToMap(myMap);
    }, 60000);
};

// Inicializar el mapa al montar el componente
onMounted(async () => {
    await fetchAccidents();
    await fetchVehicles();
    if (map.value) {
        const myMap = initMap(map.value);
        addAccidentsToMap(myMap);
        addVehiclesToMap(myMap);
        updatePositions(myMap);
    }
});
</script>


<style scoped>
@import url('https://unpkg.com/leaflet@1.9.3/dist/leaflet.css');

.map-container {
    width: 100%;
    height: 400px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
}

/* Estilos del modal */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Contenido del modal */
.modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    width: 80%;
    max-width: 500px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Estilos de los campos del formulario */
.form-group {
    margin-bottom: 15px;
}

label {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
    display: block;
}

select, input[type="text"] {
    width: 100%;
    padding: 8px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Estilos de los botones de acción */
.modal-actions {
    display: flex;
    justify-content: space-between;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: white;
}

button[type="submit"]:hover {
    background-color: #45a049;
}

button[type="button"] {
    background-color: #f44336;
    color: white;
}

button[type="button"]:hover {
    background-color: #e53935;
}
</style>