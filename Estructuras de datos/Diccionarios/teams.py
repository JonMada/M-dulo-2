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

print(teams[0]) #Seleccionamos en la lista el valor de nuestro diccionario
print(teams[0].get('athletic'))
print(list(teams[0].get('athletic').values())[0])
