equipos = {
    'Athletic':['Williams','Prados','Sancet','Nico','Berenguer'],
    'Real Sociedad': ['Kubo', 'Oyarzabal', 'Rico', 'Remiro'],
    'Barcelona': ['Pedri', 'Martínez', 'Koundé']
}

# equipos_destacados = equipos['Valladolid'] #No dará error al no encontrarse en el diccionario

#A través de 'get()' podemos establecer el valor que dolverá si no se encuentra la clae

print(equipos.get('Valladolid', 'No se pudo encontrar el equipo'))
