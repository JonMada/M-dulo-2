#Colecciones anidadas dentro del los diccionarios

equipos = {
    'Athletic':['Williams','Prados','Sancet','Nico','Berenguer'],
    'Real Sociedad': ['Kubo', 'Oyarzabal', 'Rico', 'Remiro'],
    'Barcelona': ['Pedri', 'Martínez', 'Koundé']
}

print(equipos)
print(equipos['Athletic'])
print(equipos['Real Sociedad'])
print(equipos['Barcelona'])

#Son capaces de soportar estas listas los mismos procesos que de manera aislada.
slice_object = slice(2)
print(equipos['Athletic'][slice_object])
print(equipos['Athletic'][:2])

athletic = equipos['Athletic']
print(athletic)