equipos = {
    'Athletic':['Williams','Prados','Sancet','Nico','Berenguer'],
    'Real Sociedad': ['Kubo', 'Oyarzabal', 'Rico', 'Remiro'],
    'Barcelona': ['Pedri', 'Martínez', 'Koundé']
}

# Delete Command
del equipos['Barcelona']
print(equipos)

# Pop() function
print(equipos.pop('Madrid','No se ha podido encontrar el equipo'))

removed_team = equipos.pop('Real Sociedad','No se ha podido encontrar el equipo') #Nos permite asociar el valor de la clave eliminada a un objeto
print(removed_team)