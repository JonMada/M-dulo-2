#Creación de una lista
users = ['Valeria', 'Mada', 'Bruce']

#Si quisiesemos insertar otro elemento en la lista utilizamos la función 'insert()'
users.insert(0,'Ane') #El primer argumento indica la posición en la que queremos insertar el elemento dentro de la lista
print(users)

#Si queremos insertar un elemento y nos da igual la posición 'append()'
users.append('Kel')
print(users)

#¿Cómo seleccionar un elemento del objeto lista?
print(users[2]) #Esto nos devuelve el elemento y su tipo
print([users[2]]) #Esto nos devuelve el elemento y lo mantiene como lista

#Cambiar valores de los elementos del objeto lista
users[2] = 'Patxi' #Estamos asignando al elemento en posición dos de la lista 'users' el valor 'Patxi'
print(users)