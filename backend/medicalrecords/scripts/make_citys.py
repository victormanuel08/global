from medicalrecords.models import Cities
from users.models import User

cities_to_create = [       
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.001",
        "name": "Medellín"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.002",
        "name": "Abejorral"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.004",
        "name": "Abriaquí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.021",
        "name": "Alejandría"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.03",
        "name": "Amagá"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.031",
        "name": "Amalfi"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.034",
        "name": "Andes"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.036",
        "name": "Angelópolis"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.038",
        "name": "Angostura"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.04",
        "name": "Anorí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.832",
        "name": "Tununguá"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.044",
        "name": "Anza"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.045",
        "name": "Apartadó"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.051",
        "name": "Arboletes"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.055",
        "name": "Argelia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.059",
        "name": "Armenia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.079",
        "name": "Barbosa"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.088",
        "name": "Bello"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.091",
        "name": "Betania"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.093",
        "name": "Betulia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.101",
        "name": "Ciudad Bolívar"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.107",
        "name": "Briceño"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.113",
        "name": "Buriticá"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.12",
        "name": "Cáceres"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.125",
        "name": "Caicedo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.129",
        "name": "Caldas"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.134",
        "name": "Campamento"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.138",
        "name": "Cañasgordas"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.142",
        "name": "Caracolí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.145",
        "name": "Caramanta"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.147",
        "name": "Carepa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.476",
        "name": "Motavita"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.15",
        "name": "Carolina"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.154",
        "name": "Caucasia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.172",
        "name": "Chigorodó"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.19",
        "name": "Cisneros"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.197",
        "name": "Cocorná"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.206",
        "name": "Concepción"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.209",
        "name": "Concordia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.212",
        "name": "Copacabana"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.234",
        "name": "Dabeiba"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.237",
        "name": "Don Matías"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.24",
        "name": "Ebéjico"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.25",
        "name": "El Bagre"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.264",
        "name": "Entrerrios"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.266",
        "name": "Envigado"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.282",
        "name": "Fredonia"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.675",
        "name": "San Bernardo del Viento"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.306",
        "name": "Giraldo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.308",
        "name": "Girardota"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.31",
        "name": "Gómez Plata"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.361",
        "name": "Istmina"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.315",
        "name": "Guadalupe"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.318",
        "name": "Guarne"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.321",
        "name": "Guatapé"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.347",
        "name": "Heliconia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.353",
        "name": "Hispania"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.36",
        "name": "Itagui"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.361",
        "name": "Ituango"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.086",
        "name": "Belmira"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.368",
        "name": "Jericó"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.376",
        "name": "La Ceja"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.38",
        "name": "La Estrella"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.39",
        "name": "La Pintada"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.4",
        "name": "La Unión"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.411",
        "name": "Liborina"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.425",
        "name": "Maceo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.44",
        "name": "Marinilla"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.467",
        "name": "Montebello"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.475",
        "name": "Murindó"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.48",
        "name": "Mutatá"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.483",
        "name": "Nariño"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.49",
        "name": "Necoclí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.495",
        "name": "Nechí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.501",
        "name": "Olaya"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.541",
        "name": "Peñol"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.543",
        "name": "Peque"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.576",
        "name": "Pueblorrico"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.579",
        "name": "Puerto Berrío"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.585",
        "name": "Puerto Nare"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.591",
        "name": "Puerto Triunfo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.604",
        "name": "Remedios"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.607",
        "name": "Retiro"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.615",
        "name": "Rionegro"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.628",
        "name": "Sabanalarga"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.631",
        "name": "Sabaneta"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.642",
        "name": "Salgar"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.189",
        "name": "Ciénega"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.699",
        "name": "Santacruz"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.652",
        "name": "San Francisco"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.656",
        "name": "San Jerónimo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.575",
        "name": "Puerto Wilches"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.573",
        "name": "Puerto Parra"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.66",
        "name": "San Luis"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.664",
        "name": "San Pedro"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.667",
        "name": "San Rafael"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.67",
        "name": "San Roque"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.674",
        "name": "San Vicente"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.679",
        "name": "Santa Bárbara"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.69",
        "name": "Santo Domingo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.697",
        "name": "El Santuario"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.736",
        "name": "Segovia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.761",
        "name": "Sopetrán"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.37",
        "name": "Uribe"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.789",
        "name": "Támesis"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.79",
        "name": "Tarazá"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.792",
        "name": "Tarso"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.809",
        "name": "Titiribí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.819",
        "name": "Toledo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.837",
        "name": "Turbo"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.842",
        "name": "Uramita"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.847",
        "name": "Urrao"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.854",
        "name": "Valdivia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.856",
        "name": "Valparaíso"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.858",
        "name": "Vegachí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.861",
        "name": "Venecia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.885",
        "name": "Yalí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.887",
        "name": "Yarumal"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.89",
        "name": "Yolombó"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.893",
        "name": "Yondó"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.895",
        "name": "Zaragoza"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.001",
        "name": "Barranquilla"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.078",
        "name": "Baranoa"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.141",
        "name": "Candelaria"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.296",
        "name": "Galapa"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.421",
        "name": "Luruaco"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.433",
        "name": "Malambo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.436",
        "name": "Manatí"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.549",
        "name": "Piojó"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.558",
        "name": "Polonuevo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.634",
        "name": "Sabanagrande"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.638",
        "name": "Sabanalarga"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.675",
        "name": "Santa Lucía"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.685",
        "name": "Santo Tomás"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.758",
        "name": "Soledad"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.77",
        "name": "Suan"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.832",
        "name": "Tubará"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.849",
        "name": "Usiacurí"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.006",
        "name": "Achí"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.042",
        "name": "Arenal"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.052",
        "name": "Arjona"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.062",
        "name": "Arroyohondo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.14",
        "name": "Calamar"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.16",
        "name": "Cantagallo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.188",
        "name": "Cicuco"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.212",
        "name": "Córdoba"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.222",
        "name": "Clemencia"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.248",
        "name": "El Guamo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.43",
        "name": "Magangué"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.433",
        "name": "Mahates"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.44",
        "name": "Margarita"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.458",
        "name": "Montecristo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.468",
        "name": "Mompós"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.473",
        "name": "Morales"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.49",
        "name": "Norosí"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.549",
        "name": "Pinillos"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.58",
        "name": "Regidor"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.6",
        "name": "Río Viejo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.647",
        "name": "San Estanislao"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.65",
        "name": "San Fernando"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.657",
        "name": "San Juan Nepomuceno"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.673",
        "name": "Santa Catalina"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.683",
        "name": "Santa Rosa"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.744",
        "name": "Simití"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.76",
        "name": "Soplaviento"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.78",
        "name": "Talaigua Nuevo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.81",
        "name": "Tiquisio"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.836",
        "name": "Turbaco"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.838",
        "name": "Turbaná"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.873",
        "name": "Villanueva"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.001",
        "name": "Tunja"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.022",
        "name": "Almeida"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.047",
        "name": "Aquitania"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.051",
        "name": "Arcabuco"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.09",
        "name": "Berbeo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.092",
        "name": "Betéitiva"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.097",
        "name": "Boavita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.104",
        "name": "Boyacá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.106",
        "name": "Briceño"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.109",
        "name": "Buena Vista"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.114",
        "name": "Busbanzá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.131",
        "name": "Caldas"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.135",
        "name": "Campohermoso"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.162",
        "name": "Cerinza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.172",
        "name": "Chinavita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.176",
        "name": "Chiquinquirá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.18",
        "name": "Chiscas"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.183",
        "name": "Chita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.185",
        "name": "Chitaraque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.187",
        "name": "Chivatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.204",
        "name": "Cómbita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.212",
        "name": "Coper"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.215",
        "name": "Corrales"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.218",
        "name": "Covarachía"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.223",
        "name": "Cubará"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.224",
        "name": "Cucaita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.226",
        "name": "Cuítiva"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.232",
        "name": "Chíquiza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.236",
        "name": "Chivor"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.238",
        "name": "Duitama"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.244",
        "name": "El Cocuy"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.248",
        "name": "El Espino"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.272",
        "name": "Firavitoba"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.276",
        "name": "Floresta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.293",
        "name": "Gachantivá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.296",
        "name": "Gameza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.299",
        "name": "Garagoa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.317",
        "name": "Guacamayas"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.322",
        "name": "Guateque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.325",
        "name": "Guayatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.332",
        "name": "Güicán"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.362",
        "name": "Iza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.367",
        "name": "Jenesano"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.368",
        "name": "Jericó"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.377",
        "name": "Labranzagrande"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.38",
        "name": "La Capilla"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.401",
        "name": "La Victoria"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.425",
        "name": "Macanal"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.442",
        "name": "Maripí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.455",
        "name": "Miraflores"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.464",
        "name": "Mongua"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.466",
        "name": "Monguí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.469",
        "name": "Moniquirá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.48",
        "name": "Muzo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.491",
        "name": "Nobsa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.494",
        "name": "Nuevo Colón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.5",
        "name": "Oicatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.507",
        "name": "Otanche"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.511",
        "name": "Pachavita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.514",
        "name": "Páez"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.516",
        "name": "Paipa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.518",
        "name": "Pajarito"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.522",
        "name": "Panqueba"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.531",
        "name": "Pauna"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.533",
        "name": "Paya"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.542",
        "name": "Pesca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.55",
        "name": "Pisba"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.572",
        "name": "Puerto Boyacá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.58",
        "name": "Quípama"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.599",
        "name": "Ramiriquí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.6",
        "name": "Ráquira"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.621",
        "name": "Rondón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.632",
        "name": "Saboyá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.638",
        "name": "Sáchica"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.646",
        "name": "Samacá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.66",
        "name": "San Eduardo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.673",
        "name": "San Mateo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.686",
        "name": "Santana"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.69",
        "name": "Santa María"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.696",
        "name": "Santa Sofía"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.72",
        "name": "Sativanorte"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.723",
        "name": "Sativasur"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.74",
        "name": "Siachoque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.753",
        "name": "Soatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.755",
        "name": "Socotá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.757",
        "name": "Socha"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.759",
        "name": "Sogamoso"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.761",
        "name": "Somondoco"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.762",
        "name": "Sora"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.763",
        "name": "Sotaquirá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.764",
        "name": "Soracá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.774",
        "name": "Susacón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.776",
        "name": "Sutamarchán"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.778",
        "name": "Sutatenza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.79",
        "name": "Tasco"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.798",
        "name": "Tenza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.804",
        "name": "Tibaná"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.808",
        "name": "Tinjacá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.81",
        "name": "Tipacoque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.814",
        "name": "Toca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.82",
        "name": "Tópaga"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.822",
        "name": "Tota"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.835",
        "name": "Turmequé"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.839",
        "name": "Tutazá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.842",
        "name": "Umbita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.861",
        "name": "Ventaquemada"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.879",
        "name": "Viracachá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.897",
        "name": "Zetaquira"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.001",
        "name": "Manizales"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.013",
        "name": "Aguadas"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.042",
        "name": "Anserma"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.05",
        "name": "Aranzazu"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.088",
        "name": "Belalcázar"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.174",
        "name": "Chinchiná"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.272",
        "name": "Filadelfia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.38",
        "name": "La Dorada"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.388",
        "name": "La Merced"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.433",
        "name": "Manzanares"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.442",
        "name": "Marmato"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.446",
        "name": "Marulanda"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.486",
        "name": "Neira"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.495",
        "name": "Norcasia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.513",
        "name": "Pácora"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.524",
        "name": "Palestina"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.541",
        "name": "Pensilvania"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.614",
        "name": "Riosucio"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.616",
        "name": "Risaralda"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.653",
        "name": "Salamina"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.662",
        "name": "Samaná"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.665",
        "name": "San José"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.777",
        "name": "Supía"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.867",
        "name": "Victoria"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.873",
        "name": "Villamaría"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.877",
        "name": "Viterbo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.001",
        "name": "Florencia"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.029",
        "name": "Albania"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.205",
        "name": "Curillo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.247",
        "name": "El Doncello"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.256",
        "name": "El Paujil"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.479",
        "name": "Morelia"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.592",
        "name": "Puerto Rico"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.756",
        "name": "Solano"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.785",
        "name": "Solita"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.86",
        "name": "Valparaíso"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.001",
        "name": "Popayán"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.022",
        "name": "Almaguer"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.05",
        "name": "Argelia"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.075",
        "name": "Balboa"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.1",
        "name": "Bolívar"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.11",
        "name": "Buenos Aires"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.13",
        "name": "Cajibío"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.137",
        "name": "Caldono"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.142",
        "name": "Caloto"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.212",
        "name": "Corinto"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.256",
        "name": "El Tambo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.29",
        "name": "Florencia"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.3",
        "name": "Guachené"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.318",
        "name": "Guapi"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.355",
        "name": "Inzá"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.364",
        "name": "Jambaló"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.392",
        "name": "La Sierra"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.397",
        "name": "La Vega"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.418",
        "name": "López"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.45",
        "name": "Mercaderes"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.455",
        "name": "Miranda"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.473",
        "name": "Morales"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.513",
        "name": "Padilla"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.532",
        "name": "Patía"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.533",
        "name": "Piamonte"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.548",
        "name": "Piendamó"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.573",
        "name": "Puerto Tejada"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.585",
        "name": "Puracé"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.622",
        "name": "Rosas"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.701",
        "name": "Santa Rosa"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.743",
        "name": "Silvia"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.76",
        "name": "Sotara"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.78",
        "name": "Suárez"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.785",
        "name": "Sucre"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.807",
        "name": "Timbío"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.809",
        "name": "Timbiquí"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.821",
        "name": "Toribio"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.824",
        "name": "Totoró"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.845",
        "name": "Villa Rica"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.001",
        "name": "Valledupar"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.011",
        "name": "Aguachica"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.013",
        "name": "Agustín Codazzi"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.032",
        "name": "Astrea"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.045",
        "name": "Becerril"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.06",
        "name": "Bosconia"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.175",
        "name": "Chimichagua"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.178",
        "name": "Chiriguaná"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.228",
        "name": "Curumaní"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.238",
        "name": "El Copey"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.25",
        "name": "El Paso"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.295",
        "name": "Gamarra"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.31",
        "name": "González"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.383",
        "name": "La Gloria"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.443",
        "name": "Manaure"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.517",
        "name": "Pailitas"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.55",
        "name": "Pelaya"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.57",
        "name": "Pueblo Bello"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.621",
        "name": "La Paz"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.71",
        "name": "San Alberto"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.75",
        "name": "San Diego"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.77",
        "name": "San Martín"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.787",
        "name": "Tamalameque"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.001",
        "name": "Montería"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.068",
        "name": "Ayapel"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.079",
        "name": "Buenavista"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.09",
        "name": "Canalete"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.162",
        "name": "Cereté"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.168",
        "name": "Chimá"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.182",
        "name": "Chinú"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.3",
        "name": "Cotorra"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.417",
        "name": "Lorica"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.419",
        "name": "Los Córdobas"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.464",
        "name": "Momil"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.5",
        "name": "Moñitos"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.555",
        "name": "Planeta Rica"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.57",
        "name": "Pueblo Nuevo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.574",
        "name": "Puerto Escondido"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.586",
        "name": "Purísima"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.66",
        "name": "Sahagún"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.67",
        "name": "San Andrés Sotavento"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.672",
        "name": "San Antero"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.686",
        "name": "San Pelayo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.807",
        "name": "Tierralta"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.815",
        "name": "Tuchín"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.855",
        "name": "Valencia"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.035",
        "name": "Anapoima"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.053",
        "name": "Arbeláez"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.086",
        "name": "Beltrán"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.095",
        "name": "Bituima"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.099",
        "name": "Bojacá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.12",
        "name": "Cabrera"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.123",
        "name": "Cachipay"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.126",
        "name": "Cajicá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.148",
        "name": "Caparrapí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.151",
        "name": "Caqueza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.168",
        "name": "Chaguaní"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.178",
        "name": "Chipaque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.181",
        "name": "Choachí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.183",
        "name": "Chocontá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.2",
        "name": "Cogua"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.214",
        "name": "Cota"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.224",
        "name": "Cucunubá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.245",
        "name": "El Colegio"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.26",
        "name": "El Rosal"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.279",
        "name": "Fomeque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.281",
        "name": "Fosca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.286",
        "name": "Funza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.288",
        "name": "Fúquene"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.293",
        "name": "Gachala"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.295",
        "name": "Gachancipá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.297",
        "name": "Gachetá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.307",
        "name": "Girardot"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.312",
        "name": "Granada"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.317",
        "name": "Guachetá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.32",
        "name": "Guaduas"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.322",
        "name": "Guasca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.324",
        "name": "Guataquí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.326",
        "name": "Guatavita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.335",
        "name": "Guayabetal"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.339",
        "name": "Gutiérrez"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.368",
        "name": "Jerusalén"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.372",
        "name": "Junín"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.377",
        "name": "La Calera"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.386",
        "name": "La Mesa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.394",
        "name": "La Palma"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.398",
        "name": "La Peña"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.402",
        "name": "La Vega"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.407",
        "name": "Lenguazaque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.426",
        "name": "Macheta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.43",
        "name": "Madrid"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.436",
        "name": "Manta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.438",
        "name": "Medina"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.473",
        "name": "Mosquera"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.483",
        "name": "Nariño"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.486",
        "name": "Nemocón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.488",
        "name": "Nilo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.489",
        "name": "Nimaima"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.491",
        "name": "Nocaima"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.506",
        "name": "Venecia"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.513",
        "name": "Pacho"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.518",
        "name": "Paime"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.524",
        "name": "Pandi"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.53",
        "name": "Paratebueno"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.535",
        "name": "Pasca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.572",
        "name": "Puerto Salgar"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.58",
        "name": "Pulí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.592",
        "name": "Quebradanegra"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.594",
        "name": "Quetame"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.596",
        "name": "Quipile"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.599",
        "name": "Apulo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.612",
        "name": "Ricaurte"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.649",
        "name": "San Bernardo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.653",
        "name": "San Cayetano"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.658",
        "name": "San Francisco"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.736",
        "name": "Sesquilé"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.74",
        "name": "Sibaté"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.743",
        "name": "Silvania"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.745",
        "name": "Simijaca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.754",
        "name": "Soacha"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.769",
        "name": "Subachoque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.772",
        "name": "Suesca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.777",
        "name": "Supatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.779",
        "name": "Susa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.781",
        "name": "Sutatausa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.785",
        "name": "Tabio"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.793",
        "name": "Tausa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.797",
        "name": "Tena"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.799",
        "name": "Tenjo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.805",
        "name": "Tibacuy"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.807",
        "name": "Tibirita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.815",
        "name": "Tocaima"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.817",
        "name": "Tocancipá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.823",
        "name": "Topaipí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.839",
        "name": "Ubalá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.841",
        "name": "Ubaque"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.845",
        "name": "Une"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.851",
        "name": "Útica"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.867",
        "name": "Vianí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.871",
        "name": "Villagómez"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.873",
        "name": "Villapinzón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.875",
        "name": "Villeta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.878",
        "name": "Viotá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.898",
        "name": "Zipacón"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.001",
        "name": "Quibdó"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.006",
        "name": "Acandí"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.025",
        "name": "Alto Baudo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.05",
        "name": "Atrato"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.073",
        "name": "Bagadó"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.075",
        "name": "Bahía Solano"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.077",
        "name": "Bajo Baudó"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.099",
        "name": "Bojaya"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.16",
        "name": "Cértegui"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.205",
        "name": "Condoto"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.372",
        "name": "Juradó"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.413",
        "name": "Lloró"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.425",
        "name": "Medio Atrato"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.43",
        "name": "Medio Baudó"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.45",
        "name": "Medio San Juan"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.491",
        "name": "Nóvita"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.495",
        "name": "Nuquí"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.58",
        "name": "Río Iro"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.6",
        "name": "Río Quito"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.615",
        "name": "Riosucio"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.745",
        "name": "Sipí"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.8",
        "name": "Unguía"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.001",
        "name": "Neiva"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.006",
        "name": "Acevedo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.013",
        "name": "Agrado"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.016",
        "name": "Aipe"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.02",
        "name": "Algeciras"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.026",
        "name": "Altamira"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.078",
        "name": "Baraya"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.132",
        "name": "Campoalegre"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.206",
        "name": "Colombia"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.244",
        "name": "Elías"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.298",
        "name": "Garzón"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.306",
        "name": "Gigante"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.319",
        "name": "Guadalupe"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.349",
        "name": "Hobo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.357",
        "name": "Iquira"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.359",
        "name": "Isnos"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.378",
        "name": "La Argentina"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.396",
        "name": "La Plata"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.483",
        "name": "Nátaga"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.503",
        "name": "Oporapa"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.518",
        "name": "Paicol"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.524",
        "name": "Palermo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.53",
        "name": "Palestina"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.548",
        "name": "Pital"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.551",
        "name": "Pitalito"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.615",
        "name": "Rivera"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.66",
        "name": "Saladoblanco"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.676",
        "name": "Santa María"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.77",
        "name": "Suaza"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.791",
        "name": "Tarqui"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.797",
        "name": "Tesalia"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.799",
        "name": "Tello"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.801",
        "name": "Teruel"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.807",
        "name": "Timaná"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.872",
        "name": "Villavieja"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.885",
        "name": "Yaguará"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.001",
        "name": "Riohacha"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.035",
        "name": "Albania"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.078",
        "name": "Barrancas"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.09",
        "name": "Dibula"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.098",
        "name": "Distracción"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.11",
        "name": "El Molino"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.279",
        "name": "Fonseca"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.378",
        "name": "Hatonuevo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.43",
        "name": "Maicao"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.56",
        "name": "Manaure"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.847",
        "name": "Uribia"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.855",
        "name": "Urumita"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.874",
        "name": "Villanueva"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.001",
        "name": "Santa Marta"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.03",
        "name": "Algarrobo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.053",
        "name": "Aracataca"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.058",
        "name": "Ariguaní"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.161",
        "name": "Cerro San Antonio"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.17",
        "name": "Chivolo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.205",
        "name": "Concordia"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.245",
        "name": "El Banco"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.258",
        "name": "El Piñon"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.268",
        "name": "El Retén"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.288",
        "name": "Fundación"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.318",
        "name": "Guamal"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.46",
        "name": "Nueva Granada"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.541",
        "name": "Pedraza"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.551",
        "name": "Pivijay"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.555",
        "name": "Plato"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.605",
        "name": "Remolino"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.675",
        "name": "Salamina"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.703",
        "name": "San Zenón"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.707",
        "name": "Santa Ana"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.745",
        "name": "Sitionuevo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.798",
        "name": "Tenerife"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.96",
        "name": "Zapayán"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.98",
        "name": "Zona Bananera"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.001",
        "name": "Villavicencio"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.006",
        "name": "Acacias"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.124",
        "name": "Cabuyaro"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.223",
        "name": "Cubarral"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.226",
        "name": "Cumaral"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.245",
        "name": "El Calvario"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.251",
        "name": "El Castillo"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.27",
        "name": "El Dorado"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.313",
        "name": "Granada"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.318",
        "name": "Guamal"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.325",
        "name": "Mapiripán"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.33",
        "name": "Mesetas"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.35",
        "name": "La Macarena"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.4",
        "name": "Lejanías"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.45",
        "name": "Puerto Concordia"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.568",
        "name": "Puerto Gaitán"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.573",
        "name": "Puerto López"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.577",
        "name": "Puerto Lleras"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.59",
        "name": "Puerto Rico"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.606",
        "name": "Restrepo"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.686",
        "name": "San Juanito"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.689",
        "name": "San Martín"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.711",
        "name": "Vista Hermosa"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.001",
        "name": "Pasto"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.019",
        "name": "Albán"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.022",
        "name": "Aldana"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.036",
        "name": "Ancuyá"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.079",
        "name": "Barbacoas"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.203",
        "name": "Colón"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.207",
        "name": "Consaca"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.21",
        "name": "Contadero"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.215",
        "name": "Córdoba"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.224",
        "name": "Cuaspud"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.227",
        "name": "Cumbal"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.233",
        "name": "Cumbitara"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.25",
        "name": "El Charco"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.254",
        "name": "El Peñol"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.256",
        "name": "El Rosario"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.26",
        "name": "El Tambo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.287",
        "name": "Funes"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.317",
        "name": "Guachucal"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.32",
        "name": "Guaitarilla"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.323",
        "name": "Gualmatán"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.352",
        "name": "Iles"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.354",
        "name": "Imués"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.356",
        "name": "Ipiales"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.378",
        "name": "La Cruz"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.381",
        "name": "La Florida"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.385",
        "name": "La Llanada"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.39",
        "name": "La Tola"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.399",
        "name": "La Unión"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.405",
        "name": "Leiva"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.411",
        "name": "Linares"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.418",
        "name": "Los Andes"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.427",
        "name": "Magüí"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.435",
        "name": "Mallama"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.473",
        "name": "Mosquera"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.48",
        "name": "Nariño"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.49",
        "name": "Olaya Herrera"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.506",
        "name": "Ospina"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.52",
        "name": "Francisco Pizarro"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.54",
        "name": "Policarpa"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.56",
        "name": "Potosí"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.565",
        "name": "Providencia"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.573",
        "name": "Puerres"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.585",
        "name": "Pupiales"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.612",
        "name": "Ricaurte"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.621",
        "name": "Roberto Payán"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.678",
        "name": "Samaniego"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.683",
        "name": "Sandoná"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.685",
        "name": "San Bernardo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.687",
        "name": "San Lorenzo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.693",
        "name": "San Pablo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.696",
        "name": "Santa Bárbara"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.72",
        "name": "Sapuyes"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.786",
        "name": "Taminango"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.788",
        "name": "Tangua"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.838",
        "name": "Túquerres"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.885",
        "name": "Yacuanquer"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.001",
        "name": "Armenia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.111",
        "name": "Buenavista"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.19",
        "name": "Circasia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.212",
        "name": "Córdoba"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.272",
        "name": "Filandia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.401",
        "name": "La Tebaida"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.47",
        "name": "Montenegro"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.548",
        "name": "Pijao"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.594",
        "name": "Quimbaya"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindío",
        "municipality_dane_code": "63.69",
        "name": "Salento"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.001",
        "name": "Pereira"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.045",
        "name": "Apía"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.075",
        "name": "Balboa"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.17",
        "name": "Dosquebradas"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.318",
        "name": "Guática"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.383",
        "name": "La Celia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.4",
        "name": "La Virginia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.44",
        "name": "Marsella"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.456",
        "name": "Mistrató"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.572",
        "name": "Pueblo Rico"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.594",
        "name": "Quinchía"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.687",
        "name": "Santuario"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.001",
        "name": "Bucaramanga"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.013",
        "name": "Aguada"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.02",
        "name": "Albania"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.051",
        "name": "Aratoca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.077",
        "name": "Barbosa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.079",
        "name": "Barichara"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.081",
        "name": "Barrancabermeja"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.092",
        "name": "Betulia"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.101",
        "name": "Bolívar"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.121",
        "name": "Cabrera"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.132",
        "name": "California"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.152",
        "name": "Carcasí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.16",
        "name": "Cepitá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.162",
        "name": "Cerrito"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.167",
        "name": "Charalá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.169",
        "name": "Charta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.179",
        "name": "Chipatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.19",
        "name": "Cimitarra"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.207",
        "name": "Concepción"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.209",
        "name": "Confines"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.211",
        "name": "Contratación"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.217",
        "name": "Coromoro"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.229",
        "name": "Curití"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.245",
        "name": "El Guacamayo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.255",
        "name": "El Playón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.264",
        "name": "Encino"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.266",
        "name": "Enciso"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.271",
        "name": "Florián"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.276",
        "name": "Floridablanca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.296",
        "name": "Galán"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.298",
        "name": "Gambita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.307",
        "name": "Girón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.318",
        "name": "Guaca"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.32",
        "name": "Guadalupe"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.322",
        "name": "Guapotá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.324",
        "name": "Guavatá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.327",
        "name": "Güepsa"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.368",
        "name": "Jesús María"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.37",
        "name": "Jordán"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.377",
        "name": "La Belleza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.385",
        "name": "Landázuri"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.397",
        "name": "La Paz"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.406",
        "name": "Lebríja"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.418",
        "name": "Los Santos"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.425",
        "name": "Macaravita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.432",
        "name": "Málaga"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.444",
        "name": "Matanza"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.464",
        "name": "Mogotes"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.468",
        "name": "Molagavita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.498",
        "name": "Ocamonte"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.5",
        "name": "Oiba"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.502",
        "name": "Onzaga"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.522",
        "name": "Palmar"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.533",
        "name": "Páramo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.547",
        "name": "Piedecuesta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.549",
        "name": "Pinchote"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.572",
        "name": "Puente Nacional"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.615",
        "name": "Rionegro"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.669",
        "name": "San Andrés"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.679",
        "name": "San Gil"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.682",
        "name": "San Joaquín"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.686",
        "name": "San Miguel"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.705",
        "name": "Santa Bárbara"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.745",
        "name": "Simacota"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.755",
        "name": "Socorro"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.77",
        "name": "Suaita"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.773",
        "name": "Sucre"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.78",
        "name": "Suratá"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.82",
        "name": "Tona"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.861",
        "name": "Vélez"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.867",
        "name": "Vetas"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.872",
        "name": "Villanueva"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.895",
        "name": "Zapatoca"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.001",
        "name": "Sincelejo"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.11",
        "name": "Buenavista"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.124",
        "name": "Caimito"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.204",
        "name": "Coloso"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.221",
        "name": "Coveñas"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.23",
        "name": "Chalán"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.233",
        "name": "El Roble"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.235",
        "name": "Galeras"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.265",
        "name": "Guaranda"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.4",
        "name": "La Unión"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.418",
        "name": "Los Palmitos"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.429",
        "name": "Majagual"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.473",
        "name": "Morroa"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.508",
        "name": "Ovejas"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.523",
        "name": "Palmito"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.678",
        "name": "San Benito Abad"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.708",
        "name": "San Marcos"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.713",
        "name": "San Onofre"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.717",
        "name": "San Pedro"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.771",
        "name": "Sucre"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.823",
        "name": "Tolú Viejo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.024",
        "name": "Alpujarra"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.026",
        "name": "Alvarado"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.03",
        "name": "Ambalema"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.055",
        "name": "Armero"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.067",
        "name": "Ataco"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.124",
        "name": "Cajamarca"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.168",
        "name": "Chaparral"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.2",
        "name": "Coello"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.217",
        "name": "Coyaima"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.226",
        "name": "Cunday"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.236",
        "name": "Dolores"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.268",
        "name": "Espinal"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.27",
        "name": "Falan"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.275",
        "name": "Flandes"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.283",
        "name": "Fresno"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.319",
        "name": "Guamo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.347",
        "name": "Herveo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.349",
        "name": "Honda"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.352",
        "name": "Icononzo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.443",
        "name": "Mariquita"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.449",
        "name": "Melgar"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.461",
        "name": "Murillo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.483",
        "name": "Natagaima"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.504",
        "name": "Ortega"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.52",
        "name": "Palocabildo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.547",
        "name": "Piedras"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.555",
        "name": "Planadas"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.563",
        "name": "Prado"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.585",
        "name": "Purificación"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.616",
        "name": "Rio Blanco"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.622",
        "name": "Roncesvalles"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.624",
        "name": "Rovira"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.671",
        "name": "Saldaña"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.686",
        "name": "Santa Isabel"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.861",
        "name": "Venadillo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.87",
        "name": "Villahermosa"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.873",
        "name": "Villarrica"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.065",
        "name": "Arauquita"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.22",
        "name": "Cravo Norte"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.3",
        "name": "Fortul"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.591",
        "name": "Puerto Rondón"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.736",
        "name": "Saravena"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.794",
        "name": "Tame"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.001",
        "name": "Arauca"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.001",
        "name": "Yopal"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.01",
        "name": "Aguazul"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.015",
        "name": "Chámeza"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.125",
        "name": "Hato Corozal"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.136",
        "name": "La Salina"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.162",
        "name": "Monterrey"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.263",
        "name": "Pore"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.279",
        "name": "Recetor"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.3",
        "name": "Sabanalarga"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.315",
        "name": "Sácama"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.41",
        "name": "Tauramena"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.43",
        "name": "Trinidad"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.44",
        "name": "Villanueva"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.001",
        "name": "Mocoa"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.219",
        "name": "Colón"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.32",
        "name": "Orito"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.569",
        "name": "Puerto Caicedo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.571",
        "name": "Puerto Guzmán"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.573",
        "name": "Leguízamo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.749",
        "name": "Sibundoy"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.755",
        "name": "San Francisco"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.757",
        "name": "San Miguel"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.76",
        "name": "Santiago"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.001",
        "name": "Leticia"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.263",
        "name": "El Encanto"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.405",
        "name": "La Chorrera"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.407",
        "name": "La Pedrera"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.43",
        "name": "La Victoria"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.536",
        "name": "Puerto Arica"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.54",
        "name": "Puerto Nariño"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.669",
        "name": "Puerto Santander"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.798",
        "name": "Tarapacá"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.001",
        "name": "Inírida"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.343",
        "name": "Barranco Minas"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.663",
        "name": "Mapiripana"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.883",
        "name": "San Felipe"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.884",
        "name": "Puerto Colombia"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.885",
        "name": "La Guadalupe"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.886",
        "name": "Cacahual"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.887",
        "name": "Pana Pana"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.001",
        "name": "Mitú"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.161",
        "name": "Carurú"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.666",
        "name": "Taraira"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.777",
        "name": "Papunahua"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.889",
        "name": "Yavaraté"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.511",
        "name": "Pacoa"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "94",
        "departament": "Guainía",
        "municipality_dane_code": "94.888",
        "name": "Morichal"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.001",
        "name": "Puerto Carreño"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.524",
        "name": "La Primavera"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.624",
        "name": "Santa Rosalía"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.773",
        "name": "Cumaribo"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.61",
        "name": "San José del Fragua"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.11",
        "name": "Barranca de Upía"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.524",
        "name": "Palmas del Socorro"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.662",
        "name": "San Juan de Río Seco"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.372",
        "name": "Juan de Acosta"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.287",
        "name": "Fuente de Oro"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.325",
        "name": "San Luis de Gaceno"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.25",
        "name": "El Litoral del San Juan"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.843",
        "name": "Villa de San Diego de Ubate"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.074",
        "name": "Barranco de Loba"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.816",
        "name": "Togüí"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.688",
        "name": "Santa Rosa del Sur"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.135",
        "name": "El Cantón del San Pablo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.407",
        "name": "Villa de Leyva"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.692",
        "name": "San Sebastián de Buenavista"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.537",
        "name": "Paz de Río"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.3",
        "name": "Hatillo de Loba"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.66",
        "name": "Sabanas de San Angel"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.015",
        "name": "Calamar"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.614",
        "name": "Río de Oro"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.665",
        "name": "San Pedro de Uraba"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.001",
        "name": "San José del Guaviare"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.693",
        "name": "Santa Rosa de Viterbo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.698",
        "name": "Santander de Quilichao"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.2",
        "name": "Miraflores"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.042",
        "name": "Santafé de Antioquia"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.68",
        "name": "San Carlos de Guaroa"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.52",
        "name": "Palmar de Varela"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.686",
        "name": "Santa Rosa de Osos"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.647",
        "name": "San Andrés de Cuerquía"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.854",
        "name": "Valle de San Juan"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.689",
        "name": "San Vicente de Chucurí"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.684",
        "name": "San José de Miranda"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "88",
        "departament": "Archipiélago de San Andrés, Providencia y Santa Catalina",
        "municipality_dane_code": "88.564",
        "name": "Providencia"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.682",
        "name": "Santa Rosa de Cabal"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.328",
        "name": "Guayabal de Siquima"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.094",
        "name": "Belén de Los Andaquies"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.25",
        "name": "Paz de Ariporo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.72",
        "name": "Santa Helena del Opón"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.681",
        "name": "San Pablo de Borbur"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.42",
        "name": "La Jagua del Pilar"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.4",
        "name": "La Jagua de Ibirico"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.742",
        "name": "San Luis de Sincé"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.667",
        "name": "San Luis de Gaceno"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.244",
        "name": "El Carmen de Bolívar"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.245",
        "name": "El Carmen de Atrato"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.702",
        "name": "San Juan de Betulia"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.545",
        "name": "Pijiño del Carmen"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.873",
        "name": "Vigía del Fuerte"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.667",
        "name": "San Martín de Loba"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.03",
        "name": "Altos del Rosario"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.148",
        "name": "Carmen de Apicala"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.645",
        "name": "San Antonio del Tequendama"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.655",
        "name": "Sabana de Torres"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.025",
        "name": "El Retorno"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.682",
        "name": "San José de Uré"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.694",
        "name": "San Pedro de Cartago"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "8",
        "departament": "Atlántico",
        "municipality_dane_code": "8.137",
        "name": "Campo de La Cruz"
    },
    {
        "region": "Región Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.683",
        "name": "San Juan de Arama"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.658",
        "name": "San José de La Montaña"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caquetá",
        "municipality_dane_code": "18.15",
        "name": "Cartagena del Chairá"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.66",
        "name": "San José del Palmar"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.001",
        "name": "Agua de Dios"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.655",
        "name": "San Jacinto del Cauca"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.668",
        "name": "San Agustín"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.258",
        "name": "El Tablón de Gómez"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "88",
        "departament": "Archipiélago de San Andrés, Providencia y Santa Catalina",
        "municipality_dane_code": "88.001",
        "name": "San Andrés"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.664",
        "name": "San José de Pare"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.865",
        "name": "Valle de Guamez"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.67",
        "name": "San Pablo de Borbur"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.82",
        "name": "Santiago de Tolú"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "11",
        "departament": "Bogotá D.C.",
        "municipality_dane_code": "11.001",
        "name": "Bogotá D.C."
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.154",
        "name": "Carmen de Carupa"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.189",
        "name": "Ciénaga de Oro"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.659",
        "name": "San Juan de Urabá"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.65",
        "name": "San Juan del Cesar"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.235",
        "name": "El Carmen de Chucurí"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.148",
        "name": "El Carmen de Viboral"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.088",
        "name": "Belén de Umbría"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "27",
        "departament": "Chocó",
        "municipality_dane_code": "27.086",
        "name": "Belén de Bajira"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.855",
        "name": "Valle de San José"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.678",
        "name": "San Luis"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.676",
        "name": "San Miguel de Sema"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.675",
        "name": "San Antonio"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.673",
        "name": "San Benito"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.862",
        "name": "Vergara"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "23",
        "departament": "Córdoba",
        "municipality_dane_code": "23.678",
        "name": "San Carlos"
    },
    {
        "region": "Región Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.53",
        "name": "Puerto Alegría"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.344",
        "name": "Hato"
    },
    {
        "region": "Región Caribe",
        "departament_dane_code": "13",
        "departament": "Bolívar",
        "municipality_dane_code": "13.654",
        "name": "San Jacinto"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.693",
        "name": "San Sebastián"
    },
    {
        "region": "Región Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.649",
        "name": "San Carlos"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyacá",
        "municipality_dane_code": "15.837",
        "name": "Tuta"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.743",
        "name": "Silos"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.125",
        "name": "Cácota"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.25",
        "name": "El Dovio"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.82",
        "name": "Toledo"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.622",
        "name": "Roldanillo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.48",
        "name": "Mutiscua"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.054",
        "name": "Argelia"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.261",
        "name": "El Zulia"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.66",
        "name": "Salazar"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.736",
        "name": "Sevilla"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.895",
        "name": "Zarzal"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.223",
        "name": "Cucutilla"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.248",
        "name": "El Cerrito"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.147",
        "name": "Cartago"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.122",
        "name": "Caicedonia"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.553",
        "name": "Puerto Santander"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.313",
        "name": "Gramalote"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.246",
        "name": "El Cairo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.25",
        "name": "El Tarra"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.4",
        "name": "La Unión"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.606",
        "name": "Restrepo"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.8",
        "name": "Teorama"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.233",
        "name": "Dagua"
    },
    {
        "region": "Región Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.051",
        "name": "Arboledas"
    },
    {
        "region": "Región Pacífico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.318",
        "name": "Guacarí"
    }
]

for user_to_create in ["admin" ]:
    try:
        user = User.objects.create_superuser(
            username=user_to_create, password=user_to_create
        )
    except Exception as e:
        print("Error creating user:", e)

   
for city_data in cities_to_create:
    try:
        city = Cities.objects.create(**city_data)
        print("Created City:", city)
    except Exception as e:
        print("Error creating city:", e)

   