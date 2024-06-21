from models.specialities import *

specialities_to_create = [
	{
		"code" : "00",
		"description" : "SIN ESPECIALIDAD"
	},
	{
		"code" : "001",
		"description" : "MEDICINA FISICA Y REHABILITACION"
	},
	{
		"code" : "002",
		"description" : "FISIOTERAPIA"
	},
	{
		"code" : "003",
		"description" : "FONOAUDIOLOGIA"
	},
	{
		"code" : "004",
		"description" : "MEDICO GENERAL"
	},
	{
		"code" : "005",
		"description" : "SALUD OCUPACIONAL"
	},
	{
		"code" : "006",
		"description" : "NUTRICIONISTA DIETISTA"
	},
	{
		"code" : "007",
		"description" : "PSICOLOGIA"
	},
	{
		"code" : "008",
		"description" : "TERAPIA OCUPACIONAL"
	},
	{
		"code" : "009",
		"description" : "NEUROCIRUG A"
	},
	{
		"code" : "010",
		"description" : "MEDICINA LABORAL"
	},
	{
		"code" : "011",
		"description" : "FISIATRIA"
	},
	{
		"code" : "012",
		"description" : "TERAPIA FISICA"
	},
	{
		"code" : "013",
		"description" : "ESPIROMETRIA"
	},
	{
		"code" : "014",
		"description" : "ORTOPEDIA Y TRAUMATOLOGIA"
	},
	{
		"code" : "015",
		"description" : "CIRUGIA DE LA MANO"
	},
	{
		"code" : "016",
		"description" : "VISITA DOMICILIARIA ENFERMERIA"
	},
	{
		"code" : "017",
		"description" : "CIRUGIA MAXILOFACIAL"
	},
	{
		"code" : "018",
		"description" : "ALGOLOGA"
	},
	{
		"code" : "019",
		"description" : "LINEA BLANDA"
	},
	{
		"code" : "24",
		"description" : "TRASLADO DE PACIENTES"
	},
	{
		"code" : "09",
		"description" : "GRUPO # 09"
	},
	{
		"code" : "20",
		"description" : "GRUPO # 20"
	},
	{
		"code" : "08",
		"description" : "GRUPO # 08"
	},
	{
		"code" : "12",
		"description" : "GRUPO # 12"
	},
	{
		"code" : "13",
		"description" : "GRUPO # 13"
	},
	{
		"code" : "21",
		"description" : "GRUPO # 21"
	},
	{
		"code" : "23",
		"description" : "GRUPO # 23"
	},
	{
		"code" : "22",
		"description" : "GRUPO # 22"
	},
	{
		"code" : "05",
		"description" : "GRUPO # 05"
	},
	{
		"code" : "07",
		"description" : "GRUPO # 07"
	},
	{
		"code" : "03",
		"description" : "GRUPO # 03"
	},
	{
		"code" : "06",
		"description" : "GRUPO # 06"
	},
	{
		"code" : "10",
		"description" : "GRUPO # 10"
	},
	{
		"code" : "11",
		"description" : "GRUPO # 11"
	},
	{
		"code" : "04",
		"description" : "GRUPO # 04"
	},
	{
		"code" : "02",
		"description" : "GRUPO # 02"
	},
	{
		"code" : "25",
		"description" : "DOLOR Y CUIDADOS PALIATIVOS"
	},
	{
		"code" : "020",
		"description" : "CIRUGIA PLASTICA"
	},
	{
		"code" : "26",
		"description" : "MATERIAL DE OSTEOSINTESIS"
	},
	{
		"code" : "021",
		"description" : "PSQUIATRIA"
	},
	{
		"code" : "027",
		"description" : "PSIQUIATRIA"
	},
	{
		"code" : "27",
		"description" : "INTERESES DE MORA"
	},
	{
		"code" : "28",
		"description" : "SALUD OCUPACIONAL"
	},
	{
		"code" : "0010",
		"description" : "PSIQUIATRIA"
	},
	{
		"code" : "112",
		"description" : "CONSULTORIO 112"
	},
	{
		"code" : "29",
		"description" : "LABORATORIO CLINICO"
	},
	{
		"code" : "30",
		"description" : "ENFERMERIA"
	},
	{
		"code" : "31",
		"description" : "FARMACIA"
	},
	{
		"code" : "0011",
		"description" : "AUXILIAR DE ENFERMERIA"
	},
	{
		"code" : "32",
		"description" : "MEDICINA INTERNA"
	},
	{
		"code" : "33",
		"description" : "ODONTOLOGIA"
	},
	{
		"code" : "35",
		"description" : "MANEJO DEL DOLOR Y CUIDADO PALIATIVO"
	},
	{
		"code" : "456",
		"description" : "REGENTE DE FARMACIA"
	},
	{
		"code" : "34",
		"description" : "IMAGENOLOGIA"
	},
	{
		"code" : "AMB",
		"description" : "AMBULANCIA"
	},
	{
		"code" : "CHB",
		"description" : "CAMARA HIPERBARICA"
	},
	{
		"code" : "SLP",
		"description" : "SALA DE PROCEDIMIENTOS"
	},
	{
		"code" : "GOLD",
		"description" : "PAQUETE GOLD"
	},
	{
		"code" : "CARE",
		"description" : "PAQUETE CARE"
	},
	{
		"code" : "SILVE",
		"description" : "PAQUETE SILVER"
	}
]

for specialities_to_create in specialities_to_create:
   specialities =Specialities.objects.create(**specialities_to_create)
   print("Created Specialities:", specialities)