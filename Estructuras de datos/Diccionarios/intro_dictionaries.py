#Crear diccionarios

mi_diccionario = {}

mi_diccionario ['nombre'] = 'Jon'
mi_diccionario ['edad'] = 30
mi_diccionario ['residencia'] = 'Sopela'
mi_diccionario ['universidad'] = 'UPV/EHU'

print(mi_diccionario)

otro_diccionario = {
    'nombre':'Jon',
    'apodo': 'Mada',
    'año de nacimiento': 1993
}

print(otro_diccionario)

#¿Cómo hacer búsquedas de valores?
players = {
    'DL': 'Williams',
    'MC': 'Sancet',
    'DEF': 'Vivian',
    'POR': 'Simón'
}

delantero = players ['DL']
print(delantero)