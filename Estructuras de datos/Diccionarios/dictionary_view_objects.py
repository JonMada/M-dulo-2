
equipos = {
    'Athletic':['Williams','Prados','Sancet','Nico','Berenguer'],
    'Real Sociedad': ['Kubo', 'Oyarzabal', 'Rico', 'Remiro'],
    'Barcelona': ['Pedri', 'Martínez', 'Koundé']
}

#Visualizar las keys, los values y los items de nuestro diccionarios 
print(equipos.keys())
print(equipos.values())
print(equipos.items())

#Los objetos dict_keys/values/items no nos permite trabajar con las keys como listas, salvo si aplicamos list():
print(list(equipos.keys())[0])

#Si queremos mantener una versión anterior de las keys (valores o items) sin que se registren los posibles cambios en el dictionary, utilizamos 'copy()':
import copy 
nombres_equipos = list(equipos.copy().keys())
print(nombres_equipos)

#Añadimos otro equipo para comprobar que funciona la función 'copy()' en la versión anterior
equipos['Sevilla'] = ['Rakitic']
nombres_equipos_cambiados = list(equipos.keys())
print(nombres_equipos_cambiados)

#Otras funciones aplicables a un objeto vista
#Length
print(len(equipos.keys()))

#Trabajando con tuples
print(equipos.items()) #Nos devuelve una tuple
print(list(equipos.items())[0][1][2]) #Del primer elemento de la tupla, coger su segundo elemento, y de ese coger el tercer elemento.






