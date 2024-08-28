from medicalrecords.models import Cities
from users.models import User


cities_to_create = [       
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.001",
        "name": "Medellin"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.002",
        "name": "Abejorral"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.004",
        "name": "Abriaqui"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.021",
        "name": "Alejandria"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.03",
        "name": "Amaga"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.031",
        "name": "Amalfi"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.034",
        "name": "Andes"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.036",
        "name": "Angelopolis"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.038",
        "name": "Angostura"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.04",
        "name": "Anori"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.832",
        "name": "Tunungua"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.044",
        "name": "Anza"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.045",
        "name": "Apartado"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.051",
        "name": "Arboletes"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.055",
        "name": "Argelia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.059",
        "name": "Armenia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.079",
        "name": "Barbosa"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.088",
        "name": "Bello"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.091",
        "name": "Betania"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.093",
        "name": "Betulia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.101",
        "name": "Ciudad Bolivar"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.107",
        "name": "Briceño"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.113",
        "name": "Buritica"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.12",
        "name": "Caceres"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.125",
        "name": "Caicedo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.129",
        "name": "Caldas"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.134",
        "name": "Campamento"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.138",
        "name": "Cañasgordas"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.142",
        "name": "Caracoli"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.145",
        "name": "Caramanta"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.147",
        "name": "Carepa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.476",
        "name": "Motavita"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.15",
        "name": "Carolina"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.154",
        "name": "Caucasia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.172",
        "name": "Chigorodo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.19",
        "name": "Cisneros"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.197",
        "name": "Cocorna"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.206",
        "name": "Concepcion"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.209",
        "name": "Concordia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.212",
        "name": "Copacabana"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.234",
        "name": "Dabeiba"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.237",
        "name": "Don Matias"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.24",
        "name": "Ebéjico"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.25",
        "name": "El Bagre"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.264",
        "name": "Entrerrios"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.266",
        "name": "Envigado"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.282",
        "name": "Fredonia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.675",
        "name": "San Bernardo del Viento"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.306",
        "name": "Giraldo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.308",
        "name": "Girardota"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.31",
        "name": "Gomez Plata"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.361",
        "name": "Istmina"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.315",
        "name": "Guadalupe"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.318",
        "name": "Guarne"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.321",
        "name": "Guatapé"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.347",
        "name": "Heliconia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.353",
        "name": "Hispania"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.36",
        "name": "Itagui"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.361",
        "name": "Ituango"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.086",
        "name": "Belmira"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.368",
        "name": "Jerico"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.376",
        "name": "La Ceja"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.38",
        "name": "La Estrella"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.39",
        "name": "La Pintada"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.4",
        "name": "La Union"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.411",
        "name": "Liborina"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.425",
        "name": "Maceo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.44",
        "name": "Marinilla"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.467",
        "name": "Montebello"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.475",
        "name": "Murindo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.48",
        "name": "Mutata"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.483",
        "name": "Nariño"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.49",
        "name": "Necocli"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.495",
        "name": "Nechi"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.501",
        "name": "Olaya"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.541",
        "name": "Peñol"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.543",
        "name": "Peque"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.576",
        "name": "Pueblorrico"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.579",
        "name": "Puerto Berrio"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.585",
        "name": "Puerto Nare"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.591",
        "name": "Puerto Triunfo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.604",
        "name": "Remedios"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.607",
        "name": "Retiro"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.615",
        "name": "Rionegro"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.628",
        "name": "Sabanalarga"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.631",
        "name": "Sabaneta"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.642",
        "name": "Salgar"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.189",
        "name": "Ciénega"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.699",
        "name": "Santacruz"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.652",
        "name": "San Francisco"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.656",
        "name": "San Jeronimo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.575",
        "name": "Puerto Wilches"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.573",
        "name": "Puerto Parra"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.66",
        "name": "San Luis"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.664",
        "name": "San Pedro"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.667",
        "name": "San Rafael"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.67",
        "name": "San Roque"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.674",
        "name": "San Vicente"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.679",
        "name": "Santa Barbara"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.69",
        "name": "Santo Domingo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.697",
        "name": "El Santuario"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.736",
        "name": "Segovia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.761",
        "name": "Sopetran"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.37",
        "name": "Uribe"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.789",
        "name": "Tamesis"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.79",
        "name": "Taraza"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.792",
        "name": "Tarso"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.809",
        "name": "Titiribi"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.819",
        "name": "Toledo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.837",
        "name": "Turbo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.842",
        "name": "Uramita"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.847",
        "name": "Urrao"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.854",
        "name": "Valdivia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.856",
        "name": "Valparaiso"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.858",
        "name": "Vegachi"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.861",
        "name": "Venecia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.885",
        "name": "Yali"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.887",
        "name": "Yarumal"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.89",
        "name": "Yolombo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.893",
        "name": "Yondo"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.895",
        "name": "Zaragoza"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.001",
        "name": "Barranquilla"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.078",
        "name": "Baranoa"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.141",
        "name": "Candelaria"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.296",
        "name": "Galapa"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.421",
        "name": "Luruaco"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.433",
        "name": "Malambo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.436",
        "name": "Manati"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.549",
        "name": "Piojo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.558",
        "name": "Polonuevo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.634",
        "name": "Sabanagrande"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.638",
        "name": "Sabanalarga"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.675",
        "name": "Santa Lucia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.685",
        "name": "Santo Tomas"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.758",
        "name": "Soledad"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.77",
        "name": "Suan"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.832",
        "name": "Tubara"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.849",
        "name": "Usiacuri"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.006",
        "name": "Achi"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.042",
        "name": "Arenal"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.052",
        "name": "Arjona"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.062",
        "name": "Arroyohondo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.14",
        "name": "Calamar"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.16",
        "name": "Cantagallo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.188",
        "name": "Cicuco"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.212",
        "name": "Cordoba"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.222",
        "name": "Clemencia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.248",
        "name": "El Guamo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.43",
        "name": "Magangué"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.433",
        "name": "Mahates"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.44",
        "name": "Margarita"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.458",
        "name": "Montecristo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.468",
        "name": "Mompos"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.473",
        "name": "Morales"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.49",
        "name": "Norosi"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.549",
        "name": "Pinillos"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.58",
        "name": "Regidor"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.6",
        "name": "Rio Viejo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.647",
        "name": "San Estanislao"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.65",
        "name": "San Fernando"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.657",
        "name": "San Juan Nepomuceno"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.673",
        "name": "Santa Catalina"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.683",
        "name": "Santa Rosa"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.744",
        "name": "Simiti"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.76",
        "name": "Soplaviento"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.78",
        "name": "Talaigua Nuevo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.81",
        "name": "Tiquisio"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.836",
        "name": "Turbaco"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.838",
        "name": "Turbana"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.873",
        "name": "Villanueva"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.001",
        "name": "Tunja"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.022",
        "name": "Almeida"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.047",
        "name": "Aquitania"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.051",
        "name": "Arcabuco"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.09",
        "name": "Berbeo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.092",
        "name": "Betéitiva"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.097",
        "name": "Boavita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.104",
        "name": "Boyaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.106",
        "name": "Briceño"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.109",
        "name": "Buena Vista"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.114",
        "name": "Busbanza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.131",
        "name": "Caldas"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.135",
        "name": "Campohermoso"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.162",
        "name": "Cerinza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.172",
        "name": "Chinavita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.176",
        "name": "Chiquinquira"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.18",
        "name": "Chiscas"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.183",
        "name": "Chita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.185",
        "name": "Chitaraque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.187",
        "name": "Chivata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.204",
        "name": "Combita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.212",
        "name": "Coper"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.215",
        "name": "Corrales"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.218",
        "name": "Covarachia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.223",
        "name": "Cubara"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.224",
        "name": "Cucaita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.226",
        "name": "Cuitiva"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.232",
        "name": "Chiquiza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.236",
        "name": "Chivor"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.238",
        "name": "Duitama"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.244",
        "name": "El Cocuy"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.248",
        "name": "El Espino"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.272",
        "name": "Firavitoba"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.276",
        "name": "Floresta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.293",
        "name": "Gachantiva"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.296",
        "name": "Gameza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.299",
        "name": "Garagoa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.317",
        "name": "Guacamayas"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.322",
        "name": "Guateque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.325",
        "name": "Guayata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.332",
        "name": "Güican"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.362",
        "name": "Iza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.367",
        "name": "Jenesano"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.368",
        "name": "Jerico"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.377",
        "name": "Labranzagrande"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.38",
        "name": "La Capilla"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.401",
        "name": "La Victoria"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.425",
        "name": "Macanal"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.442",
        "name": "Maripi"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.455",
        "name": "Miraflores"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.464",
        "name": "Mongua"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.466",
        "name": "Mongui"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.469",
        "name": "Moniquira"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.48",
        "name": "Muzo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.491",
        "name": "Nobsa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.494",
        "name": "Nuevo Colon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.5",
        "name": "Oicata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.507",
        "name": "Otanche"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.511",
        "name": "Pachavita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.514",
        "name": "Paez"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.516",
        "name": "Paipa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.518",
        "name": "Pajarito"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.522",
        "name": "Panqueba"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.531",
        "name": "Pauna"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.533",
        "name": "Paya"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.542",
        "name": "Pesca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.55",
        "name": "Pisba"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.572",
        "name": "Puerto Boyaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.58",
        "name": "Quipama"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.599",
        "name": "Ramiriqui"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.6",
        "name": "Raquira"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.621",
        "name": "Rondon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.632",
        "name": "Saboya"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.638",
        "name": "Sachica"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.646",
        "name": "Samaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.66",
        "name": "San Eduardo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.673",
        "name": "San Mateo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.686",
        "name": "Santana"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.69",
        "name": "Santa Maria"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.696",
        "name": "Santa Sofia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.72",
        "name": "Sativanorte"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.723",
        "name": "Sativasur"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.74",
        "name": "Siachoque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.753",
        "name": "Soata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.755",
        "name": "Socota"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.757",
        "name": "Socha"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.759",
        "name": "Sogamoso"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.761",
        "name": "Somondoco"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.762",
        "name": "Sora"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.763",
        "name": "Sotaquira"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.764",
        "name": "Soraca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.774",
        "name": "Susacon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.776",
        "name": "Sutamarchan"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.778",
        "name": "Sutatenza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.79",
        "name": "Tasco"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.798",
        "name": "Tenza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.804",
        "name": "Tibana"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.808",
        "name": "Tinjaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.81",
        "name": "Tipacoque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.814",
        "name": "Toca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.82",
        "name": "Topaga"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.822",
        "name": "Tota"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.835",
        "name": "Turmequé"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.839",
        "name": "Tutaza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.842",
        "name": "Umbita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.861",
        "name": "Ventaquemada"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.879",
        "name": "Viracacha"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.897",
        "name": "Zetaquira"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.001",
        "name": "Manizales"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.013",
        "name": "Aguadas"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.042",
        "name": "Anserma"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.05",
        "name": "Aranzazu"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.088",
        "name": "Belalcazar"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.174",
        "name": "Chinchina"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.272",
        "name": "Filadelfia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.38",
        "name": "La Dorada"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.388",
        "name": "La Merced"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.433",
        "name": "Manzanares"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.442",
        "name": "Marmato"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.446",
        "name": "Marulanda"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.486",
        "name": "Neira"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.495",
        "name": "Norcasia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.513",
        "name": "Pacora"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.524",
        "name": "Palestina"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.541",
        "name": "Pensilvania"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.614",
        "name": "Riosucio"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.616",
        "name": "Risaralda"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.653",
        "name": "Salamina"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.662",
        "name": "Samana"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.665",
        "name": "San José"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.777",
        "name": "Supia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.867",
        "name": "Victoria"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.873",
        "name": "Villamaria"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "17",
        "departament": "Caldas",
        "municipality_dane_code": "17.877",
        "name": "Viterbo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.001",
        "name": "Florencia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.029",
        "name": "Albania"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.205",
        "name": "Curillo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.247",
        "name": "El Doncello"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.256",
        "name": "El Paujil"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.479",
        "name": "Morelia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.592",
        "name": "Puerto Rico"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.756",
        "name": "Solano"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.785",
        "name": "Solita"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.86",
        "name": "Valparaiso"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.001",
        "name": "Popayan"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.022",
        "name": "Almaguer"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.05",
        "name": "Argelia"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.075",
        "name": "Balboa"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.1",
        "name": "Bolivar"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.11",
        "name": "Buenos Aires"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.13",
        "name": "Cajibio"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.137",
        "name": "Caldono"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.142",
        "name": "Caloto"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.212",
        "name": "Corinto"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.256",
        "name": "El Tambo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.29",
        "name": "Florencia"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.3",
        "name": "Guachené"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.318",
        "name": "Guapi"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.355",
        "name": "Inza"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.364",
        "name": "Jambalo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.392",
        "name": "La Sierra"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.397",
        "name": "La Vega"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.418",
        "name": "Lopez"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.45",
        "name": "Mercaderes"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.455",
        "name": "Miranda"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.473",
        "name": "Morales"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.513",
        "name": "Padilla"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.532",
        "name": "Patia"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.533",
        "name": "Piamonte"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.548",
        "name": "Piendamo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.573",
        "name": "Puerto Tejada"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.585",
        "name": "Puracé"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.622",
        "name": "Rosas"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.701",
        "name": "Santa Rosa"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.743",
        "name": "Silvia"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.76",
        "name": "Sotara"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.78",
        "name": "Suarez"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.785",
        "name": "Sucre"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.807",
        "name": "Timbio"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.809",
        "name": "Timbiqui"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.821",
        "name": "Toribio"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.824",
        "name": "Totoro"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.845",
        "name": "Villa Rica"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.001",
        "name": "Valledupar"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.011",
        "name": "Aguachica"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.013",
        "name": "Agustin Codazzi"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.032",
        "name": "Astrea"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.045",
        "name": "Becerril"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.06",
        "name": "Bosconia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.175",
        "name": "Chimichagua"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.178",
        "name": "Chiriguana"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.228",
        "name": "Curumani"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.238",
        "name": "El Copey"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.25",
        "name": "El Paso"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.295",
        "name": "Gamarra"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.31",
        "name": "Gonzalez"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.383",
        "name": "La Gloria"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.443",
        "name": "Manaure"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.517",
        "name": "Pailitas"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.55",
        "name": "Pelaya"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.57",
        "name": "Pueblo Bello"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.621",
        "name": "La Paz"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.71",
        "name": "San Alberto"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.75",
        "name": "San Diego"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.77",
        "name": "San Martin"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.787",
        "name": "Tamalameque"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.001",
        "name": "Monteria"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.068",
        "name": "Ayapel"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.079",
        "name": "Buenavista"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.09",
        "name": "Canalete"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.162",
        "name": "Cereté"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.168",
        "name": "Chima"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.182",
        "name": "Chinú"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.3",
        "name": "Cotorra"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.417",
        "name": "Lorica"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.419",
        "name": "Los Cordobas"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.464",
        "name": "Momil"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.5",
        "name": "Moñitos"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.555",
        "name": "Planeta Rica"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.57",
        "name": "Pueblo Nuevo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.574",
        "name": "Puerto Escondido"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.586",
        "name": "Purisima"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.66",
        "name": "Sahagún"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.67",
        "name": "San Andrés Sotavento"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.672",
        "name": "San Antero"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.686",
        "name": "San Pelayo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.807",
        "name": "Tierralta"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.815",
        "name": "Tuchin"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.855",
        "name": "Valencia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.035",
        "name": "Anapoima"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.053",
        "name": "Arbelaez"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.086",
        "name": "Beltran"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.095",
        "name": "Bituima"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.099",
        "name": "Bojaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.12",
        "name": "Cabrera"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.123",
        "name": "Cachipay"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.126",
        "name": "Cajica"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.148",
        "name": "Caparrapi"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.151",
        "name": "Caqueza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.168",
        "name": "Chaguani"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.178",
        "name": "Chipaque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.181",
        "name": "Choachi"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.183",
        "name": "Choconta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.2",
        "name": "Cogua"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.214",
        "name": "Cota"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.224",
        "name": "Cucunuba"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.245",
        "name": "El Colegio"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.26",
        "name": "El Rosal"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.279",
        "name": "Fomeque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.281",
        "name": "Fosca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.286",
        "name": "Funza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.288",
        "name": "Fúquene"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.293",
        "name": "Gachala"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.295",
        "name": "Gachancipa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.297",
        "name": "Gacheta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.307",
        "name": "Girardot"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.312",
        "name": "Granada"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.317",
        "name": "Guacheta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.32",
        "name": "Guaduas"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.322",
        "name": "Guasca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.324",
        "name": "Guataqui"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.326",
        "name": "Guatavita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.335",
        "name": "Guayabetal"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.339",
        "name": "Gutiérrez"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.368",
        "name": "Jerusalén"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.372",
        "name": "Junin"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.377",
        "name": "La Calera"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.386",
        "name": "La Mesa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.394",
        "name": "La Palma"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.398",
        "name": "La Peña"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.402",
        "name": "La Vega"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.407",
        "name": "Lenguazaque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.426",
        "name": "Macheta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.43",
        "name": "Madrid"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.436",
        "name": "Manta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.438",
        "name": "Medina"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.473",
        "name": "Mosquera"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.483",
        "name": "Nariño"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.486",
        "name": "Nemocon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.488",
        "name": "Nilo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.489",
        "name": "Nimaima"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.491",
        "name": "Nocaima"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.506",
        "name": "Venecia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.513",
        "name": "Pacho"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.518",
        "name": "Paime"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.524",
        "name": "Pandi"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.53",
        "name": "Paratebueno"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.535",
        "name": "Pasca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.572",
        "name": "Puerto Salgar"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.58",
        "name": "Puli"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.592",
        "name": "Quebradanegra"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.594",
        "name": "Quetame"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.596",
        "name": "Quipile"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.599",
        "name": "Apulo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.612",
        "name": "Ricaurte"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.649",
        "name": "San Bernardo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.653",
        "name": "San Cayetano"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.658",
        "name": "San Francisco"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.736",
        "name": "Sesquilé"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.74",
        "name": "Sibaté"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.743",
        "name": "Silvania"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.745",
        "name": "Simijaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.754",
        "name": "Soacha"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.769",
        "name": "Subachoque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.772",
        "name": "Suesca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.777",
        "name": "Supata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.779",
        "name": "Susa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.781",
        "name": "Sutatausa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.785",
        "name": "Tabio"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.793",
        "name": "Tausa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.797",
        "name": "Tena"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.799",
        "name": "Tenjo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.805",
        "name": "Tibacuy"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.807",
        "name": "Tibirita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.815",
        "name": "Tocaima"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.817",
        "name": "Tocancipa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.823",
        "name": "Topaipi"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.839",
        "name": "Ubala"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.841",
        "name": "Ubaque"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.845",
        "name": "Une"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.851",
        "name": "Útica"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.867",
        "name": "Viani"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.871",
        "name": "Villagomez"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.873",
        "name": "Villapinzon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.875",
        "name": "Villeta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.878",
        "name": "Viota"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.898",
        "name": "Zipacon"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.001",
        "name": "Quibdo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.006",
        "name": "Acandi"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.025",
        "name": "Alto Baudo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.05",
        "name": "Atrato"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.073",
        "name": "Bagado"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.075",
        "name": "Bahia Solano"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.077",
        "name": "Bajo Baudo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.099",
        "name": "Bojaya"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.16",
        "name": "Cértegui"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.205",
        "name": "Condoto"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.372",
        "name": "Jurado"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.413",
        "name": "Lloro"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.425",
        "name": "Medio Atrato"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.43",
        "name": "Medio Baudo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.45",
        "name": "Medio San Juan"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.491",
        "name": "Novita"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.495",
        "name": "Nuqui"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.58",
        "name": "Rio Iro"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.6",
        "name": "Rio Quito"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.615",
        "name": "Riosucio"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.745",
        "name": "Sipi"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.8",
        "name": "Unguia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.001",
        "name": "Neiva"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.006",
        "name": "Acevedo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.013",
        "name": "Agrado"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.016",
        "name": "Aipe"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.02",
        "name": "Algeciras"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.026",
        "name": "Altamira"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.078",
        "name": "Baraya"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.132",
        "name": "Campoalegre"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.206",
        "name": "Colombia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.244",
        "name": "Elias"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.298",
        "name": "Garzon"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.306",
        "name": "Gigante"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.319",
        "name": "Guadalupe"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.349",
        "name": "Hobo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.357",
        "name": "Iquira"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.359",
        "name": "Isnos"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.378",
        "name": "La Argentina"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.396",
        "name": "La Plata"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.483",
        "name": "Nataga"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.503",
        "name": "Oporapa"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.518",
        "name": "Paicol"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.524",
        "name": "Palermo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.53",
        "name": "Palestina"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.548",
        "name": "Pital"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.551",
        "name": "Pitalito"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.615",
        "name": "Rivera"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.66",
        "name": "Saladoblanco"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.676",
        "name": "Santa Maria"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.77",
        "name": "Suaza"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.791",
        "name": "Tarqui"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.797",
        "name": "Tesalia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.799",
        "name": "Tello"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.801",
        "name": "Teruel"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.807",
        "name": "Timana"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.872",
        "name": "Villavieja"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.885",
        "name": "Yaguara"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.001",
        "name": "Riohacha"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.035",
        "name": "Albania"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.078",
        "name": "Barrancas"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.09",
        "name": "Dibula"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.098",
        "name": "Distraccion"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.11",
        "name": "El Molino"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.279",
        "name": "Fonseca"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.378",
        "name": "Hatonuevo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.43",
        "name": "Maicao"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.56",
        "name": "Manaure"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.847",
        "name": "Uribia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.855",
        "name": "Urumita"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.874",
        "name": "Villanueva"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.001",
        "name": "Santa Marta"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.03",
        "name": "Algarrobo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.053",
        "name": "Aracataca"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.058",
        "name": "Ariguani"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.161",
        "name": "Cerro San Antonio"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.17",
        "name": "Chivolo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.205",
        "name": "Concordia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.245",
        "name": "El Banco"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.258",
        "name": "El Piñon"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.268",
        "name": "El Retén"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.288",
        "name": "Fundacion"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.318",
        "name": "Guamal"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.46",
        "name": "Nueva Granada"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.541",
        "name": "Pedraza"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.551",
        "name": "Pivijay"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.555",
        "name": "Plato"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.605",
        "name": "Remolino"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.675",
        "name": "Salamina"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.703",
        "name": "San Zenon"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.707",
        "name": "Santa Ana"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.745",
        "name": "Sitionuevo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.798",
        "name": "Tenerife"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.96",
        "name": "Zapayan"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.98",
        "name": "Zona Bananera"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.001",
        "name": "Villavicencio"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.006",
        "name": "Acacias"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.124",
        "name": "Cabuyaro"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.223",
        "name": "Cubarral"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.226",
        "name": "Cumaral"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.245",
        "name": "El Calvario"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.251",
        "name": "El Castillo"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.27",
        "name": "El Dorado"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.313",
        "name": "Granada"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.318",
        "name": "Guamal"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.325",
        "name": "Mapiripan"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.33",
        "name": "Mesetas"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.35",
        "name": "La Macarena"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.4",
        "name": "Lejanias"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.45",
        "name": "Puerto Concordia"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.568",
        "name": "Puerto Gaitan"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.573",
        "name": "Puerto Lopez"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.577",
        "name": "Puerto Lleras"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.59",
        "name": "Puerto Rico"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.606",
        "name": "Restrepo"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.686",
        "name": "San Juanito"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.689",
        "name": "San Martin"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.711",
        "name": "Vista Hermosa"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.001",
        "name": "Pasto"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.019",
        "name": "Alban"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.022",
        "name": "Aldana"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.036",
        "name": "Ancuya"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.079",
        "name": "Barbacoas"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.203",
        "name": "Colon"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.207",
        "name": "Consaca"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.21",
        "name": "Contadero"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.215",
        "name": "Cordoba"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.224",
        "name": "Cuaspud"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.227",
        "name": "Cumbal"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.233",
        "name": "Cumbitara"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.25",
        "name": "El Charco"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.254",
        "name": "El Peñol"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.256",
        "name": "El Rosario"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.26",
        "name": "El Tambo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.287",
        "name": "Funes"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.317",
        "name": "Guachucal"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.32",
        "name": "Guaitarilla"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.323",
        "name": "Gualmatan"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.352",
        "name": "Iles"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.354",
        "name": "Imués"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.356",
        "name": "Ipiales"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.378",
        "name": "La Cruz"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.381",
        "name": "La Florida"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.385",
        "name": "La Llanada"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.39",
        "name": "La Tola"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.399",
        "name": "La Union"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.405",
        "name": "Leiva"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.411",
        "name": "Linares"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.418",
        "name": "Los Andes"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.427",
        "name": "Magüi"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.435",
        "name": "Mallama"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.473",
        "name": "Mosquera"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.48",
        "name": "Nariño"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.49",
        "name": "Olaya Herrera"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.506",
        "name": "Ospina"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.52",
        "name": "Francisco Pizarro"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.54",
        "name": "Policarpa"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.56",
        "name": "Potosi"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.565",
        "name": "Providencia"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.573",
        "name": "Puerres"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.585",
        "name": "Pupiales"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.612",
        "name": "Ricaurte"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.621",
        "name": "Roberto Payan"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.678",
        "name": "Samaniego"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.683",
        "name": "Sandona"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.685",
        "name": "San Bernardo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.687",
        "name": "San Lorenzo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.693",
        "name": "San Pablo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.696",
        "name": "Santa Barbara"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.72",
        "name": "Sapuyes"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.786",
        "name": "Taminango"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.788",
        "name": "Tangua"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.838",
        "name": "Túquerres"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.885",
        "name": "Yacuanquer"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.001",
        "name": "Armenia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.111",
        "name": "Buenavista"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.19",
        "name": "Circasia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.212",
        "name": "Cordoba"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.272",
        "name": "Filandia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.401",
        "name": "La Tebaida"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.47",
        "name": "Montenegro"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.548",
        "name": "Pijao"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.594",
        "name": "Quimbaya"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "63",
        "departament": "Quindio",
        "municipality_dane_code": "63.69",
        "name": "Salento"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.001",
        "name": "Pereira"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.045",
        "name": "Apia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.075",
        "name": "Balboa"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.17",
        "name": "Dosquebradas"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.318",
        "name": "Guatica"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.383",
        "name": "La Celia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.4",
        "name": "La Virginia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.44",
        "name": "Marsella"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.456",
        "name": "Mistrato"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.572",
        "name": "Pueblo Rico"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.594",
        "name": "Quinchia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.687",
        "name": "Santuario"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.001",
        "name": "Bucaramanga"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.013",
        "name": "Aguada"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.02",
        "name": "Albania"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.051",
        "name": "Aratoca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.077",
        "name": "Barbosa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.079",
        "name": "Barichara"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.081",
        "name": "Barrancabermeja"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.092",
        "name": "Betulia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.101",
        "name": "Bolivar"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.121",
        "name": "Cabrera"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.132",
        "name": "California"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.152",
        "name": "Carcasi"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.16",
        "name": "Cepita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.162",
        "name": "Cerrito"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.167",
        "name": "Charala"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.169",
        "name": "Charta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.179",
        "name": "Chipata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.19",
        "name": "Cimitarra"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.207",
        "name": "Concepcion"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.209",
        "name": "Confines"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.211",
        "name": "Contratacion"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.217",
        "name": "Coromoro"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.229",
        "name": "Curiti"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.245",
        "name": "El Guacamayo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.255",
        "name": "El Playon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.264",
        "name": "Encino"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.266",
        "name": "Enciso"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.271",
        "name": "Florian"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.276",
        "name": "Floridablanca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.296",
        "name": "Galan"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.298",
        "name": "Gambita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.307",
        "name": "Giron"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.318",
        "name": "Guaca"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.32",
        "name": "Guadalupe"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.322",
        "name": "Guapota"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.324",
        "name": "Guavata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.327",
        "name": "Güepsa"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.368",
        "name": "Jesús Maria"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.37",
        "name": "Jordan"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.377",
        "name": "La Belleza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.385",
        "name": "Landazuri"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.397",
        "name": "La Paz"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.406",
        "name": "Lebrija"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.418",
        "name": "Los Santos"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.425",
        "name": "Macaravita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.432",
        "name": "Malaga"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.444",
        "name": "Matanza"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.464",
        "name": "Mogotes"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.468",
        "name": "Molagavita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.498",
        "name": "Ocamonte"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.5",
        "name": "Oiba"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.502",
        "name": "Onzaga"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.522",
        "name": "Palmar"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.533",
        "name": "Paramo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.547",
        "name": "Piedecuesta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.549",
        "name": "Pinchote"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.572",
        "name": "Puente Nacional"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.615",
        "name": "Rionegro"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.669",
        "name": "San Andrés"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.679",
        "name": "San Gil"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.682",
        "name": "San Joaquin"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.686",
        "name": "San Miguel"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.705",
        "name": "Santa Barbara"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.745",
        "name": "Simacota"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.755",
        "name": "Socorro"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.77",
        "name": "Suaita"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.773",
        "name": "Sucre"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.78",
        "name": "Surata"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.82",
        "name": "Tona"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.861",
        "name": "Vélez"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.867",
        "name": "Vetas"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.872",
        "name": "Villanueva"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.895",
        "name": "Zapatoca"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.001",
        "name": "Sincelejo"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.11",
        "name": "Buenavista"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.124",
        "name": "Caimito"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.204",
        "name": "Coloso"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.221",
        "name": "Coveñas"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.23",
        "name": "Chalan"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.233",
        "name": "El Roble"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.235",
        "name": "Galeras"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.265",
        "name": "Guaranda"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.4",
        "name": "La Union"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.418",
        "name": "Los Palmitos"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.429",
        "name": "Majagual"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.473",
        "name": "Morroa"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.508",
        "name": "Ovejas"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.523",
        "name": "Palmito"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.678",
        "name": "San Benito Abad"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.708",
        "name": "San Marcos"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.713",
        "name": "San Onofre"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.717",
        "name": "San Pedro"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.771",
        "name": "Sucre"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.823",
        "name": "Tolú Viejo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.024",
        "name": "Alpujarra"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.026",
        "name": "Alvarado"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.03",
        "name": "Ambalema"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.055",
        "name": "Armero"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.067",
        "name": "Ataco"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.124",
        "name": "Cajamarca"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.168",
        "name": "Chaparral"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.2",
        "name": "Coello"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.217",
        "name": "Coyaima"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.226",
        "name": "Cunday"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.236",
        "name": "Dolores"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.268",
        "name": "Espinal"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.27",
        "name": "Falan"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.275",
        "name": "Flandes"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.283",
        "name": "Fresno"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.319",
        "name": "Guamo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.347",
        "name": "Herveo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.349",
        "name": "Honda"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.352",
        "name": "Icononzo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.443",
        "name": "Mariquita"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.449",
        "name": "Melgar"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.461",
        "name": "Murillo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.483",
        "name": "Natagaima"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.504",
        "name": "Ortega"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.52",
        "name": "Palocabildo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.547",
        "name": "Piedras"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.555",
        "name": "Planadas"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.563",
        "name": "Prado"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.585",
        "name": "Purificacion"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.616",
        "name": "Rio Blanco"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.622",
        "name": "Roncesvalles"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.624",
        "name": "Rovira"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.671",
        "name": "Saldaña"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.686",
        "name": "Santa Isabel"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.861",
        "name": "Venadillo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.87",
        "name": "Villahermosa"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.873",
        "name": "Villarrica"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.065",
        "name": "Arauquita"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.22",
        "name": "Cravo Norte"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.3",
        "name": "Fortul"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.591",
        "name": "Puerto Rondon"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.736",
        "name": "Saravena"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.794",
        "name": "Tame"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "81",
        "departament": "Arauca",
        "municipality_dane_code": "81.001",
        "name": "Arauca"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.001",
        "name": "Yopal"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.01",
        "name": "Aguazul"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.015",
        "name": "Chameza"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.125",
        "name": "Hato Corozal"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.136",
        "name": "La Salina"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.162",
        "name": "Monterrey"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.263",
        "name": "Pore"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.279",
        "name": "Recetor"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.3",
        "name": "Sabanalarga"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.315",
        "name": "Sacama"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.41",
        "name": "Tauramena"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.43",
        "name": "Trinidad"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.44",
        "name": "Villanueva"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.001",
        "name": "Mocoa"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.219",
        "name": "Colon"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.32",
        "name": "Orito"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.569",
        "name": "Puerto Caicedo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.571",
        "name": "Puerto Guzman"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.573",
        "name": "Leguizamo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.749",
        "name": "Sibundoy"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.755",
        "name": "San Francisco"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.757",
        "name": "San Miguel"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.76",
        "name": "Santiago"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.001",
        "name": "Leticia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.263",
        "name": "El Encanto"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.405",
        "name": "La Chorrera"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.407",
        "name": "La Pedrera"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.43",
        "name": "La Victoria"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.536",
        "name": "Puerto Arica"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.54",
        "name": "Puerto Nariño"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.669",
        "name": "Puerto Santander"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.798",
        "name": "Tarapaca"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.001",
        "name": "Inirida"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.343",
        "name": "Barranco Minas"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.663",
        "name": "Mapiripana"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.883",
        "name": "San Felipe"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.884",
        "name": "Puerto Colombia"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.885",
        "name": "La Guadalupe"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.886",
        "name": "Cacahual"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.887",
        "name": "Pana Pana"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.001",
        "name": "Mitú"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.161",
        "name": "Carurú"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.666",
        "name": "Taraira"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.777",
        "name": "Papunahua"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.889",
        "name": "Yavaraté"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "97",
        "departament": "Vaupés",
        "municipality_dane_code": "97.511",
        "name": "Pacoa"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "94",
        "departament": "Guainia",
        "municipality_dane_code": "94.888",
        "name": "Morichal"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.001",
        "name": "Puerto Carreño"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.524",
        "name": "La Primavera"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.624",
        "name": "Santa Rosalia"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "99",
        "departament": "Vichada",
        "municipality_dane_code": "99.773",
        "name": "Cumaribo"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.61",
        "name": "San José del Fragua"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.11",
        "name": "Barranca de Upia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.524",
        "name": "Palmas del Socorro"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.662",
        "name": "San Juan de Rio Seco"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.372",
        "name": "Juan de Acosta"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.287",
        "name": "Fuente de Oro"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.325",
        "name": "San Luis de Gaceno"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.25",
        "name": "El Litoral del San Juan"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.843",
        "name": "Villa de San Diego de Ubate"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.074",
        "name": "Barranco de Loba"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.816",
        "name": "Togüi"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.688",
        "name": "Santa Rosa del Sur"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.135",
        "name": "El Canton del San Pablo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.407",
        "name": "Villa de Leyva"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.692",
        "name": "San Sebastian de Buenavista"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.537",
        "name": "Paz de Rio"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.3",
        "name": "Hatillo de Loba"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.66",
        "name": "Sabanas de San Angel"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.015",
        "name": "Calamar"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.614",
        "name": "Rio de Oro"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.665",
        "name": "San Pedro de Uraba"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.001",
        "name": "San José del Guaviare"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.693",
        "name": "Santa Rosa de Viterbo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.698",
        "name": "Santander de Quilichao"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.2",
        "name": "Miraflores"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.042",
        "name": "Santafé de Antioquia"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.68",
        "name": "San Carlos de Guaroa"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.52",
        "name": "Palmar de Varela"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.686",
        "name": "Santa Rosa de Osos"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.647",
        "name": "San Andrés de Cuerquia"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.854",
        "name": "Valle de San Juan"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.689",
        "name": "San Vicente de Chucuri"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.684",
        "name": "San José de Miranda"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "88",
        "departament": "Archipiélago de San Andrés, Providencia y Santa Catalina",
        "municipality_dane_code": "88.564",
        "name": "Providencia"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.682",
        "name": "Santa Rosa de Cabal"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.328",
        "name": "Guayabal de Siquima"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.094",
        "name": "Belén de Los Andaquies"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "85",
        "departament": "Casanare",
        "municipality_dane_code": "85.25",
        "name": "Paz de Ariporo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.72",
        "name": "Santa Helena del Opon"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.681",
        "name": "San Pablo de Borbur"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.42",
        "name": "La Jagua del Pilar"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "20",
        "departament": "Cesar",
        "municipality_dane_code": "20.4",
        "name": "La Jagua de Ibirico"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.742",
        "name": "San Luis de Sincé"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.667",
        "name": "San Luis de Gaceno"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.244",
        "name": "El Carmen de Bolivar"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.245",
        "name": "El Carmen de Atrato"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.702",
        "name": "San Juan de Betulia"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "47",
        "departament": "Magdalena",
        "municipality_dane_code": "47.545",
        "name": "Pijiño del Carmen"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.873",
        "name": "Vigia del Fuerte"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.667",
        "name": "San Martin de Loba"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.03",
        "name": "Altos del Rosario"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.148",
        "name": "Carmen de Apicala"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.645",
        "name": "San Antonio del Tequendama"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.655",
        "name": "Sabana de Torres"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "95",
        "departament": "Guaviare",
        "municipality_dane_code": "95.025",
        "name": "El Retorno"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.682",
        "name": "San José de Uré"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.694",
        "name": "San Pedro de Cartago"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "8",
        "departament": "Atlantico",
        "municipality_dane_code": "8.137",
        "name": "Campo de La Cruz"
    },
    {
        "region": "Region Llano",
        "departament_dane_code": "50",
        "departament": "Meta",
        "municipality_dane_code": "50.683",
        "name": "San Juan de Arama"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.658",
        "name": "San José de La Montaña"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "18",
        "departament": "Caqueta",
        "municipality_dane_code": "18.15",
        "name": "Cartagena del Chaira"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.66",
        "name": "San José del Palmar"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.001",
        "name": "Agua de Dios"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.655",
        "name": "San Jacinto del Cauca"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "41",
        "departament": "Huila",
        "municipality_dane_code": "41.668",
        "name": "San Agustin"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "52",
        "departament": "Nariño",
        "municipality_dane_code": "52.258",
        "name": "El Tablon de Gomez"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "88",
        "departament": "Archipiélago de San Andrés, Providencia y Santa Catalina",
        "municipality_dane_code": "88.001",
        "name": "San Andrés"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.664",
        "name": "San José de Pare"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "86",
        "departament": "Putumayo",
        "municipality_dane_code": "86.865",
        "name": "Valle de Guamez"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.67",
        "name": "San Pablo de Borbur"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "70",
        "departament": "Sucre",
        "municipality_dane_code": "70.82",
        "name": "Santiago de Tolú"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "11",
        "departament": "Bogota D.C.",
        "municipality_dane_code": "11.001",
        "name": "Bogota D.C."
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.154",
        "name": "Carmen de Carupa"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.189",
        "name": "Ciénaga de Oro"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.659",
        "name": "San Juan de Uraba"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "44",
        "departament": "La Guajira",
        "municipality_dane_code": "44.65",
        "name": "San Juan del Cesar"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.235",
        "name": "El Carmen de Chucuri"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.148",
        "name": "El Carmen de Viboral"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "66",
        "departament": "Risaralda",
        "municipality_dane_code": "66.088",
        "name": "Belén de Umbria"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "27",
        "departament": "Choco",
        "municipality_dane_code": "27.086",
        "name": "Belén de Bajira"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.855",
        "name": "Valle de San José"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.678",
        "name": "San Luis"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.676",
        "name": "San Miguel de Sema"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "73",
        "departament": "Tolima",
        "municipality_dane_code": "73.675",
        "name": "San Antonio"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.673",
        "name": "San Benito"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "25",
        "departament": "Cundinamarca",
        "municipality_dane_code": "25.862",
        "name": "Vergara"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "23",
        "departament": "Cordoba",
        "municipality_dane_code": "23.678",
        "name": "San Carlos"
    },
    {
        "region": "Region Centro Sur",
        "departament_dane_code": "91",
        "departament": "Amazonas",
        "municipality_dane_code": "91.53",
        "name": "Puerto Alegria"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "68",
        "departament": "Santander",
        "municipality_dane_code": "68.344",
        "name": "Hato"
    },
    {
        "region": "Region Caribe",
        "departament_dane_code": "13",
        "departament": "Bolivar",
        "municipality_dane_code": "13.654",
        "name": "San Jacinto"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "19",
        "departament": "Cauca",
        "municipality_dane_code": "19.693",
        "name": "San Sebastian"
    },
    {
        "region": "Region Eje Cafetero - Antioquia",
        "departament_dane_code": "5",
        "departament": "Antioquia",
        "municipality_dane_code": "5.649",
        "name": "San Carlos"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "15",
        "departament": "Boyaca",
        "municipality_dane_code": "15.837",
        "name": "Tuta"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.743",
        "name": "Silos"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.125",
        "name": "Cacota"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.25",
        "name": "El Dovio"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.82",
        "name": "Toledo"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.622",
        "name": "Roldanillo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.48",
        "name": "Mutiscua"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.054",
        "name": "Argelia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.261",
        "name": "El Zulia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.66",
        "name": "Salazar"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.736",
        "name": "Sevilla"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.895",
        "name": "Zarzal"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.223",
        "name": "Cucutilla"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.248",
        "name": "El Cerrito"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.147",
        "name": "Cartago"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.122",
        "name": "Caicedonia"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.553",
        "name": "Puerto Santander"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.313",
        "name": "Gramalote"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.246",
        "name": "El Cairo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.25",
        "name": "El Tarra"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.25",
        "name": "San Jose de Cucuta"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.4",
        "name": "La Union"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.606",
        "name": "Restrepo"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.8",
        "name": "Teorama"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.233",
        "name": "Dagua"
    },
    {
        "region": "Region Centro Oriente",
        "departament_dane_code": "54",
        "departament": "Norte de Santander",
        "municipality_dane_code": "54.051",
        "name": "Arboledas"
    },
    {
        "region": "Region Pacifico",
        "departament_dane_code": "76",
        "departament": "Valle del Cauca",
        "municipality_dane_code": "76.318",
        "name": "Guacari"
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

   