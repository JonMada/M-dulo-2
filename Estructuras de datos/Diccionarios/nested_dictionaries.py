#Estructura de diccionarios anidados

teams = [
    {
        'athletic':{
            'delantero': 'Williams',
            'medio': 'Sancet',
            'defensa': 'Vivian'
        }
    },
    {
        'barcelona':{
            'delantero': 'Yamal',
            'medio': 'Pedri',
            'defensa': 'Koundé'
        }
    }
]

print(teams)

#Si queremos obtener el primer key:
print(teams[0]) #Obtenemos nuestro key 'athletic' con un valor en el que se almacena el diccionario 

#Si queremos obtener el diccionario con sus claves y sus valores. Primero lo tratamos como lista, luego como diccionario:
barcelona = teams[1].get('barcelona', 'No se ha encontrado el equipo')
print(barcelona)

#Si queremos obtener los valores del diccionario
print(barcelona.values())
print(list(barcelona.values())) #Transformamos el view object en una lista
print(list(barcelona.values())[2]) #Seleccionamos el valor deseado de la lista 
